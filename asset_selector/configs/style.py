"""
Method and Enum for changing plotting style for Matplotlib and Seaborn.
"""
from enum import Enum
import matplotlib.pyplot as plt
from asset_selector.configs.directories import Directories


class Style:
    """Halfspace style class."""

    LIGHT = "light"
    DARK = "dark"


def change_style(style: Style):
    """Change matplotlib style."""
    mpl_path = Directories.MODULE_PATH / "configs" / f"halfspace_{style}.mplstyle"
    plt.style.use(mpl_path)
