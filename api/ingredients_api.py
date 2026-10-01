import requests
from config.app_conf import API_BASE_URL


def get_ingredients_by_type(ingredient_type: str):
    resp = requests.get(f"{API_BASE_URL}/ingredients")
    resp.raise_for_status()
    all_ingredients = resp.json()["data"]
    return [item["name"] for item in all_ingredients if item["type"] == ingredient_type]
