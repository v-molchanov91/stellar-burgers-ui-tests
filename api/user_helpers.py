import uuid


def generate_unique_user():
    uniq = uuid.uuid4().hex[:8]
    return {
        "email": f"ui_{uniq}@yandex.ru",
        "password": "SecurePass123!",
        "name": f"UI User {uniq}",
    }
