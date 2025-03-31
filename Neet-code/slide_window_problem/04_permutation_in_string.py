"""You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true."""


from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Return true if s2 contains a permutation of s1, or false otherwise.
        That means if a permutation of s1 exists as a substring of s2, then return true.
        """
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        s1_count = Counter(s1)
        s2_count = Counter(s2[:n1])

        if s1_count == s2_count:
            return True

        # slide window
        for i in range(n1, n2):
            # add the new element
            s2_count[s2[i]] += 1

            # remove the oldest element
            s2_count[s2[i - n1]] -= 1
            if s2_count[s2[i - n1]] == 0:
                del s2_count[s2[i - n1]]

            if s1_count == s2_count:
                return True

        return False
