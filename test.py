import unittest

from RMS_TC_test import find_product_horizontal, find_product_vertical, find_product_diagonal_right, find_product_diagonal_left, find_product

class TestHorizontalProducts(unittest.TestCase):
    def test_horizontal_product_single(self):
        '''
        Test that the correct product is calculated for a horizontal line
        '''

        data = [1,2,3]
        length = 3
        firstIndex = 0
        result = find_product_horizontal(data,firstIndex,length)
        self.assertEqual(result, 6)

    def test_horizontal_product_none(self):
        '''
        Test that a value of 'None' is returned if the horizontal line is of length 2 but number of required adjacent numbers is 3
        '''

        data = [1,2]
        length = 3
        firstIndex = 0
        result = find_product_horizontal(data,firstIndex,length)
        self.assertEqual(result, None)

    def test_horizontal_product_with_loop(self):
        '''
        Test that it can return multiple correct products for a horizontal line
        '''

        data = [1,2,3,4,5]
        length = 3
        results = []
        for i in range(len(data)):
            results.append(find_product_horizontal(data, i, length))
        
        self.assertEqual(results, [6, 24, 60, None, None])

class TestVerticalProducts(unittest.TestCase):
    
    def test_vertical_product_single(self):
        '''
        Test that it can return correct product for a vertical line in grid
        '''

        data = [[1,2],
                [2,3]]
        length = 2
        result = find_product_vertical(data, 0, 0 ,length)

        self.assertEqual(result, 2)

    def test_vertical_product_none(self):
        '''
        Test that a value of 'None' is returned if the vertical line is of length 2 but number of required adjacent numbers is 3
        '''

        data = [[1,2],
                [2,3]]
        length = 3
        result = find_product_vertical(data, 0, 0 ,length)

        self.assertEqual(result, None)

    def test_vertical_product_with_loop(self):
        '''
        Test that it can return multiple correct products for vertical lines in a grid
        '''
        data = [[1,2,3],
                [2,3,4],
                [3,4,5],
                [2,1,1]]
        length = 3  
        results = []

        for i in range(len(data)):
            for j in range(len(data[i])):
                results.append(find_product_vertical(data, i, j ,length))

        self.assertEqual(results, [6, 24, 60, 12,  12, 20, None, None,None,None, None,None])

class TestDiagonalRightProducts(unittest.TestCase):

    def test_diagonal_right_product_single(self):
        '''
        Test that it can return correct product for a diagonal line to the right, in a grid
        '''

        data = [[1,2],
                [2,3]]
        length = 2
        result = find_product_diagonal_right(data, 0, 0 ,length)
        self.assertEqual(result, 3)

    def test_diagonal_right_product_loop(self):
        '''
        Test that it can return multiple correct products for diagonal lines to the right, in a grid
        '''
        data = [[1,2,3],
                [2,3,4],
                [3,4,5],
                [2,1,1]]
        length = 2
        results = []

        for i in range(len(data)):
            for j in range(len(data[i])):
                results.append(find_product_diagonal_right(data, i, j ,length))

        self.assertEqual(results, [3, 8, None, 8, 15, None, 3, 4,None,None, None, None])

class TestDiagonalLeftProducts(unittest.TestCase):

    def test_diagonal_left_product_single(self):
        '''
        Test that it can return correct product for a diagonal line to the left, in a grid
        '''

        data = [[1,2],
                [2,3]]
        length = 2
        result = find_product_diagonal_left(data, 0, 1 ,length)
        self.assertEqual(result, 4)

    def test_diagonal_left_product_loop(self):
        '''
        Test that it can return multiple correct products for diagonal lines to the left, in a grid
        '''
        data = [[1,2,3],
                [2,3,4],
                [3,4,5],
                [2,1,1]]
        length = 2
        results = []

        for i in range(len(data)):
            for j in range(len(data[i])):
                results.append(find_product_diagonal_left(data, i, j ,length))

        self.assertEqual(results, [None, 4, 9, None, 9, 16, None, 8, 5, None, None, None])

class TestProducts(unittest.TestCase):

    def test_find_product_small_length_one(self):
        '''
        Test that it can find the largest product for small grid where number of adjacent numbers should be 1
        '''
        data = [[1,2],
                [2,3]]
        length = 1

        result = find_product(data,length)

        self.assertEqual(result, 3)


    def test_find_product_small(self):
        '''
        Test that it can find the largest product for small grid
        '''
        data = [[1,2],
                [2,3]]
        length = 2

        result = find_product(data,length)

        self.assertEqual(result, 6)

    def test_find_product_medium(self):
        '''
        Test that it can find the largest product for medium grid
        '''
        data = [[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6],
                [4, 5, 6, 7]]

        length = 3

        result = find_product(data,length)

        self.assertEqual(result, 210)

    def test_find_product_large(self):
        '''
        Test that it can find the largest product for large grid
        '''
        data = [[8, 2, 22, 97, 38, 15, 0, 40, 0, 75],
                [49, 49, 99, 40, 17, 81, 18, 57, 60, 87],
                [81, 49, 31, 73, 55, 79, 14, 29, 93, 71],
                [52, 70, 95, 23, 4, 60, 11, 42, 69, 24],
                [22, 31, 16, 71, 51, 67, 63, 89, 41, 92],
                [24, 47, 32, 60, 99, 3, 45, 2, 44, 75],
                [32, 98, 81, 28, 64, 23, 67, 10, 26, 38],
                [67, 26, 20, 68, 2, 62, 12, 20, 95, 63],
                [24, 55, 58, 5, 66, 73, 99, 26, 97, 17],
                [21, 36, 23, 9, 75, 0, 76, 44, 20, 45]]

        length = 3

        result = find_product(data,length)

        self.assertEqual(result, 667755)
    
    def test_handle_impossible_length_for_adjacent_cells(self):
        '''
        Test that a message is returned when length for adjacent cells is to long
        '''
        data = [[1,2],
                [2,3]]
        length = 3

        result = find_product(data,length)

        self.assertEqual(result, 'Not possible to calculate product from 3 adjacent cells')

if __name__ == '__main__':
    unittest.main()
