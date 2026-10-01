import requests
from config.app_conf import API_BASE_URL


class UserAPI:
    @staticmethod
    def register(user):
        resp = requests.post(f"{API_BASE_URL}/auth/register", json=user)
        resp.raise_for_status()

    @staticmethod
    def delete(user):
        login_resp = requests.post(
            f"{API_BASE_URL}/auth/login",
            json={"email": user["email"], "password": user["password"]},
        )
        if login_resp.status_code == 200:
            token = login_resp.json()["accessToken"].split(" ")[1]
            requests.delete(
                f"{API_BASE_URL}/auth/user",
                headers={"Authorization": f"Bearer {token}"},
            )
