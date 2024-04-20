class Solution(object):
    # Leetcode No.75 Sort Colors
    #Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
    #We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
    #You must solve this problem without using the library's sort function.
       #My Solution: Consider two varaibles that keep track of how many zero and ones in the list.
    def sortColors(self, nums):
        Ein=0
        Zero=0
        for i in range(len(nums)):
            if nums[i]==0: Zero+=1
            if nums[i]==1: Ein+=1
        for i in range(len(nums)):
            if i<Zero: 
                nums[i]=0
            elif i<Zero+Ein:
                nums[i]=1
            else:
                nums[i]=2
        return(nums)
