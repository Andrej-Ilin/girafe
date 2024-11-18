"https://contest.yandex.ru/contest/70071/problems/A/"

def sift_up(heap, i):
    if i == 0:
        return
    parent = (i - 1) // 2
    if heap[parent] > heap[i]:
        heap[parent], heap[i] = heap[i], heap[parent]
        sift_up(heap, parent)

def sift_down(heap, i):
    child1 = 2 * i + 1
    child2 = 2 * i + 2
    if child1 >= len(heap):
        return
    if child2 >= len(heap):
        child_min = child1
    else:
        child_min = child1 if heap[child1] < heap[child2] else child2
    if heap[child_min] < heap[i]:
        heap[i], heap[child_min] = heap[child_min], heap[i]
        sift_down(heap, child_min)

def heapify(heap):
    for i in range(len(heap) -1, -1, -1):
        sift_down(heap, i)

def heap_push(heap, value):
    heap.append(value)
    sift_up(heap, len(heap) - 1)
def heap_pop(heap, i = 0):
    heap[i], heap[-1] = heap[-1], heap[i]
    res = heap.pop()
    sift_down(heap, i)
    sift_down(heap, i)
    return res

def simulate_queue(events):
    queue = []
    customer_counter = 0

    for event in events:
        event_type = event[0]
        if event_type == '+':
            customer_id = int(event[1])
            priority = int(event[2])
            heap_push(queue, (-priority, customer_counter, customer_id))
            customer_counter += 1
        elif event_type == '-':
            if queue:
                _, _, customer_id = heap_pop(queue)
                print(customer_id)

# Read the input
n = int(input())
events = [input().split() for _ in range(n)]

# Simulate the queueing process
simulate_queue(events)
