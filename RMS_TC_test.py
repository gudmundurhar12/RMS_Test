
'''
    Function finds product of 'length' number of adjacent numers in a horizonal line 
'''
def find_product_horizontal(horizontalLine, firstIndex, length):
    
    if (firstIndex + length) > len(horizontalLine):
        return None

    else:
        
        product = 1
        string = ""

        for i in range(length):
            #string += str(horizontalLine[firstIndex + i]) + " "
            product *= horizontalLine[firstIndex + i] 

        #print(string)   
        return product

'''
    Function finds product of 'length' number of adjacent numers in a vertical line 
'''
def find_product_vertical(grid, firstVerticalIndex, horizontalIndex, length):

    if (firstVerticalIndex + length) > len(grid):
        return None

    else:
        product = 1
        string = ""

        for i in range(length):
            #string += str(grid[firstVerticalIndex + i][horizontalIndex]) + " "
            product *= grid[firstVerticalIndex + i][horizontalIndex]

        #print(string)
        return product 

'''
    Function finds product of 'length' number of adjacent numers in a diagonal line, like so (marked as 'x'):

    x o o
    o x o
    o o x

'''
def find_product_diagonal_right(grid, firstVerticalIndex, horizontalIndex, length):
    
    if ((firstVerticalIndex + length) > len(grid)) or ((horizontalIndex + length) > len(grid[firstVerticalIndex])):
        return None

    else:
        product = 1
        string = ""

        for i in range(length):
            #string += str(grid[firstVerticalIndex + i][horizontalIndex + i]) + " "
            product *= grid[firstVerticalIndex + i][horizontalIndex + i]

        #print(string)
        return product 

'''
    Function finds product of 'length' number of adjacent numers in a diagonal line, like so (marked as 'x'):

    o o x
    o x o
    x o o

'''
def find_product_diagonal_left(grid, firstVerticalIndex, horizontalIndex, length):
    
    if ((firstVerticalIndex + length) > len(grid)) or ((horizontalIndex - (length-1)) < 0):
        return None

    else:
        product = 1
        string = ""

        for i in range(length):
            #string += str(grid[firstVerticalIndex + i][horizontalIndex - i]) + " "
            product *= grid[firstVerticalIndex + i][horizontalIndex - i]

        #print(string)
        return product 


'''
    Finds the greatest product of 'length' adjacent numbers in the same direction in a grid
'''
def find_product(grid, length):

    if length < 1:
        return 'length should be greater than 0'
    
    products = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            
            horizontal = find_product_horizontal(grid[i],j,length)
            if horizontal:
                products.append(horizontal)
            
            vertical = find_product_vertical(grid, i, j,length)
            if vertical:
                products.append(vertical)

            diagonal_right = find_product_diagonal_right(grid, i, j, length)
            if diagonal_right:
                products.append(diagonal_right)

            diagonal_left = find_product_diagonal_left(grid, i, j, length)
            if diagonal_left:
                products.append(diagonal_left)
    
    #print(products)
    
    if len(products) > 0:
        return max(products)
    
    else:
        return 'Not possible to calculate product from ' + str(length) + ' adjacent cells'





