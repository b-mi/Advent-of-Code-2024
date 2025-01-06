import tools
import numpy as np
import math
from astar import AStar

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

def build_trie(substrings):
    root = TrieNode()
    for word in substrings:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    return root

def count_ways_with_trie(target, root):
    n = len(target)
    dp = [0] * (n + 1)
    dp[0] = 1  # Prázdny reťazec možno vyskladať 1 spôsobom

    for i in range(n):
        if dp[i] > 0:  # Len ak existujú spôsoby, ako vyskladať reťazec do indexu `i`
            node = root
            for j in range(i, n):
                char = target[j]
                if char not in node.children:
                    break
                node = node.children[char]
                if node.is_end_of_word:
                    dp[j + 1] += dp[i]

    return dp[n]


if __name__ == "__main__":
    
    result = 0
    total_ok = 0
    # file_name = '19'
    file_name = '19f'
    lines = tools.get_lines(file_name)
    vars = lines[0].split(', ')
    for line_idx in range( 2, len(lines)):
        print(f'{line_idx}/{len(lines)}')
        line = lines[line_idx]
        trie_root = build_trie(vars)
        result = count_ways_with_trie(line, trie_root)
        total_ok += result
    #check('gbbr')
    result = total_ok
    print("end", result)
