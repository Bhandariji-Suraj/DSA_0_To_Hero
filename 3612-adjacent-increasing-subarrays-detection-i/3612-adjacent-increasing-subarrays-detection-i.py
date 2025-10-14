class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for s in range(n - 2 * k + 1):
            first = nums[s:s+k]
            second = nums[s+k : s+2*k]
            if all(first[i] < first[i+1] for i in range(k-1)):
                if all(second[i] < second[i+1] for i in range(k-1)):
                    return True
        return False