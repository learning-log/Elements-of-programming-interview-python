# generate all the permutation of an array

def getP(arr):

    ans = [arr]
    idx = 0
    while idx < len(arr):
        swpidx = idx+1
        print(swpidx)
        tmp_ans = []
        while swpidx<len(arr):
            lenn = len(ans)
            # print(lenn)
            for j in range(lenn):
                tmp_arr = ans[j]
                new_arr = tmp_arr.copy()
                tmp = new_arr[idx]
                new_arr[idx] = new_arr[swpidx]
                new_arr[swpidx] = tmp
                tmp_ans.append(new_arr)
            swpidx+=1
        ans = ans + tmp_ans
        # print(ans)
        idx+=1
    print(ans)
arr = [1,2,3,4]
getP(arr)

                

