import unittest
from paymentgrid.action_codes.visa import VisaActionCodes

class TestVisaActionCodes(unittest.TestCase):
    def test_known_action_code(self):
        visa_codes = VisaActionCodes()
        self.assertEqual(visa_codes.get_action_description("00"), "Approved for Visa-specific process")
    
    def test_standard_fallback(self):
        visa_codes = VisaActionCodes()
        self.assertEqual(visa_codes.get_action_description("05"), "Do not honor")

if __name__ == '__main__':
    unittest.main()
