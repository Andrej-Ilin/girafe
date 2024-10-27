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
            return None  # Return None for error checking
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
            return None  # Return None for error checking
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


if __name__ == '__main__':
    import sys

    # Uncomment these lines to use file input/output:
    sys.stdin = open('input.txt', 'r')
    # sys.stdout = open('output.txt', 'w')

    N = int(input().strip())  # Read number of stores
    queues = [Deque() for _ in range(N)]  # Create a deque for each store
    outputs = []  # Collect outputs to print later

    for line in sys.stdin:  # Read from standard input
        cmd = line.split()
        c_i = cmd[0]  # Command character

        if c_i == '#':  # End of the commands
            break

        q_i = int(cmd[1])  # Store index

        if c_i == '+':  # Regular customer enters the queue
            id_i = int(cmd[2])
            queues[q_i].push_back(id_i)
        elif c_i == '!':  # Certificate holder enters the queue
            id_i = int(cmd[2])
            queue = queues[q_i]
            if queue.length() == 0:
                queue.push_back(id_i)  # If the queue is empty, just append
            else:
                # Insert in the middle (before the central element)
                mid_index = (queue.length() + 1) // 2  # This ensures to insert before the middle
                new_node = Node(id_i)
                current = queue.head

                for _ in range(mid_index):  # Navigate to the mid position
                    current = current.next

                new_node.prev = current.prev
                new_node.next = current

                if current.prev:  # If there is a previous node, adjust pointers
                    current.prev.next = new_node
                else:  # If inserting at the front
                    queue.head = new_node

                current.prev = new_node

                if new_node.next is None:  # If we're at the end, update tail
                    queue.tail = new_node

                queue.size += 1

        elif c_i == '-':  # Customer leaves the queue
            queue = queues[q_i]
            leaving_customer_id = queue.pop_front()  # Remove from the front
            if leaving_customer_id is not None:
                outputs.append(str(leaving_customer_id))  # Output the customer id who left
            else:
                outputs.append("Error!")  # If they try to leave an empty queue
        elif c_i == '?':  # Query on the number of customers in the queue
            outputs.append(str(queues[q_i].length()))

    print("\n".join(outputs))  # Print all outputs at once
