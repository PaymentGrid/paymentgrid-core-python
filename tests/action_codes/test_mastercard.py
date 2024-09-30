# tests/test_mastercard.py

import unittest
from paymentgrid.action_codes.mastercard import MastercardActionCodes

class TestMastercardActionCodes(unittest.TestCase):
    def test_known_action_code(self):
        mastercard_codes = MastercardActionCodes()
        self.assertEqual(mastercard_codes.get_action_description("51"), "Not sufficient funds")
    
    def test_standard_fallback(self):
        mastercard_codes = MastercardActionCodes()
        self.assertEqual(mastercard_codes.get_action_description("05"), "Do not honor")

if __name__ == '__main__':
    unittest.main()
