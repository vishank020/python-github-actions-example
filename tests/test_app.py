import sys
import os

# Add 'src' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from src.app import index  # Import the function

def test_index():
    assert index() == "Hello, world! This is a Flask app running with CI/CD."