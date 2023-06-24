# no we can't reverse a linkedlist in less than O(n) complextity

class list_node:
    def __init__(self,data=0,next=None):
        self.data=data
        self.next=next
    
def reverse_list(head):
    if not head or not head.next:
        return head
    
    prev_node = None
    current_node= head
    next_node= None
    
    while current_node:
        next_node=current_node.next
        current_node.next = prev_node
        prev_node=current_node
        current_node=next_node
    
    return prev_node

head = list_node(1)
node2 = list_node(2)
node3 = list_node(3)
node4 = list_node(4)
node5 = list_node(5)
node6 = list_node(6)

head.next = node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=node6

reverse_head=reverse_list(head)

while reverse_head:
    print(reverse_head.data,end=" ")
    reverse_head = reverse_head.next

        
    
    