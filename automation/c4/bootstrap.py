"""Verify every member before extracting the reviewed runtime. No third party deps."""
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import zipfile


def extract(bundle, manifest, destination):
    if len(bundle) != manifest['size'] or hashlib.sha256(bundle).hexdigest() != manifest['sha256']:
        raise ValueError('Runtime archive SHA/size mismatch')
    files = manifest['files']
    with zipfile.ZipFile(io.BytesIO(bundle)) as archive:
        if len(archive.infolist()) != len(files) or sum(x.file_size for x in archive.infolist()) > 200 * 1024 * 1024:
            raise ValueError('Runtime inventory/size mismatch')
        seen = set()
        validated = []
        for item in archive.infolist():
            name = item.filename
            if name in seen or name not in files or PurePosixPath(name).is_absolute() or '\\' in name or '..' in name.split('/'):
                raise ValueError('Unsafe runtime member')
            path = (destination / name).resolve()
            if not path.is_relative_to(destination.resolve()) or path.is_symlink() or destination.exists():
                raise ValueError('Runtime must use a fresh isolated directory')
            data = archive.read(item)
            if len(data) != files[name]['size'] or hashlib.sha256(data).hexdigest() != files[name]['sha256']:
                raise ValueError('Runtime member SHA/size mismatch')
            seen.add(name)
            validated.append((path, data))
    for path, data in validated:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)


if __name__ == '__main__':
    home = Path(__file__).resolve().parent
    extract((home / 'runtime.zip').read_bytes(), json.loads((home / 'runtime.json').read_bytes()),
            Path('runtime').resolve())
