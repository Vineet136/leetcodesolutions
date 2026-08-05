class Solution:
    def findMin(self, nums: List[int]) -> int:
        def msa(nums):
            n=len(nums)
            low=0
            high=n-1
            min_ans=float('infinity')
            while(low<=high):
                mid=low+(high-low)//2
                if(nums[low]<=nums[mid]):
                    ###LEFT SORTED
                    min_ans=min(min_ans,nums[low])
                    # if nums[low]<min_ans:
                    #     min_ans=nums[low]
                    low=mid+1
                else:
                    min_ans=min(min_ans,nums[mid])
                    ###RIGHT SORTED
                    # if nums[mid]<=min_ans:
                    #     min_ans=nums[mid]
                    high=mid-1
            return min_ans
        ans=msa(nums)
        return ans
                
                    

                

        