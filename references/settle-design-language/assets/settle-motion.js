/* Settle motion runtime: springs, press, proximity, rubber-banding and velocity tracking.
   Vanilla JavaScript, no dependencies. Exposes window.Settle. */
(function () {
  'use strict';

  /* The four springs. Damping ratio = damping / (2 * sqrt(stiffness * mass)). */
  var presets = {
    snappy: { stiffness: 520, damping: 34, mass: 1 },
    settle: { stiffness: 300, damping: 22, mass: 1 },
    gentle: { stiffness: 220, damping: 24, mass: 1 },
    heavy: { stiffness: 160, damping: 26, mass: 1.6 }
  };

  var mq = window.matchMedia ? window.matchMedia('(prefers-reduced-motion: reduce)') : null;

  function reduced() {
    return !!(mq && mq.matches);
  }

  function clamp(v, min, max) {
    return v < min ? min : v > max ? max : v;
  }

  function lerp(a, b, t) {
    return a + (b - a) * t;
  }

  /* Spring
     opts: from, preset ('snappy' | 'settle' | 'gentle' | 'heavy'), stiffness, damping, mass,
           precision (rest threshold in the value's own units), onUpdate(value, spring),
           onRest(value, spring), reducedMotion (false to animate even when reduced motion is set),
           paint (false to skip the initial onUpdate call). */
  function Spring(opts) {
    opts = opts || {};
    var p = presets[opts.preset] || presets.settle;
    this.stiffness = opts.stiffness != null ? opts.stiffness : p.stiffness;
    this.damping = opts.damping != null ? opts.damping : p.damping;
    this.mass = opts.mass != null ? opts.mass : p.mass;
    this.precision = opts.precision != null ? opts.precision : 0.001;
    this.value = opts.from != null ? opts.from : 0;
    this.target = this.value;
    this.velocity = 0;
    this.onUpdate = opts.onUpdate || null;
    this.onRest = opts.onRest || null;
    this.respectReducedMotion = opts.reducedMotion !== false;
    this._raf = 0;
    this._last = 0;
    this._tick = this._tick.bind(this);
    if (this.onUpdate && opts.paint !== false) this.onUpdate(this.value, this);
  }

  /* Move toward a target. Velocity is kept unless one is passed, so interruptions stay smooth. */
  Spring.prototype.to = function (target, velocity) {
    this.target = target;
    if (typeof velocity === 'number' && isFinite(velocity)) this.velocity = velocity;
    if (this.respectReducedMotion && reduced()) return this.jump(target);
    if (!this._raf) {
      this._last = performance.now();
      this._raf = requestAnimationFrame(this._tick);
    }
    return this;
  };

  /* Place the value immediately, with no motion. */
  Spring.prototype.jump = function (value) {
    this.stop();
    this.value = value;
    this.target = value;
    this.velocity = 0;
    if (this.onUpdate) this.onUpdate(value, this);
    if (this.onRest) this.onRest(value, this);
    return this;
  };

  Spring.prototype.stop = function () {
    if (this._raf) cancelAnimationFrame(this._raf);
    this._raf = 0;
    return this;
  };

  Spring.prototype.use = function (name) {
    var p = presets[name];
    if (p) {
      this.stiffness = p.stiffness;
      this.damping = p.damping;
      this.mass = p.mass;
    }
    return this;
  };

  Spring.prototype.isMoving = function () {
    return this._raf !== 0;
  };

  Spring.prototype._tick = function (now) {
    var dt = Math.min((now - this._last) / 1000, 1 / 20);
    this._last = now;
    var steps = Math.max(1, Math.ceil(dt * 240));
    var h = dt / steps;
    var i, force;
    for (i = 0; i < steps; i++) {
      force = -this.stiffness * (this.value - this.target) - this.damping * this.velocity;
      this.velocity += (force / this.mass) * h;
      this.value += this.velocity * h;
    }
    var atRest = Math.abs(this.velocity) < this.precision * 10 && Math.abs(this.value - this.target) < this.precision;
    if (atRest) {
      this.value = this.target;
      this.velocity = 0;
      this._raf = 0;
    }
    if (this.onUpdate) this.onUpdate(this.value, this);
    if (atRest) {
      if (this.onRest) this.onRest(this.value, this);
    } else {
      this._raf = requestAnimationFrame(this._tick);
    }
  };

  function spring(opts) {
    return new Spring(opts);
  }

  /* Press: scale to 0.97 on pointerdown or Space/Enter (snappy), release with the settle overshoot.
     Writes --st-press on the element; .st-pressable and .st-btn read it in transform. */
  function press(el, opts) {
    opts = opts || {};
    var scale = opts.scale || 0.97;
    var down = false;
    var s = new Spring({
      from: 1,
      preset: 'snappy',
      precision: 0.0005,
      onUpdate: function (v) {
        el.style.setProperty('--st-press', v.toFixed(4));
      }
    });
    function isDisabled() {
      return el.disabled || el.getAttribute('aria-disabled') === 'true';
    }
    function start() {
      if (isDisabled()) return;
      down = true;
      s.use('snappy').to(scale);
    }
    function end() {
      if (!down) return;
      down = false;
      s.use('settle').to(1);
    }
    el.addEventListener('pointerdown', function (e) {
      if (e.button === 0) start();
    });
    el.addEventListener('pointerup', end);
    el.addEventListener('pointerleave', end);
    el.addEventListener('pointercancel', end);
    el.addEventListener('keydown', function (e) {
      if ((e.key === ' ' || e.key === 'Enter') && !e.repeat) start();
    });
    el.addEventListener('keyup', function (e) {
      if (e.key === ' ' || e.key === 'Enter') end();
    });
    el.addEventListener('blur', end);
    return s;
  }

  /* Proximity: a light that follows the pointer near an element. Lighting only, never movement.
     Writes --st-lx, --st-ly (px from the element's top-left) and --st-light (0 to 1). */
  function proximity(el, opts) {
    opts = opts || {};
    var radius = opts.radius || 80;
    var x = new Spring({ preset: 'gentle', precision: 0.1, onUpdate: function (v) { el.style.setProperty('--st-lx', v.toFixed(1) + 'px'); } });
    var y = new Spring({ preset: 'gentle', precision: 0.1, onUpdate: function (v) { el.style.setProperty('--st-ly', v.toFixed(1) + 'px'); } });
    var a = new Spring({ preset: 'gentle', precision: 0.002, onUpdate: function (v) { el.style.setProperty('--st-light', clamp(v, 0, 1).toFixed(3)); } });
    function move(e) {
      if (e.pointerType === 'touch') return;
      var r = el.getBoundingClientRect();
      var px = e.clientX - r.left;
      var py = e.clientY - r.top;
      var dx = Math.max(0, -px, px - r.width);
      var dy = Math.max(0, -py, py - r.height);
      var d = Math.sqrt(dx * dx + dy * dy);
      var near = d >= radius ? 0 : 1 - d / radius;
      if (near > 0 && a.value < 0.02) {
        x.jump(px);
        y.jump(py);
      } else {
        x.to(px);
        y.to(py);
      }
      a.to(d === 0 ? 1 : near * 0.6);
    }
    function leave() {
      a.to(0);
    }
    document.addEventListener('pointermove', move, { passive: true });
    document.documentElement.addEventListener('pointerleave', leave);
    return {
      destroy: function () {
        document.removeEventListener('pointermove', move);
        document.documentElement.removeEventListener('pointerleave', leave);
      }
    };
  }

  /* Rubber-banding: resistance grows with distance past a boundary.
     overflow = distance past the edge (px), size = the dimension it belongs to (px). */
  function rubber(overflow, size, constant) {
    var c = constant || 0.55;
    var sign = overflow < 0 ? -1 : 1;
    var x = Math.abs(overflow);
    return sign * (1 - 1 / ((x * c) / size + 1)) * size;
  }

  /* Velocity tracker over the last 100ms, in units per second. */
  function tracker() {
    var pts = [];
    return {
      add: function (v) {
        var t = performance.now();
        pts.push([t, v]);
        while (pts.length > 2 && t - pts[0][0] > 100) pts.shift();
      },
      velocity: function () {
        if (pts.length < 2) return 0;
        var a = pts[0];
        var b = pts[pts.length - 1];
        var dt = (b[0] - a[0]) / 1000;
        return dt > 0 ? (b[1] - a[1]) / dt : 0;
      },
      reset: function () {
        pts = [];
      }
    };
  }

  /* Sample a preset into a CSS linear() easing, plus the duration it needs. */
  function linear(name, samples) {
    var p = presets[name] || presets.settle;
    var n = samples || 24;
    var x = 0, v = 0, t = 0, h = 1 / 1000, trace = [], last = 0, i, f, k;
    while (t < 3) {
      f = -p.stiffness * (x - 1) - p.damping * v;
      v += (f / p.mass) * h;
      x += v * h;
      t += h;
      trace.push(x);
      if (Math.abs(x - 1) > 0.002) last = trace.length;
    }
    var stops = ['0'];
    for (i = 1; i < n; i++) {
      k = Math.round((last * i) / (n - 1)) - 1;
      stops.push(String(Math.round(trace[Math.max(0, k)] * 1000) / 1000));
    }
    stops[n - 1] = '1';
    return { easing: 'linear(' + stops.join(', ') + ')', duration: Math.round(last) + 'ms' };
  }

  window.Settle = {
    springs: presets,
    Spring: Spring,
    spring: spring,
    reduced: reduced,
    press: press,
    proximity: proximity,
    rubber: rubber,
    tracker: tracker,
    linear: linear,
    clamp: clamp,
    lerp: lerp
  };
})();
