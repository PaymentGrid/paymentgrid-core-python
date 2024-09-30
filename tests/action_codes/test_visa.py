import unittest
from paymentgrid.action_codes.visa import VisaActionCodes

class TestVisaActionCodes(unittest.TestCase):
    def test_known_action_code(self):
        visa_codes = VisaActionCodes()
        self.assertEqual(visa_codes.get_action_description("00"), "Approved and completed successfully")
    
    def test_standard_fallback(self):
        visa_codes = VisaActionCodes()
        self.assertEqual(visa_codes.get_action_description("05"), "Do not honor")

    def test_standard_action_code(self):
        visa_codes = VisaActionCodes()
        self.assertEqual(visa_codes.get_action_description("87"), "Reserved for private use")
    
    def test_alpha_numaric_action_code(self):
        visa_codes = VisaActionCodes()
        self.assertEqual(visa_codes.get_action_description("N7"), "Decline for CVV2 failure")
    
    def test_visa_specific_action_code(self):
        visa_codes = VisaActionCodes()
        self.assertEqual(visa_codes.get_action_description("81"), "Cryptographic error found in PIN")
    
    def test_get_all_codes_count(self):
        # Initialize VisaActionCodes
        visa_codes = VisaActionCodes()

        # Get all combined action codes
        all_codes = visa_codes.get_all_codes()

        # Get the count of standard codes and Visa-specific codes
        standard_codes_count = len(visa_codes.get_all_standard_codes())
        visa_specific_codes_count = len(visa_codes.visa_specific_codes)

        # Calculate the expected count of combined codes
        # Subtract overlapping keys
        overlapping_keys_count = len(set(visa_codes.visa_specific_codes) & set(visa_codes.get_all_standard_codes()))
        expected_count = standard_codes_count + visa_specific_codes_count - overlapping_keys_count

        # Assert that the number of combined codes matches the expected count
        self.assertEqual(len(all_codes), expected_count)


if __name__ == '__main__':
    unittest.main()
