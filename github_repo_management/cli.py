"""github_repo_management/cli.py"""

import click
import json
from github_repo_management.resources.users import Users
from github_repo_management.resources.repos import Repos


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


@cli.command()
@click.pass_context
def get_repos(ctx: object):
    """[summary]

    Args:
        ctx ([type]): [description]
    """
    user = auth(ctx)
    repos = Repos(user, ctx)
    repos = repos.get_repos()


@cli.command()
@click.pass_context
def get_repo_secrets(ctx: object):
    """[summary]

    Args:
        ctx ([type]): [description]
    """
    user = auth(ctx)
    repos = Repos(user, ctx)
    repo_secrets = repos.get_secrets()
    print(json.dumps(repo_secrets))


@cli.command()
@click.pass_context
def add_repo_secrets(ctx: object):
    user = auth(ctx)
    repos = Repos(user, ctx)
    repos.add_secrets()


cli.add_command(get_repos)
cli.add_command(get_repo_secrets)
cli.add_command(add_repo_secrets)
