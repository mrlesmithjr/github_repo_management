from github import Github


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
        gh = Github(self.token)

        return gh
