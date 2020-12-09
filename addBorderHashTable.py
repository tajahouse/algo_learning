#Given a rectangular matrix of character, add a border of asterisks (*) to it.

#For example: 
# For

# picture = ["abc",
#            "ded"]
# the output should be

# addBorder(picture) = ["*****",
#                       "*abc*",
#                       "*ded*",
#                       "*****"]

def addBorder(picture):
    picture = list(map(lambda x: "*" + x + "*", picture))
    picture.insert(0, "*", len(picture[0]))
    picture.append("*" * len(picture[0]))
    return picture