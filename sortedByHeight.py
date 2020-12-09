# Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

# Example

# For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
# sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].


def sortByHeight(a):
    humans = sorted([x for x in a if x != -1]) #Remember, sorted will get you the list in order. Humans have been taken out withouth the trees (-1) and sorted in order
    output = [humans.pop(0) if a[x]!=-1 else -1 for x in range(0,len(a))] # The output then pops out any number that is not -1 in the index of the original array and replaces it with it's sorted value. Otherwise, it will place -1 where -1 is
    return(output)

a = [-1, 150, 190, 170, -1, -1, 160, 180]
print(sortByHeight(a))