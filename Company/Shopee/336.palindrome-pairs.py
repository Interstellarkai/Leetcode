#
# @lc app=leetcode id=336 lang=python3
#
# [336] Palindrome Pairs
#

# @lc code=start
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """
        https://leetcode.com/problems/palindrome-pairs/discuss/79209/Accepted-Python-Solution-With-Explanation
        Worst case time complexity takes O(n * m * m) where n is the length of words and m is the length of wordlist.
        Average case time complexity takes O(n * m). As in the average case, the dictionary (aka hashmap) takes a search of O(1) on average case time complexity.
        T : 35.48% | 5563ms
        S : 84.38% | 26.3mb

        enumerate or iteritems?
            iteritems() is a dictionary method, which returns a lazily constructed
            sequence of all (key, value) pairs in the dictionary.

            enumerate(seq) is a function that returns a lazily constructed list of
            (index, value) pairs for all values in a sequence.
        """
        def is_palindrome(check):
            return check == check[::-1]

        words = {word: i for i, word in enumerate(words)}
        valid_pals = []

        for word, k in words.items():
            n = len(word)
            # why n+1? because in word[:j] arg2, j is excluded, so to get full string as prefix, we need n+1 as j
            for j in range(n+1):
                # pass by value
                pref, suf = word[:j], word[j:]

                # suffix reversed + prefix + suffix
                if is_palindrome(pref):
                    # reverse whatever that is behind this prefix, aka the suffix
                    back = suf[::-1]
                    # prevent duplicates (pre: '', suf: word)
                    if back != word and back in words:
                        valid_pals.append([words[back],  k])
                # prefix + suffix + prefix reversed
                # prevent duplicates (pre: word, suf: '')
                if j != n and is_palindrome(suf):
                    back = pref[::-1]
                    if back != word and back in words:
                        valid_pals.append([k, words[back]])
        return valid_pals


"""
https://leetcode.com/problems/palindrome-pairs/discuss/1987826/Python-Trie-solution-explained
"""


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end = False
        self.idx = -1
        self.palindromeIdxs = list()


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res = list()

        # populate the trie with
        # the reverse of every word.
        # once we're done inserting
        # we're going to have 3 conditions
        for i in range(len(words)):
            cur = self.root
            rWord = words[i][::-1]
            for j in range(len(rWord)):
                # if the current word (from j onwards)
                # is a palindrome, add it's index to the trie node
                # (palindromIdx list) we'll use it later on to find combinations
                if self.isPalindrome(rWord[j:]):
                    cur.palindromeIdxs.append(i)

                if rWord[j] not in cur.children:
                    cur.children[rWord[j]] = TrieNode()
                cur = cur.children[rWord[j]]

            # once the word is done
            # add it's index to the trie node
            cur.end = True
            cur.idx = i

        for i in range(len(words)):
            self.search(words[i], i, res)

        return res

    # to find all pairse, we can have
    # conditions:
    # 1. exact match (abc, cba)
    # 2. long word, short word in trie match (abbcc, a)
    # 3. short word, long word in trie match (lls, sssll)
    def search(self, word, idx, res):
        cur = self.root
        for i in range(len(word)):
            # 2. long word, short trie
            # so the trie ended here and
            # we have matched till the ith
            # character, so we check if the
            # remaining of the word is also a
            # palindrome, if yes, then we have a pair
            # for e.g. word = abcdaa, trieWord = bcda
            # we can make a pair like abcdaabcda
            if cur.end and self.isPalindrome(word[i:]):
                res.append([idx, cur.idx])

            if word[i] not in cur.children:
                return
            cur = cur.children[word[i]]

        # 1. exact match
        # in the given list, for that
        # we'll take every word and then
        # check if the reverse of that
        # word lies in the trie
        # for e.g. for abc and cba
        # the trie would have both c->b->a and a->b->c
        # but when we take the first word (abc)
        # we'll match this with a->b->c which is
        # actually cba and so we found a match
        if cur.end and cur.idx != idx:
            res.append([cur.idx, idx])

        # 3. long trie, short word
        # so the trie still has items (not cur.end)
        # and the word has ended, it's the exact
        # opposite of point 2
        # for e.g. word=abcd trieWord=bcdaa
        # we can have a pair bcdaaabcd
        # and so we have a pair
        for pIdx in cur.palindromeIdxs:
            res.append([idx, pIdx])

        return

    def isPalindrome(self, s):
        return s == s[::-1]
# @lc code=end
