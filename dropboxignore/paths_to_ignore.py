# Standard library imports
from pathlib import Path


def read_ignore_file(path: Path):
    """Parse an ignore file of glob patterns"""
    text = [l.strip() for l in path.read_text(encoding="UTF-8").strip().split("\n")]
    return list(filter(lambda s: s != "", text))


def get_paths_to_ignore(root: Path, globs: list[str]):
    """Provide list of files that match any of the glob patterns"""
    paths_to_ignore = []
    for glob_pattern in globs:
        folders = root.glob(glob_pattern)

        for folder in folders:
            skip = False
            for ignored_path in paths_to_ignore:
                if ignored_path in folder.parents:
                    skip = True
                    break
            if skip is True:
                continue
            elif skip is False:
                paths_to_ignore.append(folder)
    return paths_to_ignore
