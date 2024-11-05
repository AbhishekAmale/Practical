import heapq
from collections import Counter
class Node:
    def __init__(self,char,frq):
        self.char=char
        self.frq=frq
        self.left=None
        self.right=None
        
    def __lt__(self,other):
        return self.frq < other.frq
    
    
def Build_Tree(text):
    frequency=Counter(text)
    heap=[Node(char,freq) for char , freq in frequency.items()]
    #HEAP=[Node(A,3)]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        
        
        left=heapq.heappop(heap)
        print("After Left pop :",len(heap))
        right=heapq.heappop(heap)
        print("After right pop :",len(heap))
        merge=Node(None,left.frq+right.frq)
        merge.left=left
        merge.right=right
        heapq.heappush(heap,merge)
    return heap[0]

def Code(node,prefix="",codebook=None):
    if codebook is None:
        codebook={}
    if node.char is not None:
        codebook[node.char]=prefix
    else:
        Code(node.left,prefix+"0",codebook)
        Code(node.right,prefix+"1",codebook)
    return codebook
    
def Encoding(text):
    root=Build_Tree(text)
    codebook=Code(root)
    encoded_code="".join(codebook[char] for char in text)
    
    return encoded_code,codebook
txt=str(input("Enter Text To Encode :"))
encoded_code,codebook=Encoding(txt)
print("Encoded Code : ",encoded_code)
print("Codebook : ",codebook)



































# import heapq
# from collections import Counter

# class Node:
#     def __init__(self, char, freq):
#         self.char = char  # Character
#         self.freq = freq  # Frequency
#         self.left = None  # Left child
#         self.right = None  # Right child

#     def __lt__(self, other):
#         return self.freq < other.freq 

# def build_huffman_tree(text):
#     frequency = Counter(text)  # Count frequency of each character
#     heap = [Node(char, freq) for char, freq in frequency.items()] 
#     heapq.heapify(heap) 

#     while len(heap) > 1:
#         left = heapq.heappop(heap) 
#         right = heapq.heappop(heap)
#         merged = Node(None, left.freq + right.freq)
#         merged.left = left
#         merged.right = right
#         heapq.heappush(heap, merged)

#     return heap[0] 

# def build_codes(node, prefix="", codebook=None):
#     if codebook is None:
#         codebook = {}

#     if node.char is not None:  # Leaf node
#         codebook[node.char] = prefix
#     else:
#         build_codes(node.left, prefix + "0", codebook)
#         build_codes(node.right, prefix + "1", codebook)

#     return codebook

# def huffman_encoding(text):
#     root = build_huffman_tree(text)
#     codebook = build_codes(root)
#     encoded_text = ''.join(codebook[char] for char in text)  # Encode the text
#     return encoded_text, codebook

# text = input("Enter the text to encode: ")
# encoded_text, codebook = huffman_encoding(text)
# print("Encoded text:", encoded_text)
# print("Codebook:", codebook)