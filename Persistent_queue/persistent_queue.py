import json
import os
class Persistent_queue:
    QUEUE_FILE="queue.json"
    def load_queue(self):
        if os.path.exists(self.QUEUE_FILE):
            with open(self.QUEUE_FILE,'r') as file:
                return json.load(file)
        else: 
            return []
    def save_queue(self,queue):
        with open(self.QUEUE_FILE,'w') as file:
            json.dump(queue,file,indent=4)
        print(f"Queue saved to file: {queue}")
    def enqueue(self):
            queue=self.load_queue()
            element=input("Enter the element to enqueue: ")
            queue.append(element)
            self.save_queue(queue)
            print(f"Enqueued:{queue}")
    def dequeue(self):
        queue=self.load_queue()
        if queue:
            removed=queue.pop(0)
            self.save_queue(queue)
            print(f"Dequeued:{removed}")
        else:
            print("Queue and file are empty")
    def is_empty(self):
        queue=self.load_queue()
        if len(queue)==0:
            print("Queue is empty")
        else:
            print("Queue is not empty")
    def check_size(self):
        queue=self.load_queue()
        print(f"Queue size:{len(queue)}")
    def print_queue(self):
        queue=self.load_queue()
        print(f"Current queue: {queue}")
if __name__=='__main__':
    pq=Persistent_queue()
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
            pq.enqueue()
        elif c=='2':
           pq.dequeue()
        elif c=='3':
            pq.is_empty()
        elif c=='4':
            pq.check_size()
        elif c=='5':
            pq.print_queue()
        elif c=='6':
            print("Exiting.")
            break
        else:
            print("Invalid choice")
