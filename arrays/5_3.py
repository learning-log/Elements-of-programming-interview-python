# multiply two arbitrary precision number which are stored in array.
 

def increase(arr,carry):
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
def multiply(a,b):
    ans = []
    ab_posi = 0
    a.reverse()
    b.reverse()
    
    for num1 in a:
        re_posi = 0
        carry1 = 0
        carry2 = 0
        for num2 in b:
            mul = num1*num2 + carry1
            carry1 = mul//10
            mul = mul%10
            if (ab_posi+re_posi)>=len(ans):
                n_mul = mul+carry2
                carry2 = n_mul//10
                print(n_mul)
                ans.append(n_mul)
            else:
                n_mul = mul+carry2+ans[ab_posi+re_posi]
                carry2 = n_mul//10
                n_mul = n_mul%10
                ans[ab_posi+re_posi] =n_mul
            re_posi += 1 
        
        if carry1 or carry2:
            if (ab_posi+re_posi)>=len(ans):
                ans.append(carry2+carry1)
                print(carry2+carry1)
            else:
                n_mul = carry1+carry2+ans[ab_posi+re_posi]
                ans[ab_posi+re_posi] = n_mul
        ab_posi +=1
    ans.reverse()
    return ans
arr = [9,1]
b = [2,1,2]
print(multiply(arr,b))