# Sunday, 21st March 2021
# Reordered Power of 2

class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        res = sorted([int(x) for x in str(N)])
        for i in range(30):
            if sorted([int(x) for x in str(1 << i)]) == res:
                return True
        return False
