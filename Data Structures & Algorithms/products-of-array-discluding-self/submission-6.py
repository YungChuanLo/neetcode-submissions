class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = [1] * len(nums)
        for i in range(1, len(nums)):
            
            left_product[i] = nums[i - 1] * left_product[i - 1]

            
        
        right_product = [1] * len(nums)
        for i in reversed(range(0, len(nums) - 1)):
            right_product[i] = nums[i + 1] * right_product[i + 1]

        for index, value in enumerate(nums):
            nums[index] = right_product[index] * left_product[index]


        return nums