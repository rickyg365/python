import random

from enum import Enum

from typing import Dict, Any

"""
Sample ID
    04_random-user_1234
    :auth_level:_:username:_:id_num:

"""
class AuthLevel(Enum):
    CREATOR = "01"
    ADMIN = "02"
    MEMBER = "03"
    GUEST = "04"


def build_user_data(id: int, username: str, auth: AuthLevel=None):
    if auth is None:
        auth = random.choice([AuthLevel.CREATOR, AuthLevel.ADMIN, AuthLevel.MEMBER, AuthLevel.GUEST])
    return {
        "auth_level": auth,
        "username": username,
        "id": id
    }

def build_user_str(user_data: Dict[str, Any]):
    reformated_username = user_data['username'].replace(" ", "-")
    return f"{user_data['auth_level'].value}_{reformated_username}_{user_data['id']}"

def parse_user_str(user_str: str):
    """ Too much going on """
    auth_level, user_name, id_num = user_str.split("_")

    def match_type(type: int):
        t = f"{type:02}"
        match t:
            case AuthLevel.CREATOR.value:
                return AuthLevel.CREATOR
            case AuthLevel.ADMIN.value:
                return AuthLevel.ADMIN
            case AuthLevel.MEMBER.value:
                return AuthLevel.MEMBER
            case AuthLevel.GUEST.value:
                return AuthLevel.GUEST

    # Correct Types
    auth_level = match_type(auth_level)      # str -> AuthLevel(Enum)
    user_name = user_name.replace("-", " ")  # str -> str
    id_num = int(id_num)                     # str -> int

    return {
        "auth_level": auth_level,
        "username": user_name,
        "id": id_num
    }

class User:
    def __init__(self, id: int, username: str, auth_level: AuthLevel=AuthLevel.GUEST):
        self.id = id
        self.username = username
        self.auth_level = auth_level 

    def __str__(self):
        txt = f"[{self.id:04}]  {self.auth_level.name.title():<7}  {self.username}"
        return txt

    def update_auth(self, new_level: AuthLevel):
        self.auth_level = new_level


