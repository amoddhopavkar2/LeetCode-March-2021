# Friday, 12th March 2021
# Check If a String Contains All Binary Codes of Size K

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return len(set([s[i : i + k] for i in range(len(s) - k + 1)])) == pow(2, k)
