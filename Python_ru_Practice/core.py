class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Insert an element at the back
    def pushback(self, value):
        new_node = Node(value)
        if self.tail is None:  # If deque is empty
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node  # Link the last node to new node
            new_node.prev = self.tail  # Link new node back to last node
            self.tail = new_node  # Update tail to new node
        self.size += 1  # Increase size count
        # print(new_node.data)  # Print pushed value
        return new_node

    # Remove an element from the back
    def pop_back(self):
        if self.head is None:
            print("Error, deque is empty")
            return None
        value = self.tail.data  # Get the value of the last node
        if self.head == self.tail:  # If deque has only one node
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev  # Move tail back
            self.tail.next = None  # Remove reference to the old tail
        self.size -= 1  # Decrease size count
        return value  # Return the value of the popped node

    # Insert an element at a specified position
    def insert(self, value, position):
        new_node = Node(value)
        if position <= 0:
            return self.pushback(value)  # If position is 0 or less, push back
        elif position >= self.size:  # If position is beyond current size
            return self.pushback(value)  # Just push back
        
        current_node = self.head
        for _ in range(position):
            current_node = current_node.next
        
        new_node.prev = current_node.prev
        if current_node.prev:  # If there is a previous node
            current_node.prev.next = new_node
        new_node.next = current_node
        current_node.prev = new_node
        self.size += 1

    # Show the contents of the deque in a specific format
    def show_deque(self):
        current_node = self.head
        output = []
        if self.head is None:
            print("deque is empty")
        while current_node is not None:
            output.append(str(current_node.data))  # Collect data in a list
            current_node = current_node.next
        print(" --> ".join(output))  # Join with " --> " and print

"вставки элемента --> deque.pushback(value=)"
"- удаление элемента --> deque.pop_back()"
"- вставку в N позицию другого связанного списка, где N - задается при вызове функции пользователем --> deque.insert(value, position)"
"Пример использования"
deque = Deque()
deque.pushback(2)
deque.pushback(2)
deque.pushback(3)
deque.show_deque()  # Should print "1 --> 2 --> 3"
deque.pop_back()
deque.show_deque()  # Should print "1 --> 2"
deque.insert(4, 1)
deque.show_deque()  # Should print "1 --> 4 --> 2"