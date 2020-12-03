#You have a singly lined list l, which is sorted in strictly increasing order, and an integer value. Add value to the list l, preserving its original sorting.
class ListNode(object):
    def __init__(self,value):
        self.value = value
        self.next = None
    def inserValueIntoSortedLinedList(self, l,value):
        self.l = l
        self.value = ListNode(value)
        
        new_node = ListNode(value) #Always start here
        if l is None:
            return new_node ##This is my first edge case stating if there is nothing in the list, you want to return a linked list with the new node value in it
        curr = l # This will look at each Node
        if value < curr.value: ## We are checking to see if the value is smaller than the first value (Or cur value). If so, then we will put it to the head
            new_node.next = curr ## This will make the new node's next value be the current value or the head
            return new_node
        while curr:
            if value > curr.value: #Python will look here if there line 11 is not true. 
                if curr.next !=None: ##This will check if there is a next value.
                    if value > curr.next.value: ##This will check to see if the value is greater than the next value as well, so it is traversing the list by looking at each node until it meets it condition
                        curr = curr.next # Now we are making the cur value equal to the next value, or putting it in it's correct place
                    else:
                        new_node.next = curr.next # If the value is smaller than the next value, then we will want to place it before the next value
                        curr.next = new_node ## And make the next value be the new node
                        break ##Don't forget to break your while loops!
                else: ##this is saying if there is no next value
                    curr.next = new_node
                    break
        return l

