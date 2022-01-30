class Solution():
    def twoSum(self, nums, target) -> list:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        self.indices = {}
        
        for i, ele in enumerate(nums):
            diff = target - ele
            if diff in self.indices.keys():
                return [self.indices[diff], i]
            self.indices[ele] = i
            

obj = Solution()
print(obj.twoSum([2,7,11,15], 9))