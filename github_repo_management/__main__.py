"""github_repo_management/__main__.py"""
from github_repo_management.cli import cli
from github_repo_management.logger import setup_logger


def main():
    """Main execution of package."""

    # Setup root logger
    setup_logger()

    cli()


if __name__ == "__main__":
    main()
