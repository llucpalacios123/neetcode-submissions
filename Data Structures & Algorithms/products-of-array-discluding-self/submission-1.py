class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lista_final = [1] * len(nums)

        product = nums[0]

        for i in range(1, len(nums)):
            lista_final[i] *= product
            product *= nums[i]
        
        product = nums[len(nums)-1]
        for i in range(len(nums)-2, -1, -1):
            lista_final[i] *= product
            product *= nums[i]
        
        return lista_final