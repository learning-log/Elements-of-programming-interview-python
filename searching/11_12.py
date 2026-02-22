

def find_first_set_bit(n):
    #1001 for this 0001 will be the answer
    return n & ~(n-1)

def find_the_duplicate(arr):
    ans = 0
    idx = 0
    for i in arr:
        ans= ans ^ i
        ans = ans ^ idx
        idx += 1
    # prin
    first_set_bit = find_first_set_bit(ans) 
    idx = 0
    for i in arr:
        if i & first_set_bit:
            ans = ans ^ i
        if idx & first_set_bit:
            ans = ans ^ idx
        idx += 1
    print(ans)
    for i in arr:
        if ans == i:
            return ans
    return -1

print(find_the_duplicate([0,1,2,4,5,6,7,7,8]))

