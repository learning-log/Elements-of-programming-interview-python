

def Plin_possible(s):
    if len(s) == 0:
        return True
    arr = [0]*26
    # total_char = len(s)
    for c in s:
        arr[ord(c)-ord("a")] +=1
    flag = 0
    odd_cahr = ""
    for idx in range(len(arr)):
        i = arr[idx]
        if i%2!=0:
            flag+=1
            odd_cahr = chr(idx+ord("a"))
    palin_st = ""
    if flag<=1:
        while 
    st = 0
    end = len(s)-1
    return flag<=1

print(Plin_possible("aabbccdd"))