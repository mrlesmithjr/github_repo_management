"""github_repo_management/cli.py"""

import argparse
from github_repo_management.release import __package_name__, __version__


def cli_args():
    """Console script for github_repo_management."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--version", action="version", version=f"{__package_name__} {__version__}"
    )
    args = parser.parse_args()

    return args
