class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        # Dummy head and tail to avoid edge cases
        self.head = Node()  # LRU comes after head
        self.tail = Node()  # MRU is before tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_tail(self, node: Node):
        # Insert node before dummy tail
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def remove_node(self, node: Node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def move_to_tail(self, node: Node):
        self.remove_node(node)
        self.add_to_tail(node)

    def pop_head(self) -> Node:
        # Real LRU is right after dummy head
        if self.head.next == self.tail:
            return None
        lru = self.head.next
        self.remove_node(lru)
        return lru


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = dict()  # key -> node
        self.dll = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.dll.move_to_tail(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.value = value
            self.dll.move_to_tail(node)
        else:
            if len(self.map) >= self.capacity:
                lru = self.dll.pop_head()
                if lru:
                    del self.map[lru.key]
            new_node = Node(key, value)
            self.dll.add_to_tail(new_node)
            self.map[key] = new_node
