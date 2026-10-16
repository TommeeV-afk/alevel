class Node:
    def __init__(self, data):
        self.data = data
        self.pointer = None

head = Node(0)
current_node = head

for i in range(1,5):
    new_node = Node(i*2)
    current_node.pointer = new_node
    current_node = new_node

def show_list(head):
    x = head
    while x != None:
        print(x.data)
        x = x.pointer
##print(head.data, head.pointer)
#print(head.pointer.data)

def insert_inorder_list(head,new_data):
    new_node = Node()
    new_node.data = new_data

    if head is None or new_data < head.data:
        new_node.pointer = head
        return new_node
    current_node = head

    while current_node.pointer is not None and current_node.pointer < new_data:
        current_node = current_node.pointer

show_list(head)