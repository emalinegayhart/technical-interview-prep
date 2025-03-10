class Solution:
    def majorityElement(self, nums):
        majority_element = None
        count = 0

        for num in nums:
            if count == 0:
                majority_element = num
            count += (1 if num == majority_element else -1)

        return majority_element
    end