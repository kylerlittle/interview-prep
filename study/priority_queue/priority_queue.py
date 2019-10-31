

class PriorityQueue:
    """
    Priority queue data structure implemented as a min heap.
    
    Internally, keep track of items
    """
    def __init__(self, key):
        """
        Constructs an empty PriorityQueue

        :param: key: function to apply to elements stored in priority
                     queue to extract its key
        """
        self.keyFunction = key
        self.minHeap = []

    @staticmethod
    def fromarray(key, arr):
        """
        Create a priority queue from array/iterable. Must specify
        key function, like constructor.

        :param: key: function to apply to elements stored in priority
                     queue to extract its key
        :param: arr: iterable array of elements to store in priority queue
        """
        priorityQueue = PriorityQueue(key)

        # insert items into min heap
        for item in arr:
            priorityQueue.insert(item)

        return priorityQueue

    def isEmpty(self):
        """Return whether priority queue is empty
        """
        return not self.minHeap

    def popMin(self):
        """Pop the min element if it exists
        """
        if not self.minHeap:
            return
        
        # store top element
        minElement = self.minHeap[0]

        # copy last element into top position and percolate it down
        self.minHeap[0] = self.minHeap[-1]
        del self.minHeap[-1]
        self.percolateDown()

        # return actual value
        return minElement[1]

    def peekMin(self):
        """Look at the min element if it exists, but don't pop it
        """
        if not self.minHeap:
            raise UserWarning("PriorityQueue is empty.")
        return self.minHeap[0]

    def insert(self, item):
        """
        Insert item into priority queue

        :param: item: item to insert
        """
        try:
            key = self.keyFunction(item)
        except:
            raise ValueError("item is inoperable with key function")
        
        self.minHeap.append((key, item))

        # restore min heap property
        self.percolateUp()
        
    def percolateUp(self):
        """Percolate up the last item inserted (at last index)
        """
        if not self.minHeap:
            return

        iPercolate = len(self.minHeap) - 1
        keyToBePercolated, itemToBePercolated = self.minHeap[iPercolate]

        while True:
            i = int( iPercolate / 2 )
            key, item = self.minHeap[i]

            if keyToBePercolated < key:
                # swap
                temp = self.minHeap[iPercolate]
                self.minHeap[iPercolate] = self.minHeap[i]
                self.minHeap[i] = temp

                # update index
                iPercolate = i
            # min heap property restored
            else:
                break

    def percolateDown(self):
        """Percolate first element downwards until restored min heap property
        """
        if not self.minHeap:
            return

        # overwrite the first element and restore min heap property
        iPercolate = 0

        while True:
            # done iterating when iPercolate * 2 + 1 is out of bounds
            leftI = iPercolate * 2
            rightI = leftI + 1

            # if leftI is out of bounds, we're done
            if leftI >= len(self.minHeap) - 1:
                return

            # if no right child or left child is less than right child, choose left (else right)
            i = leftI if rightI >= len(self.minHeap) - 1 or self.minHeap[leftI][0] < self.minHeap[rightI][0] else rightI

            # continue while heap property hasn't been restored
            if self.minHeap[i][0] < self.minHeap[iPercolate][0]:
                temp = self.minHeap[i]
                self.minHeap[i] = self.minHeap[iPercolate]
                self.minHeap[iPercolate] = temp
            else:
                return

            # continue looping
            iPercolate = i

def main():
    pq = PriorityQueue.fromarray(key=lambda x: x, arr=[5,4,3,2,1,2,5])
    print(pq.peekMin())
    print(pq.minHeap)
    while not pq.isEmpty():
        top = pq.popMin()
        print(top)

if __name__ == "__main__":
    main()