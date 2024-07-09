"""String Encode and Decode
Solved 
Design an algorithm to encode a list of strings to a single string. 
The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

"""


from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in strs:
            i = i+'@@@@'+str(len(i))
        return strs

    def decode(self, s: str) -> List[str]:
        return [i.split('@@@@')[0] for i in list(s)]


# Input: ["we","say",":","yes"]
# Output: ["we","say",":","yes"]


# Input: ["we","say",":","yes"]
# Output: ["we","say",":","yes"]

