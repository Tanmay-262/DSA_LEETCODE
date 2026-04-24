class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        #OPTIMAL_APPROACH
        nums.sort()  # Step 1: sort array
        res = []

        for i in range(len(nums)):
            # Skip duplicate values for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            # Two pointer search
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for left
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for right
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers inward
                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1  # Need bigger sum
                else:
                    right -= 1  # Need smaller sum

        return res