"""github_repo_management/cli.py"""

import click
from github_repo_management.resources.users import Users


@click.group()
@click.option("--token", required=True, help="GitHub API token.")
@click.option("--user", help="GitHub user to manage.")
@click.pass_context
def cli(ctx: object, token: str, user: str):
    """[summary]

    Args:
        ctx (object): [description]
        token (str): [description]
        user (str): [description]
    """
    ctx.obj = {"token": token, "user": user}


def auth(ctx: object):
    """[summary]

    Args:
        ctx (object): [description]

    Returns:
        [type]: [description]
    """
    users = Users(ctx)
    user = users.auth().get_user()
    return user
