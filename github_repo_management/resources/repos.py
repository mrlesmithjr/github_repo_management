import requests
import json
from base64 import b64encode
from nacl import encoding, public

API_URL = "https://api.github.com/repos"


class Repos:
    """[summary]"""

    def __init__(self, ctx: object):
        """[summary]

        Args:
            ctx (object): [description]
        """
        self.login = ctx.obj["user"].login
        self.user = ctx.obj["user"]
        self.token = ctx.obj["token"]
        self.url = f"{API_URL}/{self.login}"
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {self.token}",
        }

    def get_repos(self):
        """[summary]

        Returns:
            [list]: [Returns list of repos]
        """
        # We only include non forks and non org repos here
        repos = [
            repo
            for repo in self.user.get_repos()
            if not repo.fork and repo.organization is None and "ansible" in repo.name
        ]
        return repos

    def get_secrets(self):
        """[summary]

        Returns:
            [dict]: [Returns dictionary of repo secrets]
        """
        repos = self.get_repos()
        payload = {}
        repo_secrets = {}

        for repo in repos:
            url = f"{self.url}/{repo.name}/actions/secrets"
            response = requests.request("GET", url, headers=self.headers, data=payload)
            secrets = response.json()
            repo_secrets[repo.name] = secrets

        return repo_secrets

    def encrypt(self, public_key: str, secret_value: str):
        """[summary]

        Args:
            public_key (str): [description]
            secret_value (str): [description]

        Returns:
            [type]: [description]
        """
        public_key = public.PublicKey(
            public_key.encode("utf-8"), encoding.Base64Encoder()
        )
        sealed_box = public.SealedBox(public_key)
        encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))

        return b64encode(encrypted).decode("utf-8")

    def add_secrets(self):
        """[summary]"""
        # repos = self.get_repos()
        repos = ["ansible-kvm", "test-repo-settings"]
        payload = {}
        secrets = {"EXAMPLE": "EXAMPLE-2"}

        for repo in repos:
            url = f"{self.url}/{repo}/actions/secrets"
            response = requests.request(
                "GET", f"{url}/public-key", headers=self.headers, data=payload
            )
            public_key = response.json()

            for key, value in secrets.items():
                encrypted_value = self.encrypt(public_key["key"], value)
                payload = {
                    "key_id": public_key["key_id"],
                    "encrypted_value": encrypted_value,
                }
                response = requests.request(
                    "PUT",
                    f"{url}/{key}",
                    headers=self.headers,
                    data=json.dumps(payload),
                )
