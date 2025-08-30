class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

    def __len__(self):
        return self.size

def get_suffix_sums(lst):
    n = len(lst)
    suffix = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix[i] = suffix[i + 1] + lst[i]
    return suffix[:-1]

def find_suffix(lst, suf, h):
    for i in range(len(suf)):
        if suf[i] == h:
            return lst[i:]
    return []

def main():
    while True:
        try:
            s1_input = input("Enter elements of Stack 1: ").split()
            s1 = [int(x) for x in s1_input]
            s2_input = input("Enter elements of Stack 2: ").split()
            s2 = [int(x) for x in s2_input]
            s3_input = input("Enter elements of Stack 3: ").split()
            s3 = [int(x) for x in s3_input]
        except ValueError:
            print("Invalid input, please enter integers separated by space.")
            continue

        # Create stacks 
        stack1 = Stack()
        for x in s1:
            stack1.push(x)
        stack2 = Stack()
        for x in s2:
            stack2.push(x)
        stack3 = Stack()
        for x in s3:
            stack3.push(x)

        total1 = sum(s1)
        total2 = sum(s2)
        total3 = sum(s3)

        print("----------------------------------------------")
        print(f"Stack 1 total height: {total1}")
        print(f"Stack 2 total height: {total2}")
        print(f"Stack 3 total height: {total3}")
        print("----------------------------------------------")

        suf1 = get_suffix_sums(s1)
        suf2 = get_suffix_sums(s2)
        suf3 = get_suffix_sums(s3)

        set1 = set(suf1)
        set2 = set(suf2)
        set3 = set(suf3)

        common = set1 & set2 & set3
        if not common:
            print("Stack heights will never be equal.")
        else:
            h = max(common)
            print(f"All stacks are equal at Height: {h}")

            rem1 = find_suffix(s1, suf1, h)
            rem2 = find_suffix(s2, suf2, h)
            rem3 = find_suffix(s3, suf3, h)

            print(f"Stack 1: {' '.join(map(str, rem1))}")
            print(f"Stack 2: {' '.join(map(str, rem2))}")
            print(f"Stack 3: {' '.join(map(str, rem3))}")

        print("----------------------------------------------")
        cont = input("Continue? Y or N? ").strip().upper()
        if cont == 'N':
            print("Thank you!")
            break
        print("----------------------------------------------")

if __name__ == "__main__":
    main()