"""github_repo_management/cli.py"""

import click
from github_repo_management.resources.users import Users


@click.group()
@click.option("--token", required=True, help="GitHub API token.")
@click.option("--user", help="GitHub user to manage.")
@click.pass_context
def cli(ctx, token, user):
    """[summary]

    Args:
        ctx ([type]): [description]
        token ([type]): [description]
        user ([type]): [description]
    """
    ctx.obj = {"token": token, "user": user}


@cli.command()
@click.pass_context
def user(ctx):
    """[summary]

    Args:
        ctx ([type]): [description]
    """
    users = Users(ctx)
    users.auth()


cli.add_command(user)
