class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count=nums.count(0)
        nums[:]=[i for i in nums if i != 0]
        nums+=[0]*count

        return nums
        
solution = Solution()
print(solution.moveZeroes([0,1,0,3,12]))
print(solution.moveZeroes([0]))