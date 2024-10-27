class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_back(self, value):
        new_node = Node(value)
        if self.tail is None:  # If deque is empty
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def push_front(self, value):
        new_node = Node(value)
        if self.head is None:  # If deque is empty
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def pop_back(self):
        if self.tail is None:  # Deque is empty
            print("Error!")
            return None
        value = self.tail.data
        if self.head == self.tail:  # Only one element case
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return value

    def pop_front(self):
        if self.head is None:  # Deque is empty
            print("Error!")
            return None
        value = self.head.data
        if self.head == self.tail:  # Only one element case
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return value

    def length(self):
        return self.size

# Create a deque instance
deque = Deque()

# Read commands and process them
while True:
    request = input().strip()
    if request == "-1":
        break

    parts = list(map(int, request.split()))
    operation = parts[0]

    if operation == 0:  # push_back
        value = parts[1]
        deque.push_back(value)
    elif operation == 1:  # push_front
        value = parts[1]
        deque.push_front(value)
    elif operation == 2:  # len
        print(deque.length())
    elif operation == 3:  # pop_back
        result = deque.pop_back()
        if result is not None:
            print(result)
    elif operation == 4:  # pop_front
        result = deque.pop_front()
        if result is not None:
            print(result)
