class Node:
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq
    
    def __str__(self):
        return f"{(self.symbol, self.freq)}"

parent = lambda i: (i-1) // 2
left = lambda i: 2*i + 1
right = lambda i: 2*i + 2

def heapify_down(A, size, i):
    l = left(i)
    r = right(i)
    best = i
    while l < size:
        best = i
        if A[best] < A[l]:
            best = l
        if r < size and A[best] < A[r]:
            best = r
        if best == i:
            break
        else:
            A[best], A[i] = A[i], A[best]
            i = best
            l = left(i)
            r = right(i)

def make_heap(A, size):
    for i in range(size - 1, -1, -1):
        heapify_down(A, len(A), i)

def heap_extract_min(A):
    return -1

def heap_push(A, element):
    A.append(element)
    heapify_down(A, len(A), 0)
    for i in A:
        print(i)



def huffman(symbols, frequencies):
    heap = []
    for i in range(len(symbols)): # THETA(n), n = len(symbols)
        heap.append(Node(symbols[i], frequencies[i]))
    make_heap(heap)

    # O(n lg n)
    while len(heap) > 1: # enter n-1 times, n = len(heap)
        left = heap_extract_min(heap) # O(lg n)
        right = heap_extract_min(heap) # O(lg n)
        paul = Node(None, left.freq + right.freq)
        paul.left = left
        paul.right = right
        heap_push(heap, paul) # O(lg n)
    
    return heap[0]

# runtime = O(n lg n)
# memory = THETA(n)

huffman()

_='''
why is this optimal?
1. given an optimal code, the 2 min. freq. symbols can be put together
why? given an optimal code, the tree must be full.
there are two leaf nodes together at max depth.
we can swap the 2 min. freq. nodes with them, and the code can only improve.

ex.
a = depth 1 = d1
b = depth 2 = d2
a,b are min. freq.s
x, y = depth 3 = d3

old # of bits = d1freq(a) + d2freq(b) + d3( freq(x) + freq(y) )
swap a&x, b&y s.t. min. freq.s are deeper in tree
new # of bits = d3( freq(a) + freq(b) ) + d1freq(x) + d2freq(y)
new # of bits will always be lower

2. minimizing the original sum of freq.s of n nodes is equivalent to minimizing the sum of the n-1 nodes after merging
after we merge 2 nodes a,b with freq.s j,k respectively, the parent node freq. is j+k -> down 1 node


'''