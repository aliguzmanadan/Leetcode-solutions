class Node():
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None


#Class list
class DLikedList():
    """Double linked list"""

    #Class Constructor
    def __init__(self):
        self.head = None
        self.tail = None

    #Insert element at tail
    def insertAtTail(self, node):
        if (self.head == None) and (self.tail == None):
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node

    #Remove a node
    def remove(self, node):
        prev = node.prev
        next = node.next

        #Checking if we are removing the head
        if prev:
            prev.next = next
        else:
            self.head = next

        #Checking if we are removing the tail
        if next:
            next.prev = prev
        else:
            self.tail = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.list = DLikedList()
        

    def get(self, key: int) -> int:
        if key in self.dict:
            self.list.remove(self.dict[key])
            self.list.insertAtTail(self.dict[key])
            return self.dict[key].value
        else: 
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.list.remove(self.dict[key])
            
        new_node = Node(key, value)
        self.list.insertAtTail(new_node)
        self.dict[key] = new_node
            
        if len(self.dict) > self.capacity:
            self.dict.pop(self.list.head.key)
            self.list.remove(self.list.head)
            
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)