import argparse
import logging
from glob import glob
from pathlib import Path
from typing import Sequence

from colorlog import ColoredFormatter

formatter = ColoredFormatter(
    "%(log_color)s%(message)s",
    log_colors={
        'WARNING': 'yellow',
    }
)


console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger = logging.getLogger('gryphon')
logger.addHandler(console_handler)

substrings = [
    '__pycache__/',
    '.ipynb_checkpoint/',
    '.venv/',
    'dist/',
    'build/',
    '.eeg-info/',
    '.git/',
    '.github/',
    'envs/',
    '.pem',
    '.yaml',
    '.yml',
    '.rc'
]


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

    unnecessary_files = []
    for f in args.filenames:
        f = str(f)
        for s in substrings:
            if s in f:
                logger.warning(f"WARNING: File \"{f}\" was committed. "
                               f"Check if you really want it inside your repository.")
                unnecessary_files.append(f)

    raise SystemExit(0)


if __name__ == "__main__":
    main()
