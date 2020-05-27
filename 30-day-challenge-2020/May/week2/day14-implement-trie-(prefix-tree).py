# Implement Trie(Prefix Tree)
# Implement a trie with insert, search, and startsWith methods.

# Example:

# Trie trie = new Trie()
#
# trie.insert("apple")
# trie.search("apple")
# // returns true
#
# trie.search("app")
# // returns false
#
# trie.startsWith("app")
# // returns true
#
# trie.insert("app")
# trie.search("app")
# // returns true
#
# Note:

# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.


class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """

        current = self.root
        for w in word:
            if w not in current.children:  # if key is not found
                current.children[w] = TrieNode()
            current = current.children[w]

        current.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """

        current = self.root
        for w in word:
            if w not in current.children:  # if key is not found
                return False
            current = current.children[w]

        return current.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """

        current = self.root
        for w in prefix:
            if w not in current.children:  # if key is not found
                return False
            current = current.children[w]

        return True

