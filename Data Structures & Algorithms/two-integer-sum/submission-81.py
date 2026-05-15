class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        


        nums_map = {}

         
         

        for index, value in enumerate(nums):
            difference = target - value
            if (nums_map.get(difference) is not None):
                indice = [nums_map.get(difference), index]
                return indice
                 
            else:
                nums_map[value] = index


        
        