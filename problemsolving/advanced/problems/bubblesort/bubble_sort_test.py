import unittest
import insertion_sort_problem as st

class Test_TestValue(unittest.TestCase):
    def test_simple(self):
        testList = [4,3,2,1]
        expectedList = testList.copy()
        expectedList.sort()
        actualList=st.bubblesort(testList)
        self.assertEqual(actualList,expectedList)

    def test_empty(self):
        testList=[]
        expectedList = testList.copy()
        expectedList.sort()
        actualList=st.bubblesort(testList)
        self.assertEqual(actualList,expectedList)