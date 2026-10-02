class Queue:
    def __init__(self, capacity=None):
        self.queue = []
        self.capacity = capacity

    def enqueue(self, item):
        """Add item to rear of queue - O(1)"""
        if self.capacity and len(self.queue) >= self.capacity:
            print("Queue Overflow!")
            return
        self.queue.append(item)
        print(f"{item} enqueued")

    def dequeue(self):
        """Remove item from front - O(n) for list, use deque for O(1)"""
        if self.is_empty():
            print("Queue Underflow!")
            return None
        return self.queue.pop(0)

    def peek(self):
        """Get front element without removing"""
        if self.is_empty():
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue:", self.queue)

# --- MAIN DRIVER ---
if __name__ == "__main__":
    q = Queue()

    while True:
        print("\n1.Enqueue 2.Dequeue 3.Peek 4.Display 5.Size 6.Exit")
        ch = input("Enter choice: ")

        if ch == '1':
            val = int(input("Enter value: "))
            q.enqueue(val)
        elif ch == '2':
            removed = q.dequeue()
            if removed is not None:
                print(f"Dequeued: {removed}")
        elif ch == '3':
            print(f"Front: {q.peek()}")
        elif ch == '4':
            q.display()
        elif ch == '5':
            print(f"Size: {q.size()}")
        elif ch == '6':
            break
        else:
            print("Invalid choice")
