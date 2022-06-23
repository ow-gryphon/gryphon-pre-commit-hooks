import argparse
from glob import glob
from pathlib import Path
from typing import Sequence


def main(argv: Sequence[str] = None):

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filenames', nargs='*',
        help='Filenames pre-commit believes are changed.',
    )
    args = parser.parse_args(argv)

    path = Path.cwd()
    # gitignore = path / ".gitignore"

    pattern = str(path / '**')
    pattern2 = str(path / '.**')

    files = glob(pattern, recursive=True)
    files_2 = glob(pattern2, recursive=True)

    files.extend(files_2)

    failed = False
    unnecessary_files = []
    for f in args.filenames:
        f = str(f)
        if (
            '__pycache__/' in f or
            '.ipynb_checkpoint/' in f or
            '.venv/' in f or
            'dist/' in f or
            'build/' in f or
            '.eeg-info/' in f or
            '.git/' in f or
            '.github/' in f or
            'envs/' in f
        ):
            unnecessary_files.append(f)
            failed = True

    if failed:
        raise SystemExit(1)
    else:
        raise SystemExit(0)


if __name__ == "__main__":
    main()
