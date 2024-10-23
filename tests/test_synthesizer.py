import unittest
from rufus.synthesizer import Synthesizer

class TestSynthesizer(unittest.TestCase):

    def setUp(self):
        """
        Set up a basic instance of the Synthesizer and some sample data to test.
        """
        self.synthesizer = Synthesizer()

        # Sample data extracted from a mock website
        self.extracted_data = {
           "https://www.sfgov.com",
        }

    def test_synthesize_to_json(self):
        """
        Test synthesizing extracted data into a structured JSON format.
        """
        expected_output = {
            "pages": [
                {
                    "url": "https://www.sfgov.com",
                    "content": "This is an example website with sample text and some information."
                },
            ]
        }
        
        synthesized_json = self.synthesizer.synthesize(self.extracted_data, format='json')
        self.assertEqual(synthesized_json, expected_output)

    def test_synthesize_to_text(self):
        """
        Test synthesizing extracted data into a plain text document.
        """
        expected_output = (
            "URL: https://www.sfgov.com\n"
            "Content: This is an example website with sample text and some information.\n\n"
        )
        
        synthesized_text = self.synthesizer.synthesize(self.extracted_data, format='text')
        self.assertEqual(synthesized_text.strip(), expected_output.strip())

    def test_invalid_format(self):
        """
        Test that an invalid format raises a ValueError.
        """
        with self.assertRaises(ValueError):
            self.synthesizer.synthesize(self.extracted_data, format='xml')

if __name__ == "__main__":
    unittest.main()
