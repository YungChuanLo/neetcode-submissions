class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        remaining = set(nums)
        longest_length = 0
        print(remaining)
        for i in nums:
            print(i)

            remaining.discard(i)
            current_length = 1
            up = 1
            down = 1
            while (i + up) in remaining:
                
                current_length += 1
                remaining.remove(i + up)
                up += 1
            while (i - down) in remaining:
                current_length += 1
                remaining.remove(i - down)
                down += 1
            if (current_length > longest_length):
                longest_length = current_length
        return longest_length
                
            
            
            