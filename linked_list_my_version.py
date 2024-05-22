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

    def append(self, data): # append to the end of the list
        node = Node(data)

        # if the head is empty, set the node as the head
        if not self.head:
            self.head = node
            return
        
        # set head as current node
        current_node = self.head

        # find the last node
        while current_node.next:
            current_node = current_node.next

        # set the current last node's next as the new node
        current_node.next = node
        self._add_length()
        return
    
    def prepend(self, data): # add the node to the front
        node = Node(data)
        self._add_length()

        # set new node as the head if the head is empty
        if not self.head:
            self.head = node
            return
        node.next = self.head
        self.head = node
        return
    
    def delete_with_data(self, data):
        current_node = self.head

        # return the node if current data matches the target data
        if current_node.data == data:
            return current_node

        # if next node is not empty and next node's data not matches the target data
        while current_node.next and current_node.next.data != data:
            # it will stop if the next is None, or next data matches the target data
            current_node = current_node.next
        
        # if next is not None, which means the next data equals the target data
        if current_node.next:
            # skip the next node
            current_node.next = current_node.next.next
            self._reduce_length()
        return
    
    def find_with_data(self, data):
        current_node = self.head

        # return the node if current data matches the target data
        if current_node.data == data:
            return current_node

        # if next node is not empty and next node's data not matches the target data
        while current_node.next and current_node.next.data != data:
            current_node = current_node.next

        # if next node exist, return the next node
        if current_node.next:
            return current_node.next
        return
        
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

        

