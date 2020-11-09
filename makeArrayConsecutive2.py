# Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

#my code:
# def makeArrayConsecutive2(statues):
#     if statues is None:
#         return statues
#     min_stats = min(statues) #Takes the smallest int in statues
#     max_stats = max(statues) #Takes the largest int in statues
#     for i in range(len(statues)): ##for each index between 0 and the length of the statues array
#         if statues[i] < min_stats: ## If the statues at each index is smaller than the smallest statues
#             min_stats = statues[i] ## That must be the smallest statue
#         if statues[i] > max_stats:## If the statues at each index is larger than the largest statue,
#             max_stats = statues[i]##That one must be the largest    
#     ###a What I have figured is that I could just sort the array using the sorted() method before finding the max and min values
#     consec = max_stats - min_stats + 1 - len(statues) ## This is taking the largest value and subtracting the smallest value and adding 1, then subtracting the length of the statues.. 
#     return( consec)
##To GH

#my refacter:
def makeArrayConsecutive2(statues):
    return(max(statues) - min(statues) + 1 - len(statues))##So! This basically means I am taking the range of the statues (or how many numbers are in range of the smallest value and the largest value) and subtracting the length of the statues. This will equal how many statues are missing =) 

data = [6, 2, 3, 8] 
print(makeArrayConsecutive2(data))