class ListNode:
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:

    def __init__(self):
        self.size = 10000
        self.buckets = [ListNode() for i in range(self.size)]

    def hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        hashed_key = self.hash(key)
        node = self.buckets[hashed_key]  
        while node:
            if node.key == key:
                node.val = value
                return
            if node.next:
                node = node.next
            else:
                break
        node.next = ListNode(key, value)

    def get(self, key: int) -> int:
        hashed_key = self.hash(key)
        node = self.buckets[hashed_key]
        while node:
            if node.key == key:
                return node.val
            node = node.next
            
        return -1

    def remove(self, key: int) -> None:
        hashed_key = self.hash(key)
        node = self.buckets[hashed_key]
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next

                
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)