class MinHeap:
    """Min-Heap implementation using bitwise operations for parent-child access."""

    def __init__(self, data=None):
        """
        Initialize a min-heap.

        Args:
        - data (list): Optional initial list of elements to heapify.
        """
        self.heap = data if data else []  # Initialize heap with given data or an empty list
        if self.heap:  
            self.build_min_heap()  # Convert input list into a valid min-heap

    def parent(self, i):
        """
        Get the index of the parent node using bitwise shift.

        Parent of node at index i: (i - 1) // 2 is the integer division,
        which is equivalent to (i - 1) >> 1 in bitwise operations.
        """
        return (i - 1) >> 1  

    def left(self, i):
        """
        Get the index of the left child using bitwise shift.

        Left child of node at index i is at: 2 * i + 1,
        which is equivalent to (i << 1) + 1.
        """
        return (i << 1) + 1  

    def right(self, i):
        """
        Get the index of the right child using bitwise shift.

        Right child of node at index i is at: 2 * i + 2,
        which is equivalent to (i << 1) + 2.
        """
        return (i << 1) + 2  

    def swap(self, i, j):
        """
        Swap two elements in the heap.

        Args:
        - i (int): Index of first element.
        - j (int): Index of second element.
        """
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapify(self, i):
        """
        Ensure the heap property is maintained from index i downward.

        This method checks if the current node is smaller than its children,
        and if not, swaps it with the smallest child and recursively heapifies.

        Args:
        - i (int): Index to heapify from.
        """
        smallest = i  # Assume the current node is the smallest
        left_child = self.left(i)  # Get left child index
        right_child = self.right(i)  # Get right child index
        size = len(self.heap)  # Size of heap

        # Compare left child with current node
        if left_child < size and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child

        # Compare right child with the smallest found so far
        if right_child < size and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        # If the smallest value is not the current node, swap and continue heapifying
        if smallest != i:
            self.swap(i, smallest)
            self.heapify(smallest)  # Recursively heapify the affected subtree

    def build_min_heap(self):
        """
        Convert an unordered array into a valid min-heap.

        This method starts heapifying from the last non-leaf node (bottom-up).
        """
        n = len(self.heap)
        for i in range((n - 1) >> 1, -1, -1):  # Start from the last non-leaf node
            self.heapify(i)

    def pop(self):
        """
        Remove and return the root (minimum element) from the heap.

        - Swaps the root with the last element.
        - Removes the last element.
        - Restores heap property by heapifying from the root.

        Returns:
        - The minimum element (root of the heap).

        Raises:
        - IndexError: If the heap is empty.
        """
        if not self.heap:
            raise IndexError("Heap is empty")
        
        root = self.heap[0]  # Get the minimum element (root)
        last_element = self.heap.pop()  # Remove last element
        
        if self.heap:  # If heap is not empty, move last element to root and heapify
            self.heap[0] = last_element
            self.heapify(0)

        return root  # Return the extracted minimum element

    def insert(self, value):
        """
        Insert a new element into the heap while maintaining the heap property.

        - Adds the new element at the end.
        - Moves it up the heap until the heap property is restored.

        Args:
        - value: The value to insert.
        """
        self.heap.append(value)  # Insert at the end
        i = len(self.heap) - 1  # Get index of the inserted element

        # Bubble up: Swap with parent if smaller than the parent
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)  # Move up to the parent's index

    def __str__(self):
        """
        Return a string representation of the heap.
        """
        return str(self.heap)


# Demonstration of heap functionality
if __name__ == "__main__":
    print("### Min-Heap Demonstration ###")

    # Initial unsorted array
    arr = [10, 3, 5, 8, 2, 7, 6]
    print("\nBuilding Min-Heap from:", arr)
    heap = MinHeap(arr)
    print("Heap after build_min_heap():", heap)

    # Insert elements
    print("\nInserting elements:")
    heap.insert(1)
    print("Heap after inserting 1:", heap)

    heap.insert(4)
    print("Heap after inserting 4:", heap)

    # Extract the minimum (pop the root)
    print("\nPopping elements:")
    print("Extracted:", heap.pop())
    print("Heap after pop():", heap)

    print("Extracted:", heap.pop())
    print("Heap after pop():", heap)
