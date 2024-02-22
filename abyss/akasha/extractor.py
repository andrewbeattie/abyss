import json
import regex as re


def extract_schedule(text: str) -> str:
    """
    Extracts the static schedule from a text. Between "static_schedule_version_dict = and ;
    """
    pattern = r"static_schedule_version_dict =(.*);"
    match = re.search(pattern, text)
    if match:
        return json.loads(match.group(1))
    else:
        return None
    
def extract_abyss_records(text: str) -> str:
    """
    Extracts the static abyss record dict from a text. Between "static_abyss_record_dict = and ;
    """
    pattern = r"static_abyss_record_dict =(.*)"
    match = re.search(pattern, text)
    if match:
        return json.loads(match.group(1))
    else:
        return None
