class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def _add_length(self):
        self.length += 1

    def _reduce_length(self):
        self.length -= 1

    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = node
        self._add_length()
        return
    
    def prepend(self, data):
        node = Node(data)
        self._add_length()
        if not self.head:
            self.head = node
            return
        node.next = self.head
        self.head = node
        return
    
    def delete_with_data(self, data):
        current_node = self.head

        if current_node.data == data:
            return current_node

        while current_node.next and current_node.next.data != data:
            current_node = current_node.next
        
        if current_node.next:
            current_node.next = current_node.next.next
            self._reduce_length()
        return
    
    def find_with_data(self, data):
        current_node = self.head

        if current_node.data == data:
            return current_node

        while current_node.next and current_node.next.data != data:
            current_node = current_node.next

        if current_node.next:
            return current_node.next
        
    def display(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next
        print("-->".join(elements))

    def get_length(self):
        return self.length
    
ll = LinkedList()
ll.append("data1")
ll.append("data2")
ll.append("data3")
ll.append("data4")
ll.append("data5")


ll.delete_with_data("data3")
ll.append("data6")

ll.display()

print(ll.find_with_data("data4"))

        

