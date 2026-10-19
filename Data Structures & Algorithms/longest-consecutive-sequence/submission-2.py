class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        seen = set(nums)

        count = 0
        

        for i in nums:
            act_count = 1
            if  i-1 not in seen: 
                
                nextval = i+1

                while nextval in seen: 
                    act_count += 1
                    nextval += 1
                
                if act_count > count: 
                    count = act_count

        return count 

