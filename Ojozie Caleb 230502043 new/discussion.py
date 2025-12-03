def main():
    print("\nASSIGNMENT QUESTIONS AND ANSWERS\n")

    # Question 1
    print("1. What are the key differences between primitive data types and ADTs?")
    print("Answer:")
    print("- Primitive data types are basic built-in types such as int, float, bool, and char.")
    print("- Abstract Data Types (ADTs) are user-defined models like stacks, queues, and lists that specify what operations can be done, not how they are implemented.\n")

    # Question 2
    print("2. Why are arrays considered static, and linked lists dynamic?")
    print("Answer:")
    print("- Arrays are static because their size is fixed when created and cannot grow or shrink.WHILE")
    print("- Linked lists are dynamic because nodes can be added or removed at runtime without needing a fixed size.\n")

    # Question 3
    print("3. In what situations would you prefer a linked list over an array?")
    print("Answer:")
    print("- When you need frequent insertions and deletions.")
    print("- When memory is limited or unpredictable.")
    print("- When the size of the data is not known beforehand.\n")

    # Question 4
    print("4. Real-world examples where each structure would be useful:")
    
    print("\n   o Stack:")
    print("     - Undo/redo buttons in apps.")
    print("     - Browser back button.")
    print("     - Expression evaluation (e.g., calculators).")
    
    print("\n   o Queue:")
    print("     - Waiting line in banks.")
    print("     - Printer job scheduling.")
    print("     - Customer service ticketing systems.")
    
    print("\n   o Linked List:")
    print("     - Music playlists that allow easy insertion/removal.")
    print("     - Navigation through a photo gallery.")
    print("     - Implementing browser forward/backward history.\n")

# ============================================================
# Differences Between Stack and Queue + Time Complexities
# ============================================================

# 1. Five Differences Between Stack and Queue
print("----- DIFFERENCES BETWEEN STACK AND QUEUE -----")
differences = [
    "1. Stack follows LIFO (Last In First Out), Queue follows FIFO (First In First Out).",
    "2. Stack inserts and removes at one end (Top), Queue inserts at Rear and removes at Front.",
    "3. Stack operations: push(), pop() | Queue operations: enqueue(), dequeue().",
    "4. Stack is used for function calls, undo operations | Queue is used for scheduling and buffering.",
    "5. In Stack the last element inserted is removed first | In Queue the first element inserted is removed first."
]

for diff in differences:
    print(diff)



# 2. Time Complexity of Stack and Queue
print("\n----- TIME COMPLEXITY OF STACK -----")
stack_time = [
    "Push   -> O(1)",
    "Pop    -> O(1)",
    "Peek   -> O(1)",
    "IsEmpty-> O(1)"
]

for t in stack_time:
    print(t)

print("\n----- TIME COMPLEXITY OF QUEUE -----")
queue_time = [
    "Enqueue -> O(1)",
    "Dequeue -> O(1)",
    "Front   -> O(1)",
    "IsEmpty -> O(1)"
]

for t in queue_time:
    print(t)


if __name__ == '__main__':
    main()
