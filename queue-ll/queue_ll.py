# Queue implementation using Linked List in Python

class Node:
  # dummy node
    def __init__(self, data): 
        self.data = data
        self.next = None
    
# A Linked List class
class QueueLL:
    def __init__(self):  
        self.head = None
        self.tail = None
        self.size = 0
        self.total_workload = 0
        
    # insert at the tail of the linked list
    def enqueue(self, data):
        newNode = Node(data)
        if self.tail is None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1
        self.total_workload += data
            
    # delete an element from the head of the linked list
    def dequeue(self):
        if self.head is None:
            return None
        
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
            
        self.size -= 1
        self.total_workload -= data
        return data
        
    # display an element from the tail of the linked list
    def peek(self):
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            return current.data
        
    # print linked list
    def printLL(self):
        current = self.head
        while(current):
            print(current.data, end =" ")
            current = current.next
            
    # check if the linked list is empty
    def is_empty(self):
        return self.head is None
    
    # return the size of the linked list
    def get_size(self):
        return self.size
    
    # return the total workload
    def get_total_workload(self):
        return self.total_workload

# Main function            
def main():
    queue1 = QueueLL()
    queue2 = QueueLL()
    queue3 = QueueLL()
    queues = [queue1, queue2, queue3]
    enqueue_turn = 0
    dequeue_turn = 0

    def print_queues():
        print("----------------------------------------------\n")
        for i, queue in enumerate(queues, 1):
            print(f"Queue {i}: ", end="")
            if queue.is_empty():
                print("Empty")
            else:
                current = queue.head
                while current:
                    print(current.data, end=" ")
                    current = current.next
                print()
        print("----------------------------------------------\n")

    while True:
        print_queues()
        print("[0] Exit\n[1] Enqueue Workload\n[2] Dequeue Workload\n")
        choice = input("Choice: ")
        print("----------------------------------------------\n")
        if choice == "0":
            print("Thank you!\n")
            print("----------------------------------------------")
            break
        elif choice == "1":
            value = input("Input Value of Workload: ")
            try:
                value = int(value)
            except ValueError:
                print("Invalid input. Please enter an integer.\n")
                continue
            queues[enqueue_turn % 3].enqueue(value)
            enqueue_turn += 1
        elif choice == "2":
            if queues[dequeue_turn % 3].is_empty():
                print("Queue is empty. Cannot dequeue.\n")
            else:
                queues[dequeue_turn % 3].dequeue()
            dequeue_turn += 1
        else:
            print("Invalid choice. Please select 0, 1, or 2.\n")
    

if __name__ == "__main__":
    main()