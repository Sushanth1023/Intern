import json
import os

QUEUE_FILE="queue.json"
def load_queue():
    if os.path.exists(QUEUE_FILE):
        with open(QUEUE_FILE,'r') as file:
            return json.load(file)
    else: 
        return []
def save_queue(queue):
    with open(QUEUE_FILE,'w') as file:
        json.dump(queue,file,indent=4)
    print(f"Queue saved to file: {queue}")
def enqueue():
    queue=load_queue()
    element=input("Enter the element to enqueue: ")
    queue.append(element)
    save_queue(queue)
    print(f"Enqueued:{queue}")
def dequeue():
    queue=load_queue()
    if queue:
        removed=queue.pop(0)
        save_queue(queue)
        print(f"Dequeued:{removed}")
    else:
        print("Queue and file are empty")
def is_empty():
    queue=load_queue()
    if len(queue)==0:
        print("Queue is empty")
    else:
        print("Queue is not empty")
def check_size():
    queue=load_queue()
    print(f"Queue size:{len(queue)}")
def print_queue():
    queue=load_queue()
    print(f"Current queue: {queue}")

while True:
    print("Options are:")
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Check if queue is empty")
    print("4.Check Size of queue")
    print("5.Print queue")
    print("6.Exit")
    c=input("Enter your choice:")
    if c=='1':
        enqueue()
    elif c=='2':
       dequeue()
    elif c=='3':
        is_empty()
    elif c=='4':
        check_size()
    elif c=='5':
        print_queue()
    elif c=='6':
        print("Exiting.")
        break
    else:
        print("Invalid choice")
