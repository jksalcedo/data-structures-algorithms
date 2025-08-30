class Node:
    def __init__(self, data):
        # Initialize a node with data
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        # Initialize an empty stack
        self.top = None
        self.size = 0

    def push(self, data):
        # Push a new element onto the stack
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        # Pop the top element from the stack
        if self.is_empty():
            return None
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def peek(self):
        # Peek at the top element
        if self.is_empty():
            return None
        return self.top.data

    def is_empty(self):
        # Check if the stack is empty
        return self.top is None

    def __len__(self):
        # Return the size of the stack
        return self.size

def get_suffix_sums(lst):
    # Calculate suffix sums for a list
    n = len(lst)
    suffix = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix[i] = suffix[i + 1] + lst[i]
    return suffix[:-1]

def find_suffix(lst, suf, h):
    # Find the suffix of the list that matches the given height
    for i in range(len(suf)):
        if suf[i] == h:
            return lst[i:]
    return []

def main():
    while True:
        try:
            # Read input for three stacks
            s1_input = input("Enter elements of Stack 1: ").split()
            s1 = [int(x) for x in s1_input]
            s2_input = input("Enter elements of Stack 2: ").split()
            s2 = [int(x) for x in s2_input]
            s3_input = input("Enter elements of Stack 3: ").split()
            s3 = [int(x) for x in s3_input]
        except ValueError:
            # Handle invalid input
            print("Invalid input, please enter integers separated by space.")
            continue

        # Create stacks and push elements
        stack1 = Stack()
        for x in s1:
            stack1.push(x)
        stack2 = Stack()
        for x in s2:
            stack2.push(x)
        stack3 = Stack()
        for x in s3:
            stack3.push(x)

        # Calculate total heights of stacks
        total1 = sum(s1)
        total2 = sum(s2)
        total3 = sum(s3)

        print("----------------------------------------------")
        print(f"Stack 1 total height: {total1}")
        print(f"Stack 2 total height: {total2}")
        print(f"Stack 3 total height: {total3}")
        print("----------------------------------------------")

        # Calculate suffix sums for each stack
        suf1 = get_suffix_sums(s1)
        suf2 = get_suffix_sums(s2)
        suf3 = get_suffix_sums(s3)

        # Find common heights among the stacks
        set1 = set(suf1)
        set2 = set(suf2)
        set3 = set(suf3)

        common = set1 & set2 & set3
        if not common:
            # No common height found
            print("Stack heights will never be equal.")
        else:
            # Find the maximum common height
            h = max(common)
            print(f"All stacks are equal at Height: {h}")

            # Find the remaining elements in each stack
            rem1 = find_suffix(s1, suf1, h)
            rem2 = find_suffix(s2, suf2, h)
            rem3 = find_suffix(s3, suf3, h)

            print(f"Stack 1: {' '.join(map(str, rem1))}")
            print(f"Stack 2: {' '.join(map(str, rem2))}")
            print(f"Stack 3: {' '.join(map(str, rem3))}")

        print("----------------------------------------------")
        # Ask user if they want to continue
        cont = input("Continue? Y or N? ").strip().upper()
        if cont == 'N':
            print("Thank you!")
            break
        print("----------------------------------------------")

if __name__ == "__main__":
    main()