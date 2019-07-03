from CashTable import addCash,CheckCash
import unittest
import time

class CT_Test(unittest.TestCase):
    def testAddingCash(self):
        addCash("omar",2)
        self.assertEqual(CheckCash("omar"),"item  exist ")
    def testNotExpiredCash(self):
        addCash("ahmed",2)
        time.sleep(1)
        self.assertEqual(CheckCash("ahmed"),"item  exist ")
    def testExpiredCash(self):
        addCash("hamada",5);
        time.sleep(5.001)
        self.assertEqual(CheckCash("hamada"),"item expired")
    def testNotExistCash(self):
        self.assertEqual(CheckCash("hhhhhhh"), "item not exist")

if __name__ == '__main__':
    unittest.main()