# test_walletforge.py
"""
Tests for WalletForge module.
"""

import unittest
from walletforge import WalletForge

class TestWalletForge(unittest.TestCase):
    """Test cases for WalletForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WalletForge()
        self.assertIsInstance(instance, WalletForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WalletForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
