class Node:
    def __init__(self, x):
        self.value = x
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node
    
def insert_at_tail(lst, value):
    new_node = Node(value)
    if lst.get_head() is None:
        lst.head_node = new_node
        return
    temp = lst.get_head()
    while temp.next:
        temp = temp.next
    temp.next = new_node
    return 

def mergeTwoLinkedLists(l1,l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    new_list = Node(0)
    temp = new_list
    while l1  != None and l2 != None:
        if l1.value <= l2.value:
            new_list.next = l1
            l1 = l1.next
        else:
            new_list.next = l2
            l2 = l2.next
        new_list = new_list.next
    if l1 is None:
        new_list.next = l2
    if l2 is None:
        new_list.next = l1
    return temp.next
l1 = LinkedList()
insert_at_tail(l1, 1)
insert_at_tail(l1, 2)
insert_at_tail(l1, 3)
l2 = LinkedList()
insert_at_tail(l2, 4)
insert_at_tail(l2, 5)
insert_at_tail(l2, 6)
# l1 = [1,2,3]
# l2 = [4,5,6]
print(mergeTwoLinkedLists(l1.head_node,l2.head_node))