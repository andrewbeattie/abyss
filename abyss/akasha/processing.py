import json
import requests
from abyss.akasha.extractor import extract_abyss_records, extract_schedule


url = "https://akashadata.feixiaoqiu.com/static/data/abyss_record_list.js"

response = requests.get(url)
text = response.text

class Parser:
    def __init__(self, text):
        self.text = text
        self.schedule = None
        self.abyss_records = None

    def parse(self):
        self.schedule = extract_schedule(self.text)
        self.abyss_records = extract_abyss_records(self.text)

parser = Parser(text)
parser.parse()

from abyss.models import CharacterAppearance, CharacterFullStar, CharacterUsage

parser.abyss_records['usage_list']
mapper = {
    "i":"character_id",
    "v":"version_id",
    "d":"rate",
    "r": "rank"
}

def remap_dict(d, mapper):
    return {mapper[k]: v for k, v in d.items()}

character_by_usage = []
for record in parser.abyss_records['usage_list']:
    record = remap_dict(record, mapper)
    character_by_usage.append(CharacterUsage(**record))

import pandas as pd
data = pd.DataFrame(character_by_usage)
data.to_csv(r"./data/character_usage.csv", index=False)
bp = 0