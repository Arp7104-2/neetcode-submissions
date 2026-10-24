class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for val in nums:
            counts[val] += 1
       
        buckets = [[] for _ in range(len(nums) + 1)]

        for key in counts:
            buckets[counts[key]].append(key)

        answer = []
        for buck in reversed(buckets):
            for val in buck:
                answer.append(val)
                if len(answer) == k:
                    return answer
        

    

        