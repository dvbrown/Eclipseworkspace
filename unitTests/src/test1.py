import unittest

# Here is out 'unit'
def IsOdd(n):
    return n % 2 == 1
    
# Make my test
def square(x):
        if x != 0:
            z = x * x
        elif x == 0:
            z = "you can't square 0 you dummy"
            print z
        else:
            pass
        return z
    
# here are the unit tests
class IsOddTests(unittest.TestCase):
    
    def testOne(self):
        self.failUnless(IsOdd(1))
        
    def testTwo(self):
        self.failIf(IsOdd(2))
        
class testSquare(unittest.TestCase):
    
    def testTwo(self):
        self.failUnlessEqual(square(3),9)
        
    def testThreee(self):
        self.assertAlmostEqual(square(1), 1)
        
    def tryZero(self):
        self.assertEqual(square(0),"you ")
        
def main():
    unittest.main()
    
if __name__ == '__main__':
    main()