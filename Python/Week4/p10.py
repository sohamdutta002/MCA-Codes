#  Write a Python program to implement Queue using array.
def enqueue(queue, element):
    queue.append(element)
    return queue

def dequeue(queue):
    if len(queue) == 0:
        return "Queue is empty"
    else:
        return queue.pop(0)

def display(queue):
    return queue

def is_empty(queue):
    return len(queue) == 0

queue = []
while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Is empty")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        element = int(input("Enter the element to be enqueued: "))
        print("Queue after enqueuing: ", enqueue(queue, element))
    elif choice == 2:
        print("Element dequeued: ", dequeue(queue))
    elif choice == 3:
        print("Queue: ", display(queue))
    elif choice == 4:
        print("Is empty: ", is_empty(queue))
    elif choice == 5:
        break
    else:
        print("Invalid choice")