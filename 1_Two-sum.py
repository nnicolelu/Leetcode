class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # #Hint: Use a dictionary to solve the question. The keys of the dictionary will be the element in the nums list. The values will be the corresponding index. Iterate through the list using a for loop. During every iteration, compute the remaining value by using Target - currentElement. Check if the remaining value is a key in the dictionary. If it’s not, add element and index into the dictionary as a new pair and continue.
#def twoSum(nums, target):
    #for i in range(len(nums)):
        # if (target - nums[i] is in dict)
        #   print()
        #   return [dict{target - nums[i]}, i] 
        # 
        # dict[XXX] = ???
        dict = {}
        for i in range(len(nums)):
            if (target - nums[i] in dict):
                print(dict[target - nums[i]], i)
                return [dict[target - nums[i]], i]
            dict[nums[i]] = i


