import requests
from config import ConfigHandler


class ApiHandler:
    def __init__(self):
        self.config_handler = ConfigHandler()
        self.base_url = self.config_handler.get_option(
            "api", "base_url", "http://localhost:8000"
        )

    def signup(self, email: str, username: str, password: str) -> str:
        """Register new user api.

        Args:
            email (str): user email.
            username (str): user username.
            password (str): user password.

        Returns:
            str: JWT access token.
        """
        url = f"{self.base_url}/api/v1/users/register"
        body = {"email": email, "username": username, "password": password}
        r = requests.post(url, json=body)
        if r.status_code == 201:
            return r.json()["access"]

    def create_post(self, title: str, content: str, access_token: str) -> int:
        """Create post api.

        Args:
            title (str): post title.
            content (str): post content.
            access_token (str): user access token.

        Returns:
            int: created post ID.
        """
        url = f"{self.base_url}/api/v1/posts/"
        body = {"title": title, "content": content}
        r = requests.post(
            url, json=body, headers={"Authorization": f"Bearer {access_token}"}
        )
        if r.status_code == 201:
            return r.json()["id"]

    def like_post(self, post_id: int, access_token: str):
        """Set like to post api.

        Args:
            post_id (int): post id.
            access_token (str): user access token.
        """
        url = f"{self.base_url}/api/v1/posts/{post_id}/like"
        requests.post(url, headers={"Authorization": f"Bearer {access_token}"})
