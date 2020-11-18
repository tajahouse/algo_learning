# The element with single occurrence is 7
# Another approach suggested by Abhishek Sharma 44. Add each number once and multiply the sum by 3, we will get thrice the sum of each element of the array. Store it as thrice_sum. Subtract the sum of the whole array from the thrice_sum and divide the result by 2. The number we get is the required number (which appears once in the array).

# Array [] : [a, a, a, b, b, b, c, c, c, d]
# Mathematical Equation = ( 3*(a+b+c+d) – (a + a + a + b + b + b + c + c + c + d) ) / 2

# In more simple words: ( 3*(sum_of_array_without_duplicates) – (sum_of_array) ) / 2

# let arr[] = {12, 1, 12, 3, 12, 1, 1, 2, 3, 3}
# Required no = ( 3*(sum_of_array_without_duplicates) - (sum_of_array) ) / 2
#             = ( 3*(12 + 1 + 3 + 2) - (12 + 1 + 12 + 3 + 12 + 1 + 1 + 2 + 3 + 3))/2 
#             = ( 3*     18          -      50) / 2
#             = (54 - 50) / 2
#             = 2 (required answer)
# As we know that set does not contain any duplicate element,
# But, std::set is commonly implemented as a red-black binary search tree. Insertion on this data structure has a worst-case of O(log(n)) complexity, as the tree is kept balanced. we will be using set here.

# Below is the implementation of above approach:
 ##This is geeks for geeks solution:::
# def csFindTheSingleNumber(nums):
#     if nums is None:
#         return
#     return(3 * sum(set(nums)) - sum(nums)) / 2

###My solution
def csFindTheSingleNumber(nums):
    d = {} ##Creating a dictionary allow for better storage and search
    for n in nums: #Searching through each value of nums
        if n in d: #If the element is in the dictionary
            d[n] +=1 #Increment that element's value by one.. Giving a key value pair of that element and it's count (i.e {'a':1})
        else:
            d[n] = 1 #Otherwise, just add 1 to the value of the element... All elements will start like this since there is nothing in the dictionary until the element is evaluated.
    # print(d)
    for num, i in d.items(): ## This method creates a key value evaluation of the items of key:value pairs, num is the key, i is the value. The goal is to return the key in which is value is 1.
        if i == 1: #So if the value is equal to 1, 
            return(num)
    




        

