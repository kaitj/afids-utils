"""
This type stub file was generated by pyright.
"""

from ._version import get_versions

__version__ = get_versions()["version"]
def stable_semver(): # -> str:
    """
    Get the stable portion of the semantic version string (the first three
    numbers), without any of the trailing labels

    '3.0.0rc11' -> '3.0.0'
    """
    ...

