# remove the duplicates from the array which is sorted.

def remove_dps(arr):
    idx = 0
    for i in range(1,len(arr)):
        if arr[idx]!=arr[i]:
            idx += 1
            arr[idx] = arr[i]
    return arr[:idx+1]

arr = [1,3,4,5,5,5,6,6,7,9,9]
print(remove_dps(arr))
        