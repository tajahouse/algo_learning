class ListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None
def reverseNodesInKGroups(l,k):
    #First I want to keep track of a current node
    curr = l

    # move k nodes across and check if the list is long enough to do so
    # Iterate over a range of k
    #If there is nothing left or if it is not long enough, or we run out of nodes, then return l
    # increment the current node pointer 
    for _ in range(k):
        if not curr:
            return l
        curr = curr.next

    #Set a reversal ref to l - This is the first starting point
    #Set current to l.next - This is the next starting point
    rev_val, curr = l, l.next
    
    #Swap the next k elements
    #iterate to k - 1
    #Take current next and set it to reversal
    for _ in range(k-1):
        curr.next, curr, rev_val = rev_val, curr.next, curr
    l.next = reverseNodesInKGroups(curr, k)
    return rev_val
    #Set current to current next

l = [1,2,3,4,5]
k = 2
print(reverseNodesInKGroups(l, k))