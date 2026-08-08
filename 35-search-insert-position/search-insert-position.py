class Solution:
    def searchInsert(self, arr: List[int], target: int) -> int:
        def ip(arr):
            n=len(arr)
            low=0
            high=n-1
            while(low<=high):
                mid=low+(high-low)//2
                if arr[mid]==target:
                    return mid
                elif(arr[mid]>=target):
                    high=mid-1
                else:
                    low=mid+1
            return low
        ans=ip(arr)
        return ans
        