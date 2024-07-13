"""Holds class with different paths."""

from dataclasses import dataclass
from pathlib import Path

import asset_selector


@dataclass
class Directories:
    """Class with all paths used in the repository."""

    REPO_PATH = Path(asset_selector.__file__).parent.parent
    MODULE_PATH = Path(asset_selector.__file__).parent
    LOCAL_DATA_FOLDER = REPO_PATH / "local_data"
    DATA_PATH = REPO_PATH / "data"
    TESTS = REPO_PATH / "tests"
    TESTS_DATA = TESTS / "data"
    LOGGING_FOLDER = REPO_PATH / "logs"
