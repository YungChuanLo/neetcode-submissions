from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        order = Counter(nums).most_common()

        result = order[:k]

        result = [i[0] for i in result]
        
        return result