"""
Package-level docstring.

Provide high-level description of the submodules of the package.

Submodules:
 - configs: configuration classes for data pipeline, model training, etc
 - utils: collection of useful helper functions
"""
from asset_selector.configs.style import Style, change_style
STYLE = Style.LIGHT
change_style(STYLE)
