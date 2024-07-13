class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        for right in range(1,len(nums)):
        
            if nums[right] != nums[right - 1]:
                nums[left]=nums[right]
                left +=1
        return left 

    """here we took two pointers and placed each of them to the 2nd index of the array that means a[1] not a[0]
     then we are incrementing the right pointer and comparing it with the previous value of the array 
     if the values are different we are keeping it to the place of the left pointer 
     and incrementing the value of the left pointer 
     so now we will have only unique values of the array in the place of left pointer 
      youtube refrence = https://www.youtube.com/watch?v=DEJAZBq0FDA """
        