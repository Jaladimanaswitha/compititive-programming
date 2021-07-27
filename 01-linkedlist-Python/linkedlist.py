"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        # Your code goes here
        if self.head is None:
            self.head=new_element
        else:
            n=self.head
            while(n.next is not None):
                n=n.next
            n.next=new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # Your code goes here
        n=self.head
        m=0
        while(n is not None):
            m+=1
            if(m==position):
                return n
            n=n.next
       
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # Your code goes here
        n=self.head
        m=0
        while(n is not None):
            m+=1
            if(m==position):
                break
            p=n
            n=n.next
        if n is not None:
            print(n.value,'in')
            p.next=new_element
            new_element.next=n
        
    
    def delete(self, value):
        """Delete the first node with a given value."""
        # Your code goes here
        if self.head.value ==value:
            self.head=self.head.next
            return
        else:
            n=self.head
            while(n.next is not None):
                if(n.next.value==value):
                    break
                n=n.next
            if n.next is not None:
                n.next=n.next.next

# e1 = Element(1)
# e2 = Element(2)
# e3 = Element(3)

# ll = LinkedList(e1)
# ll.append(e2)
# ll.append(e3)
# e4 = Element(4)
# ll.insert(e4,3)
# ll.fun()
