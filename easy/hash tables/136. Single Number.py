class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = dict()
        for number in nums:
            if result.get(number):
                result.pop(number)
            else:
                result[number] = True
        return result.keys()
        

    def singe_number_extra(self, nums: list[int]) -> int:
        # extra task -- need to solve via O(1) memory
        nums.sort()

        while len(nums) > 1:
            if nums[0] == nums[1]:
                nums.pop(0)
                nums.pop(0)
            else:
                return nums[0]
        return nums[0]
    

    def best(self, nums: list[int]) -> int:
        accumulator = 0
        for num in nums:
            accumulator ^= num
        return accumulator



if __name__ == "__main__":
    numbers = [1, 2, 1, 3, 2]
    result = Solution().singleNumber(nums=numbers)
    print(result)

    numbers = [4, 2, 4, 3, 2]
    result = Solution().singe_number_extra(nums=numbers)
    print(result)

    numbers = [4, 2, 4, 3, 3]
    result = Solution().test(nums=numbers)
    print(result)