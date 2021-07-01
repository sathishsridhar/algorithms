def mergeSort(arr):
    #When [1,2] is divided [1] cannot be divided more, hence > 1 check to stop recrusion.
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i=j=k=0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
        #Left over numbers are already arranged in their correct positions, hence added to main array.
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1




if __name__ == '__main__':
    arr = [5,7,3,21,9,33]
    mergeSort(arr)
    print(arr)
