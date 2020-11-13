# Given a Binary Search Tree (BST) and a range, count number of nodes that lie in the given range.

# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def csBSTRangeSum(root, lower, upper):
    #Base case if if the root is none
    if root is None:
        return 0
    
    ##I need to check if the current node is between the lower and upper values then count it recursively. 
    if root.value >= lower and root.value <= upper:
        return (1 + csBSTRangeSum(root.left, lower, upper) + csBSTRangeSum(root.right, lower, upper))
    ## If it is smaller than the lowest value, it will recurse for right child... or I can do if it is larger than the highest value, recurse for left child
    elif root.value > upper:
        return csBSTRangeSum(root.left, lower, upper)
    else:
        return csBSTRangeSum(root.right, lower, upper)
    

    root:
{
    "value": 10,
    "left": {
        "value": 5,
        "left": {
            "value": 3,
            "left": null,
            "right": null
        },
        "right": {
            "value": 7,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 15,
        "left": null,
        "right": {
            "value": 18,
            "left": null,
            "right": null
        }
    }
}
lower: 7
upper: 15