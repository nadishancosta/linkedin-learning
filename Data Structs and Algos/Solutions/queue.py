# Python code​​​​​​‌​‌‌​‌‌​​​​​​‌​​‌​‌‌​​‌‌‌ below
from collections import deque

# Needed for exercise. Do not modify.
class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return not self.items
        # return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

    def __str__(self):
        return str(self.items)

# Complete this function by using a sequence of enqueue() and dequeue() 
# operations, so the final state of my_queue.items is
# deque(['the', 'aardvark', 'wore', 'a', 'silly', 'hat'])
def queue_challenge():
    my_queue = Queue()
    word_list =  ["wore", "a", "silly", "hat", "the", "aardvark"]
    for word in word_list:
        my_queue.enqueue(word)
    for x in range(4):
        my_queue.enqueue(my_queue.dequeue())
    return my_queue.items

if __name__ == "__main__":
    print(queue_challenge())