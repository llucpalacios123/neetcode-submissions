class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        left = 0
        right = len(nums) -1
        k = left + 1
        lista_final = []

        while left < right:
            suma = nums[left] + nums[k] + nums[right]

            if suma == 0:
                lista_final.append([nums[left], nums[k], nums[right]])

                k += 1
                while k < right:
                    if nums[k-1] == nums[k]:
                        k += 1
                    else:
                        break

            elif suma < 0:
                k += 1
                while k < right:
                    if nums[k-1] == nums[k]:
                        k += 1
                    else:
                        break
            else: 
                right -= 1
                while right > k:
                    if nums[right+1] == nums[right]:
                        right -= 1
                    else:
                        break
            if k >= right:
                left += 1
                while left < right:
                    if nums[left-1] == nums[left]:
                        left += 1
                    else:
                        break
                k = left + 1
                right = len(nums) -1
        
        return lista_final
                
                
