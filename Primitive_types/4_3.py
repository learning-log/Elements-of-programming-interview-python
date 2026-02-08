#Reverse Bits

def swap(n,i,j):

    if (n>>i)&1 == (n>>j)&1:
        bitMask = (1<<i) | (1<<j)
        n = n ^ bitMask
    return n


def reverse_bit(n):
    ans = 0
    i = 0
    j = 63
    while i<32:
        ans = swap(n,i,j)
        i +=1
        j-=1

    return ans

# lookup table solution

print(swap(5,0,3))
print(reverse_bit(6))

