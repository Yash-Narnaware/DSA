#TUF - https://takeuforward.org/plus/dsa/problems/trie-implementation-and-advanced-operations

class Node:
    def __init__(self):
        self.ref = [None]*26
        self.terminal = -1

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        tmp = self.root

        for chr1 in word:
            if not self.present_in_ref(tmp, chr1):
                self.add_ref(tmp, chr1, Node())
            tmp = self.get_ref_node(tmp, chr1)

        if tmp.terminal == -1:
            tmp.terminal = 1
        else:
            tmp.terminal += 1

    def countWordsEqualTo(self, word):
        """
        :type word: str
        :rtype: int
        """

        tmp = self.root

        for chr1 in word:
            if not self.present_in_ref(tmp, chr1):
                return 0
            tmp = self.get_ref_node(tmp, chr1)
        if tmp.terminal == -1:
            return 0
        else:
            return tmp.terminal

    def countWordsStartingWith(self, prefix):
        """
        :type word: str
        :rtype: int
        """

        tmp = self.root

        for chr1 in prefix:
            if not self.present_in_ref(tmp, chr1):
                return 0
            tmp = self.get_ref_node(tmp, chr1)
        
        return self.cnt(tmp)


    def erase(self, word):
        """
        :type word: str
        :rtype: None
        """

        tmp = self.root

        for chr1 in word:
            if not self.present_in_ref(tmp, chr1):
                return 
            tmp = self.get_ref_node(tmp, chr1)
        if tmp.terminal == 1:
            tmp.terminal = -1
        else:
            tmp.terminal -= 1

    def present_in_ref(self, node, char):
        return node.ref[ord(char) - ord('a')] != None

    def add_ref(self, node1, char, node2):
        node1.ref[ord(char) - ord('a')] = node2
    
    def get_ref_node(self, node, char):
        return node.ref[ord(char) - ord('a')]

    def cnt(self, node):

        res = 0
        for i in node.ref:
            if i != None:
                res += self.cnt(i)

        if node.terminal != -1:
            return res + node.terminal
        else:
            return res

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
