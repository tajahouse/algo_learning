def allLongestStrings(inputArray):
    return [i for i in inputArray if len(i) == len(max(inputArray, key=len))]

inputArray = ["aba", 
 "aa", 
 "ad", 
 "vcd", 
 "aba"]
print(allLongestStrings(inputArray))