"""Refresh the static site's skill download. Run from any directory with Python 3.9+."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import tempfile


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'docs' / 'downloads' / 'flightline-0.1.0.zip'


def main():
    files = [ROOT / name for name in ('SKILL.md', 'README.md', 'LICENSE', 'NOTICE')]
    for directory in ('agents', 'references', 'scripts', 'evaluations'):
        files.extend(path for path in (ROOT / directory).rglob('*')
                     if path.is_file() and '__pycache__' not in path.parts
                     and not any(part.startswith('.') for part in path.relative_to(ROOT).parts))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=OUTPUT.parent, suffix='.tmp', delete=False) as handle:
        temporary = Path(handle.name)
    try:
        with ZipFile(temporary, 'w', ZIP_DEFLATED) as archive:
            for path in sorted(files):
                archive.write(path, 'flightline/' + path.relative_to(ROOT).as_posix())
        with ZipFile(temporary) as archive:
            assert archive.testzip() is None, 'Download archive failed integrity check'
            for path in files:
                assert archive.read('flightline/' + path.relative_to(ROOT).as_posix()) == path.read_bytes()
        temporary.replace(OUTPUT)
    finally:
        temporary.unlink(missing_ok=True)
    print(f'Packaged and verified {len(files)} files: {OUTPUT}')


if __name__ == '__main__':
    main()
