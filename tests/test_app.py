import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app import index  # ✅ Move import to the top

def test_index():
    assert index() == "Hello, world! This is a Flask app running with CI/CD."