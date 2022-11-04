import os

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

    def __str__(self):
        txt = f"{2}"
        return txt

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def __str__(self):
        txt = f"{2}"
        return txt

    def insert(self, word: str):
        # do_stuff
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_of_word = True

    def starts_with(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


    def search(self, word: str):
        # check if it starts with the word
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.end_of_word


def main():
    
    t = Trie()
    t.insert("apple")

    r1 = t.search("apple")
    r2 = t.search("app")
    r3 = t.starts_with("app")

    result = f"""
Result 1: [search] apple -> {r1}
Result 2: [search] app -> {r2}
Result 3: [starts_with] app -> {r3}    
"""
    print(result)

if __name__ == "__main__":
    main()