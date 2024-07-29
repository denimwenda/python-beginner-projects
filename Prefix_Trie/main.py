from trie import Trie

# Example usage
trie = Trie()
trie.insert("hello")
print(trie.search("hello"))  # Output: True
print(trie.search("hell"))   # Output: False
print(trie.starts_with("hell"))  # Output: True