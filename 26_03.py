
from collections import Counter
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        count = Counter()
        for b in B:
            count |= Counter(b)

        return [a for a in A if not count - Counter(a)]