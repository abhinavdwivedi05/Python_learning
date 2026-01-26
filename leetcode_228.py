class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n=len(nums)
        x=0
        if n==0:
            return []
        prev=nums[0]
        sol=[]
        for i in range(1,n):
            if nums[i]-1==prev:
                x+=1
                prev=nums[i]
            else:
                if x:
                    sol.append(f"{nums[i-x-1]}->{nums[i-1]}")
                else:
                    sol.append(f"{nums[i-1]}")
                x=0
                prev=nums[i]
        if x:
            sol.append(f"{nums[n-x-1]}->{nums[n-1]}")
        else:
            sol.append(f"{nums[-1]}")
        return sol