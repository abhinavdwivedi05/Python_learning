arr=[1,0,0,0,0,1,0,1]

days= int(input())
ans=[0,0,0,0,0,0,0,0]
for k in range(days):
    for i in range(len(arr)):
        if i==0:
            if arr[i+1]==0:
                ans[i]=0
            else:
                ans[i]=1
            continue
        if i==len(arr)-1:
            if arr[i-1]==0:
                ans[i]=0
            else:
                ans[i]=1
            continue 

        if arr[i-1]==arr[i+1]:
            ans[i]=0
        else:
            ans[i]=1

    arr = ans.copy()
    
    

print(ans)        

