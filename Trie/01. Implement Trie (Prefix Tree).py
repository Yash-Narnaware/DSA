#Leetcode - https://leetcode.com/problems/implement-trie-prefix-tree/description/


class Node:

    def __init__(self):
        self.ref = [None]*26
        self.terminal = False

class Trie:

    def __init__(self):
        self.root = Node()

    def contains(self, node, char):
        return node.ref[ord(char) - ord('a')] != None

    def add_ref(self, node1, char, node):
        node1.ref[ord(char) - ord('a')] = node

    def get_ref_node(self, node, char):
        return node.ref[ord(char) - ord('a')]

    def set_terminal(self, node):
        node.terminal = True
    
    def is_terminal(self, node):
        return node.terminal
        

    def insert(self, word: str) -> None:
        tmp = self.root

        for chr in word:
            if not self.contains(tmp, chr):
                self.add_ref(tmp, chr, Node())
            tmp = self.get_ref_node(tmp, chr)

        self.set_terminal(tmp)
            
        

    def search(self, word: str) -> bool:
        tmp = self.root

        for chr in word:
            if not self.contains(tmp, chr):
                return False
            tmp = self.get_ref_node(tmp, chr)
        
        return self.is_terminal(tmp)

        

    def startsWith(self, prefix: str) -> bool:

        tmp = self.root

        for chr in prefix:
            if not self.contains(tmp, chr):
                return False
            tmp = self.get_ref_node(tmp, chr)

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
