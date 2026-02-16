# convert arr of string using these rules: replace a's with dd and delete b's.

def converter(arr,idx):

    total_len = 0
    for i in range(idx,-1,-1):
        ch = arr[i]
        print(ch)

        if ch=="a":
            total_len +=2
        elif ch=="b":
            total_len -= 1
        else:
            total_len+=1
    final_idx = total_len
    print(final_idx)
    for i in range(idx,-1,-1):
        ch = arr[i]
        if ch=="a":
            arr[final_idx]="d"
            final_idx-=1
            arr[final_idx]="d"
            final_idx-=1
        elif ch=="b":
            print(ch)
        else:
            arr[final_idx] = ch
            final_idx-=1
    return arr
arr = ["a","b","a","c","","",""]

print(converter(arr,3))
