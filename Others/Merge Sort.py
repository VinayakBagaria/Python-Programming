def sort(arr):
    if len(arr)>1:
        q=int(len(arr)/2)

        Left=arr[:q]    # 0 to q-1
        Right=arr[q:]   # From q onwards

        sort(Left)
        sort(Right)

        i=0
        j=0
        k=0

        #To main array arr
        while i<len(Left) and j<len(Right):
            if(Left[i]<=Right[j]):
                arr[k]=Left[i]
                i=i+1
            else:
                arr[k]=Right[j]
                j=j+1
            k=k+1

        #Remaining elements in the array to be shifted
        while i<len(Left):
            arr[k]=Left[i]
            i=i+1
            k=k+1

        while j<len(Right):
            arr[k]=Right[j]
            j=j+1
            k=k+1

arr=[2,3,6,4,-1]
sort(arr)
print(arr)