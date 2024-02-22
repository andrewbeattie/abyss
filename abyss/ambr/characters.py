"""
Use project amber to get the character ids
"""

import requests
import regex as re
from abyss.models import Character

def find_numbers(character_id: str) -> str:
    """
    10000002-B
    regex for all digits
    """
    return re.sub("[^\d]", "", character_id)

def strip_zeros(character_id: int) -> int:
    character_id = str(find_numbers(character_id))

    character_id = str(character_id)[2:]
    character_id = character_id.lstrip("0")
    return int(character_id)

def get_character_name():
    url = "https://api.ambr.top/v2/id/avatar"
    resp = requests.get(url)
    data = []
    for key, value in resp.json()["data"]["items"].items():
        character = Character(
            id=strip_zeros(key),
            name=value["name"],
        )
        data.append(character)
    return data



bp = 0