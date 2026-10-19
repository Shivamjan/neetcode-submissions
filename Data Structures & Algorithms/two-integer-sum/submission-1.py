class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}  # Map to store: { number: index }

        for i in range(len(nums)):
            current_num = nums[i]
            complement = target - current_num

            # Check if the complement we need is already in our dictionary keys
            if complement in diff:
                # Return the current index and the index of the complement
                return [diff[complement], i]

            # Store the current number and its index for future matches
            diff[current_num] = i
        
        return []
