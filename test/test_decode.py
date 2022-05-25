from decode import *
import unittest

class testDecode(unittest.TestCase):

    def test_decode_string(self):
        string_to_decode = 'SGVsbG8sIFdvcmxkIQ=='
        expected_result = b'Hello, World!'

        decoded_string = decode_string(string_to_decode)

        self.assertAlmostEqual(decoded_string, expected_result)


    def test_decode_json(self):
        json_to_decode = 'eyJoZWxsbyI6ICJ3b3JsZCJ9'
        expected_result = json.dumps({"hello": "world"}, indent=4, sort_keys=True).encode()

        decoded_json = decode_json(json_to_decode)

        self.assertEqual(decoded_json, expected_result)


    def test_get_sqs_data_field(self):
        string_to_decode = '''{"id":"sampleId","data":"ewogICAgImRhdGEiOiB7CiAgICAgICAgImRhdGFJZCI6IDEyMzQxMjM0LAogICAgICAgICJhbW91bnQiOiAiMTIzNC41NiIsCiAgICAgICAgImN1cnJlbmN5IjogIlVTRCIKICAgIH0sCiAgICAiYWRkaXRpb25hbEluZm8iOiAxMjM0Cn0="}'''
        expected_data_field = "ewogICAgImRhdGEiOiB7CiAgICAgICAgImRhdGFJZCI6IDEyMzQxMjM0LAogICAgICAgICJhbW91bnQiOiAiMTIzNC41NiIsCiAgICAgICAgImN1cnJlbmN5IjogIlVTRCIKICAgIH0sCiAgICAiYWRkaXRpb25hbEluZm8iOiAxMjM0Cn0="

        actual_data_field = get_data_field_from_sqs_json(string_to_decode)

        self.assertEqual(actual_data_field, expected_data_field)


    def test_decode_sqs_message(self):
        string_to_decode = '''{"id":"sampleId","data":"ewogICAgImRhdGEiOiB7CiAgICAgICAgImRhdGFJZCI6IDEyMzQxMjM0LAogICAgICAgICJhbW91bnQiOiAiMTIzNC41NiIsCiAgICAgICAgImN1cnJlbmN5IjogIlVTRCIKICAgIH0sCiAgICAiYWRkaXRpb25hbEluZm8iOiAxMjM0Cn0="}'''
        expected_result = json.dumps({"data": {"dataId": 12341234, "amount": "1234.56", "currency": "USD"}, "additionalInfo": 1234}, indent=4, sort_keys=True).encode()

        data_field = get_data_field_from_sqs_json(string_to_decode)
        actual_result = decode_json(data_field)

        self.assertEqual(actual_result, expected_result)