def findMaxSum( arr):
        # code here
        
    def rec(arr,i):
        if i>=len(arr):
            return 0
        print(i)
        a = rec(arr,i+2)+arr[i]
        b = rec(arr,i+1)
        return max(a,b)
        
    ans = rec(arr,0)
    return ans
arr = [1,2,3,1]
print(findMaxSum(arr))