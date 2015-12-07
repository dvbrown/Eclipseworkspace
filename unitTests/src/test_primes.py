# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 18:23:15 2015

@author: DanBrown
"""

import unittest
from primes import is_prime

class PrimesTestCast(unittest.TestCase):
    """Tests for `primes.py`."""
    
    def test_is_five_prime(self):
        self.assertTrue(is_prime(5))
        
if __name__ == '__main__':
    unittest.main()