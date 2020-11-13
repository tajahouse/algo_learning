# Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

def almostIncreasingSequence(sequence):
    droppped = False ## make the values drop or remove an element if the element iis less than the last.
    last = prev = min(sequence) - 1 # note: we are creating placeholders for the last and the previous sequence while iterating. We are taking the smallest sequence and subtracting 1 so nothing can be less than or equal to the last and previous.
    for elm in sequence:
        if elm <= last: # note: Checking if the element is less than or equal to the last element.. Which it shouldn't be in the first pass since atm, the last element is 1 less than the smallest element
            if droppped: # If the element has already been dropped, it will automatically return false, meaning it didn't go in sequencial increasing order because that number has been visited
                return False
            else:
                droppped = True #If the element was smaller than the last element, you will want to drop it then move to the next element. This should only happen once.
            if elm <= prev: # Here, you will take the element and check if it is smaller than the previous element. If so, you will switch the bigger element (prev) with the last element. It will need to be at the end so it can increase
                prev = last
            elif elm >= prev: # If the element is larger than the previous on the other hand, you will want to move the element to the end, and make the previous be the front, and the last element will now go in between teh prev and the element. So, elm = last
                prev = last = elm
        else:
            prev, last = last, elm #In response to line 6, if the element is not less than or equal to the last element, you will want to switch the elements in the same manner as line 15
    return True ## When the sequence has reached its end, it will return true because it never revisited a dropped element in the sequence


sequence = [1, 3, 2, 1]

print(almostIncreasingSequence(sequence))