charsize = 26
 
# storing a Trie node
class Node:
    next = [None] * charsize
    exist = False       #returns true on leaf node
 
 
#inserting a string into a Trie
def insertingTrie(head, S):

    node = head
 
    # traversing each character of S
    for c in S:
 
        index = ord(c) - ord('a')
 
        # it will create a new node when the path is not present
        if node.next[index] is None:
            node.next[index] = Node()
 
        # go to the next node
        node = node.next[index]
 
    # mark the last node as a leaf
    node.exist = True
 
 
# method to determine if a string can be unconcatenated into space-separated form
def wordBreak(head, S):
 
    # length of S
    n = len(S)
 
    # `fine[i]` is true if the first `i` characters of `S` can be unconcatenated
    fine = [None] * (n + 1)
    fine[0] = True
 
    for i in range(n):
        if fine[i]:
            node = head
            for j in range(i, n):
                if node is None:
                    break
 
                index = ord(S[j]) - ord('a')
                node = node.next[index]
 
                # we can make [0, i] using decomposition given in D
                # and [i+1, j] using the S in a Trie
                if node and node.exist:
                    fine[j + 1] = True
 
    # `fine[n]` would be true if all characters of `S` can be unconcatenated
    return fine[n]
 
 
if __name__ == '__main__':
 
    # a dictionary D, i.e. a list of n strings
    D = ['a', 'back', 'day', 'go', 'garden', 'gardening', 'is', 'my', 'to', 'today', 'yard', 'you', 'in']
 
    # a string S of m characters
    S = 'todayisanicedaytodogardeninginmybackyard'
 
    # created a Trie to store D
    trie = Node()
    for word in D:
        insertingTrie(trie, word)

    print(wordBreak('t',S))
