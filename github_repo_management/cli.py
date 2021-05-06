"""github_repo_management/cli.py"""

import click
import json
from github_repo_management.resources.users import Users
from github_repo_management.resources.repos import Repos


@click.group()
@click.option("--token", required=True, help="GitHub API token.")
@click.pass_context
def cli(ctx: object, token: str):
    """[summary]

    Args:
        ctx (object): [description]
        token (str): [description]
    """
    user = auth(token)
    ctx.obj = {"token": token, "user": user}


def auth(token: str):
    """[summary]

    Args:
        token (str): [description]

    Returns:
        [type]: [description]
    """
    users = Users(token)
    user = users.auth().get_user()
    return user


@cli.command()
@click.pass_context
def get_repos(ctx: object):
    """[summary]

    Args:
        ctx ([type]): [description]
    """
    repos = Repos(ctx)
    repos = repos.get_repos()


@cli.command()
@click.pass_context
def get_repo_secrets(ctx: object):
    """[summary]

    Args:
        ctx ([type]): [description]
    """
    repos = Repos(ctx)
    repo_secrets = repos.get_secrets()
    print(json.dumps(repo_secrets))


@cli.command()
@click.pass_context
def add_repo_secrets(ctx: object):
    """[summary]

    Args:
        ctx (object): [description]
    """
    repos = Repos(ctx)
    repos.add_secrets()


cli.add_command(get_repos)
cli.add_command(get_repo_secrets)
cli.add_command(add_repo_secrets)
