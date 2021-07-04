def getPivot(arr,low,high):
    pivot = arr[high]
    i = low - 1
    for j in range(low,high):
        if arr[j] < pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def quickSort(arr,low,high):
    if low < high:
        pi = getPivot(arr,low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)


if __name__=='__main__':
    arr = [24,32,5,7,93,60];
    quickSort(arr,0,len(arr)-1)
    print(arr)

'''
    [24,32,5,7,60,93]
[5,32,24,7] [60,93]
[5,7,24,32] [60,93]
[5,7,24,32,60,93]

'''

