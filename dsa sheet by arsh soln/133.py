def printNge(arr):
    for i in range(len(arr)):
        next=-1
        for j in range(i+1,len(arr)):
            if arr[i]<arr[j]:
                next=arr[j]
                break
        print(str(arr[i])+ "--"+str(next))

arr=[11,13,21,3]
printNge(arr)