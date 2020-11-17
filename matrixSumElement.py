# After becoming famous, the CodeBots decided to move into a new building together. Each of the rooms has a different cost, and some of them are free, but there's a rumour that all the free rooms are haunted! Since the CodeBots are quite superstitious, they refuse to stay in any of the free rooms, or any of the rooms below any of the free rooms.

# Given matrix, a rectangular matrix of integers, where each value represents the cost of the room, your task is to return the total sum of all rooms that are suitable for the CodeBots (ie: add up all the values that don't appear below a 0).

def matrixElementsSum(matrix):
    if matrix is None:
        return
    # I will need to have a base case of if there is matrix is None, return 0

    # I will need to check how many elements are in each array of the matrices... Or count how many elements are in the matrices collectively, and the we can subtract how many are equal to 0.

    ## In this case, I will need to iterate over all of the matricies. 
    ## I COULD create a place to append the rooms that are not 0 and then find the lenght of that appended item

    ## We are also asked to add up all the values that don't appear below 0... well, we can add up all the values and it will technically still add up correctly lol 
    ##Re-eval. When they say anything that appears below 0, they mean literally below the value of 0 in the matrix... So if it is in the same index but after it or "under" it, then don't return it. 
    rooms = len(matrix)
    floors= len(matrix[0])
    total=0
    for floor in range(floors):
        for room in range(rooms):
            if matrix[room][floor]!=0:
                total+=matrix[room][floor]
            else:
                break
    return total
                
matrix = [[0,1,1,2], 
 [0,5,0,0], 
 [2,0,3,3]]

print(matrixElementsSum(matrix))