class Solution:
    def singleNonDuplicate(self, arr: List[int]) -> int:
        def single(arr):
            n=len(arr)
            low=0
            high=len(arr)-1
            if n==1:
                return arr[0]
            if arr[0]!=arr[1]:
                return arr[0]
            if arr[n-1]!=arr[n-2]:
                return arr[n-1]
            else:
                low=low+1
                high=high-1
                while(low<=high):
                    mid=low+(high-low)//2
                    if((mid%2==1) and arr[mid-1]==arr[mid] or (mid%2==0) and arr[mid]==arr[mid+1]):
                        low=mid+1
                    else:
                        high=mid-1
                return arr[low]
        ans=single(arr)
        return ans
                
        
            

            
      
        