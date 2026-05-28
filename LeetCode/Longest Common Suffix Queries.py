from typing import List


class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.best_idx = -1

    def containsKey(self, ch):
        return self.links[ord(ch) - ord('a')] is not None

    def put(self, ch, new_node):
        self.links[ord(ch) - ord('a')] = new_node

    def get(self, ch):
        return self.links[ord(ch) - ord('a')]

class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        self.words = words

    def better(self, i, j):
        if j == -1:
            return i

        if len(self.words[i]) < len(self.words[j]):
            return i

        if len(self.words[i]) == len(self.words[j]) and i < j:
            return i

        return j

    def insert(self, word, index):
        node = self.root
        node.best_idx = self.better(index, node.best_idx)

        for ch in word[::-1]:
            if not node.containsKey(ch):
                node.put(ch, TrieNode())

            node = node.get(ch)
            node.best_idx = self.better(index, node.best_idx)

    def query(self, word):
        node = self.root
        res = node.best_idx

        for ch in word[::-1]:
            if not node.containsKey(ch):
                break

            node = node.get(ch)
            res = node.best_idx

        return res

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        ans = []

        trie = Trie(wordsContainer)

        for i, w in enumerate(wordsContainer):
            trie.insert(w, i)

        for word in wordsQuery:
            ans.append(trie.query(word))

        return ans