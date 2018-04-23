import unittest
import Robert_Reneker_solve

#use: 'python -m unittest -v test_cases' in commandline to run test cases

class TestCases(unittest.TestCase):
    def test_test1(self):
        queries = ((0,0),(4,3))
        grid = list()
        grid.append([1,0,0,1,0])
        grid.append([1,1,1,0,1])
        grid.append([1,0,0,1,0])
        grid.append([1,0,0,0,1])
        grid.append([1,1,1,1,0])

        result = Robert_Reneker_solve.path_exists(grid,queries)

        self.assertEqual(list([True]),result)
    
    def test_test2(self):
        queries = ((0,0),(3,4))
        grid = list()
        grid.append([1,0,0,1,0])
        grid.append([1,1,1,0,1])
        grid.append([1,0,0,1,0])
        grid.append([1,0,0,0,1])
        grid.append([1,1,1,1,0])

        result = Robert_Reneker_solve.path_exists(grid,queries)

        self.assertEqual(list([False]),result)

    def test_test3(self):
        queries = ((0,5),(17,19),(0,0),(19,3))
        grid = list()
        grid.append([1,0,0,1,0,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1])
        grid.append([1,1,1,0,1,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1])
        grid.append([1,0,0,1,0,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1])
        grid.append([1,0,0,0,1,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1])
        grid.append([1,1,1,1,0,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1])
        grid.append([1,0,0,1,0,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1])
        grid.append([1,1,1,0,1,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1])
        grid.append([1,0,0,1,0,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1])
        grid.append([1,0,0,0,1,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1])
        grid.append([1,1,1,1,0,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1])
        grid.append([1,0,0,1,0,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1])
        grid.append([1,1,1,0,1,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1])
        grid.append([1,0,0,1,0,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1])
        grid.append([1,0,0,0,1,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1])
        grid.append([1,1,1,1,0,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1])
        grid.append([1,0,0,1,0,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1])
        grid.append([1,1,1,0,1,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1])
        grid.append([1,0,0,1,0,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1])
        grid.append([1,0,0,0,1,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1])
        grid.append([1,1,1,1,0,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1])

        result = Robert_Reneker_solve.path_exists(grid,queries)

        self.assertEqual(list([False,True]),result)

    def test_test4(self):
        queries = ((0,5),(17,19),(0,0),(19,3),(0,0),(95,82))
        grid = list()
        for i in range(0,100):
            grid.append([1]*100)
        result = Robert_Reneker_solve.path_exists(grid,queries)
        self.assertEqual(list([True,True,True]),result)

