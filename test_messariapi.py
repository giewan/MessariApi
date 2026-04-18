# test_messariapi.py
"""
Tests for MessariApi module.
"""

import unittest
from messariapi import MessariApi

class TestMessariApi(unittest.TestCase):
    """Test cases for MessariApi class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MessariApi()
        self.assertIsInstance(instance, MessariApi)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MessariApi()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
