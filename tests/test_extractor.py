import unittest
from abyss.akasha.extractor import extract_abyss_records, extract_schedule


class TestExtractAbyssRecords(unittest.TestCase):
    """
    Test using this example parsing the response:
    """
    def test_extract_abyss_records(self):
        resp = 'static_abyss_record_dict ={"usage_list": [{"i": 73, "v": "0", "d": "77.9", "r": 1}]}'
        abyss_records = extract_abyss_records(resp)
        self.assertEqual(len(abyss_records), 1)


class TestExtractSchedule(unittest.TestCase):
    """
    Test using this example parsing the response:
    """
    def test_extract_schedule(self):
        resp = 'var static_schedule_version_dict ={"11": {"version": "1.1", "desc": "1.1", "start": " ", "end": " "}};'
        schedule = extract_schedule(resp)
        self.assertEqual(len(schedule), 1)
