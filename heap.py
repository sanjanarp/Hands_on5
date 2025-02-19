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
        """Get the index of the parent node using bitwise shift."""
        return (i - 1) >> 1  

    def left(self, i):
        """Get the index of the left child using bitwise shift."""
        return (i << 1) + 1  

    def right(self, i):
        """Get the index of the right child using bitwise shift."""
        return (i << 1) + 2  

    def swap(self, i, j):
        """Swap two elements in the heap."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapify(self, i):
        """Ensure the heap property is maintained from index i downward."""
        smallest = i  
        left_child = self.left(i)  
        right_child = self.right(i)  
        size = len(self.heap)  

        if left_child < size and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child

        if right_child < size and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        if smallest != i:
            self.swap(i, smallest)
            self.heapify(smallest)

    def build_min_heap(self):
        """Convert an unordered array into a valid min-heap."""
        n = len(self.heap)
        for i in range((n - 1) >> 1, -1, -1):  
            self.heapify(i)

    def pop(self):
        """Remove and return the root (minimum element) from the heap."""
        if not self.heap:
            raise IndexError("Heap is empty")
        
        root = self.heap[0]  
        last_element = self.heap.pop()  
        
        if self.heap:  
            self.heap[0] = last_element
            self.heapify(0)

        return root  

    def insert(self, value):
        """Insert a new element into the heap while maintaining the heap property."""
        self.heap.append(value)  
        i = len(self.heap) - 1  

        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)  

    def __str__(self):
        """Return a string representation of the heap."""
        return str(self.heap)


# Demonstration of heap functionality
if __name__ == "__main__":
    print("### Min-Heap Demonstration ###")

    # Step 1: Building the Min-Heap from an unordered array
    arr = [10, 3, 5, 8, 2, 7, 6]
    print("\nBuilding Min-Heap from:", arr)
    heap = MinHeap(arr)
    print("Heap after build_min_heap():", heap)

    # Step 2: Inserting elements
    print("\n### Inserting elements ###")
    heap.insert(1)
    print("Heap after inserting 1:", heap)

    heap.insert(4)
    print("Heap after inserting 4:", heap)

    heap.insert(0)
    print("Heap after inserting 0:", heap)

    # Step 3: Extracting elements (pop)
    print("\n### Popping elements ###")
    print("Extracted:", heap.pop())
    print("Heap after pop():", heap)

    print("Extracted:", heap.pop())
    print("Heap after pop():", heap)

    print("Extracted:", heap.pop())
    print("Heap after pop():", heap)

    # Step 4: Pop until empty to test full functionality
    print("\n### Extracting all elements ###")
    while heap.heap:
        print("Extracted:", heap.pop())
        print("Heap now:", heap)

    # Step 5: Edge cases - popping from an empty heap
    try:
        heap.pop()
    except IndexError as e:
        print("\nException caught when popping from empty heap:", e)
