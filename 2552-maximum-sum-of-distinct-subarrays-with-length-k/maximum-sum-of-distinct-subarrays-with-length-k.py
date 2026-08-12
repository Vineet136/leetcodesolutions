class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        n = len(nums)
        sumi = 0
        maxi = 0
        seen = set()

        while j < n:

            # Duplicate found
            while nums[j] in seen:
                seen.remove(nums[i])
                sumi -= nums[i]
                i += 1

            # Add current element
            seen.add(nums[j])
            sumi += nums[j]

            # Window has k distinct elements
            if j - i + 1 == k:
                maxi = max(maxi, sumi)

                seen.remove(nums[i])
                sumi -= nums[i]
                i += 1

            j += 1

        return maxi
        