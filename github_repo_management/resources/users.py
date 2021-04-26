from github import Github, GithubException


class Users:
    """[summary]"""

    def __init__(self, ctx):
        """[summary]

        Args:
            ctx ([type]): [description]
        """
        self.token = ctx.obj["token"]
        self.user = ctx.obj["user"]

    def auth(self):
        """[summary]"""
        try:
            gh = Github(self.token)
            return gh
        except GithubException as e:
            print(e)
            exit(2)
