# Define the Node class
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Function to detect if there is a cycle in the linked list
def has_cycle(head):
    """
        Function to detect if there is a cycle in the linked list.

        Parameters:
        head (Node): The head node of the linked list. It represents the first node in the list.
                     If the list is empty, this will be `None`.

        Returns:
        bool: Returns `True` if there is a cycle in the linked list, otherwise returns `False`.
        """
    pass
    # code goes here :)



# Test cases

# Test Case 1: No Cycle
# Create a linked list: 1 -> 2 -> 3 -> None
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3

print(has_cycle(node1))  # Expected Output: False

# Test Case 2: Cycle in the middle
# Create a linked list with a cycle: 1 -> 2 -> 3 -> 4 -> 2 (cycle between 4 and 2)
node4 = Node(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Cycle

print(has_cycle(node1))  # Expected Output: True

# Test Case 3: Cycle at the end
# Create a linked list with a cycle: 1 -> 2 -> 3 -> 4 -> 5 -> 3 (cycle between 5 and 3)
node5 = Node(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3  # Cycle

print(has_cycle(node1))  # Expected Output: True

# Test Case 4: Empty list
print(has_cycle(None))  # Expected Output: False

# Test Case 5: Single node with a cycle
# Create a linked list: 1 -> 1 (cycle)
node6 = Node(1)
node6.next = node6  # Cycle (points to itself)

print(has_cycle(node6))  # Expected Output: True
