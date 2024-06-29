class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return 
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = node

    def prepend(self, data):
        node = Node(data)
        if not self.head:
            self.head = node 
            return
        node.next = self.head
        self.head = node

    def delete_with_data(self, data):
        if not self.head:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current_node = self.head
        while current_node.next and current_node.next.data != data:
            current_node = current_node.next

        if current_node.next:
            current_node.next = current_node.next.next

    def find_with_data(self, data):
        current_node = self.head
        while current_node and current_node.data != data:
            current_node = current_node.next
        return current_node
    
    def display(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next
        print("-->".join(elements))


ll = LinkedList()
ll.append("data1")
ll.append("data2")
ll.append("data3")
ll.append("data4")
ll.append("data5")

ll.delete_with_data("data3")

ll.display()
        

    