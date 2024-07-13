class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """here we take two pointers left and right respectively and we compare them in order to compare the values of the numbers in the array
            we initiate both the pointers from the zeroth index of the array"""
        l=0
        r=0
        while r<len(nums):
            #the right one will be incremented upto the length of the array 
            count = 1
            #inorder to count the repeatation of the same number in this sorted array 
                #count is 1 when both adjacent number match 
            while r+1 < len(nums) and nums[r]==nums[r+1]:
                    #comparing the adjcent right element of the array upto length of the array 
                r +=1
                count +=1
                    #incrementing r and count 
                    #here if the count = 2 then we can accept the repeation 
                    #if the count is 3 then we have to take only two elements of them which is minimum\
            for i in range(min(2,count)):
                nums[l]= nums[r]
                l +=1
            r +=1
        return l

