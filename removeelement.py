class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # k incremnet we see non 2 value 
        # k starts from a[0] to end 
        k=0
        for i in range(len(nums)):
            #if we see 2 then ignore 
            # not 2 then val swap 
            #partion of quicksort all values of nums that are not val and putting them in the array 
            if nums[i] != val:
                nums[k]=nums[i]
                k+=1
        return k