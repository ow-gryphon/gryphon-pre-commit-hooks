from glob import glob
from pathlib import Path


def main():
    glob(Path.cwd(), recursive=True)


if __name__ == "__main__":
    raise SystemExit(main())
