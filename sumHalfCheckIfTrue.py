#See if the first half's sum is equal to the second half of the sum
def isLucky(n):
    lucky = [int(num) for num in str(n)] #Here we are assigning to the variable lucky a list of the integers in the n(number). You need to convert the n(number) to a string so that it can be iterable, and then each num in the string n should be an int.
    l = int(len(lucky)/2) # Here we are cutting the integer in half
    return sum(lucky[:l] == sum(lucky[l:])) #Now we will return a bool that check if the sum of the integers of the first half is the same as the sum of the integers of the last half