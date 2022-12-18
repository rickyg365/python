import os
# from utils.trie import Trie

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

    def __str__(self):
        txt = f""
        return txt

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def __str__(self):
        txt = f""
        return txt

    def insert(self, word: str):
        # do_stuff
        current_node = self.root
        for c in word:
            if c not in current_node.children:
                current_node.children[c] = TrieNode()
            current_node = current_node.children[c]
        current_node.end_of_word = True

    def starts_with(self, word: str):
        current_node = self.root
        for c in word:
            if c not in current_node.children:
                return False
            current_node = current_node.children[c]
        return True


    def search(self, word: str):
        # check if it starts with the word
        current_node = self.root

        for c in word:
            if c not in current_node.children:
                return False
            current_node = current_node.children[c]
        return current_node.end_of_word


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

    # Build list of user strings for trie
    user_trie = Trie()
    user_strings = [build_user_str(x) for x in users]

    for user in user_strings:
        user_trie.insert(user)

    t1 = user_trie.starts_with("01")
    print(t1)


if __name__ == "__main__":
    main()