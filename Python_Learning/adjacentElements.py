# Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

# Example

# For inputArray = [3, 6, -2, -5, 7, 3], the output should be
# adjacentElementsProduct(inputArray) = 21.

# 7 and 3 produce the largest product.

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] array.integer inputArray

# An array of integers containing at least two elements.

# Guaranteed constraints:
# 2 ≤ inputArray.length ≤ 10,
# -1000 ≤ inputArray[i] ≤ 1000.

# [output] integer

# The largest product of adjacent elements.




#My Solution:
def adjacentElementsProduct(inputArray):
    ##Multiply adjacent numbers and return the largest multiple
    ## mx_val = 0
    ## Determine if value in inputArray is > mx_value 
    ## We are looping through the array and determining if an element * next element is > than mx_value, if so, return that value.
    mx_val = -100
    
    for i in range(len(inputArray)-1):
        if inputArray[i] * inputArray[i+1] > mx_val:
            mx_val = inputArray[i] * inputArray[i+1]
    return mx_val
    
#Other Solution :
def adjacentElementsProduct1(inputArray):
    return max([inputArray[i] * inputArray[i+1] for i in range(len(inputArray)-1)])

arr1 = [3, 6, -2, -5, 7, 3]
arr2 = [-1, -2]
arr3 = [-23, 4, -3, 8, -12]

print("My sol",adjacentElementsProduct(arr1))
print("Other sol", adjacentElementsProduct1(arr1))
