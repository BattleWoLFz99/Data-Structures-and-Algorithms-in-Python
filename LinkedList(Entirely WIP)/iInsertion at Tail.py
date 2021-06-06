class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None
        
class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if(self.head_node is None):
            return True
        else:
            return False

    # Supplementary print function
    def print_list(self):
        if(self.is_empty()):
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True

# Inserts a value at the end of the list

def insert_at_tail(lst, value):
    # Write - Your - Code
    new_node = Node(value)

    if lst.get_head() is None:
        lst.head_node = new_node
        return

    temp = lst.get_head()
    while temp.next_element:
        temp = temp.next_element
        
    temp.next_element = new_node
    return
