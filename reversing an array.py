arr=[2,55,4,35,3]

left=0
n=len(arr)
right=n-1

print(left, right)

while left<right:
    arr[left],arr[right] = arr[right],arr[left]

    left +=1
    right -=1
    


print("ARRAY:" ,arr)