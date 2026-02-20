# buy and selling the stock only one buy and sell allowed

def get_profit1(arr):

    ans = 0
    mi = arr[0]
    for num in arr:
        ans = max(ans,num-mi)
        mi = min(mi,num)
    return ans


# 2 buy selling allowed at max.

# def get_profit2(arr):
