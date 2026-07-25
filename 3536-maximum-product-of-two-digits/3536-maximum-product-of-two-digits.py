class Solution:
    def maxProduct(self, n: int) -> int:
        arr=[]
        while n>0:
            arr.append(n%10)

            n=n//10

        arr.sort()
        arr=arr[::-1]
        k=1
        for i in range(0,2) :
            k=k*arr[i]

        return k