class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        result = []
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        for i in range(0,k):
            max_key = max(counts, key=counts.get)
            counts.pop(max_key)
            result.append(max_key)
            i += 1
        
        return result

        
         