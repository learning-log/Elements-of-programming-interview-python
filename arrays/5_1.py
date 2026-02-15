

#quicksort algorithm

def swap(arr,a,b):
    c = arr[a]
    arr[a] = arr[b]
    arr[b] = c
def settle_around_pivot(arr,s,e):
    # [6,3,5,2,4] 
    rolling_idx = s
    small_idx = s
    while rolling_idx<e:
        if arr[rolling_idx]<arr[e]:
            swap(arr,small_idx,rolling_idx)
            small_idx+=1
        rolling_idx+=1
    swap(arr,rolling_idx,small_idx)
    # print(arr,small_idx)
    return small_idx
# print(settle_around_pivot([3,6,7,5,2,4],0,5))

        



    # return

def quick_sort(arr,s,e):
    if e<s:
        return
    else:
        # pivot = arr[e]
        pivot_position = settle_around_pivot(arr,s,e)
        quick_sort(arr,s,pivot_position-1)
        quick_sort(arr,pivot_position+1,e)



arr = [5,4,3,6,7,8,4]
quick_sort(arr,0,6)
print(arr)

