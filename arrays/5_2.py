# number stored in a array increase it by one. 

def increase(arr):
    carry = 1
    arr.reverse()
    for i in range(len(arr)):
        num = arr[i]
        sum = num+carry
        carry = sum//10
        arr[i] = sum%10
        if carry==0:
            arr.reverse()
            return arr
    if carry!=0:
        arr.append(carry)
        arr.reverse()
    return arr
arr = [9,1]
print(increase(arr))