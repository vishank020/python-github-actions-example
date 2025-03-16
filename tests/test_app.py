import sys
import os
import unittest

# Add 'src' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from src.app import index  # Import the function

class TestApp(unittest.TestCase):
    def test_index(self):
        expected_output = "Hello, world! This is a Flask app running with CI/CD."
        self.assertEqual(index(), expected_output)  # ✅ No more 'assert', uses unittest

if __name__ == "__main__":
    unittest.main()