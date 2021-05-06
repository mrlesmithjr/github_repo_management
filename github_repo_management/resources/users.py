from github import Github, GithubException


class Users:
    """[summary]"""

    def __init__(self, token: str):
        """[summary]

        Args:
            token (str): [description]
        """
        self.token = token

    def auth(self):
        """[summary]"""
        try:
            gh = Github(self.token)
            return gh
        except GithubException as e:
            print(e)
            exit(2)
