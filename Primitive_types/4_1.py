# computing the parity of a word
# Brute force
def parity(n):
    ans = 0
    while(n):
        ans += (n&1)
        n = n>>1
    return ans%2==1

#optimized:

def parity_optimized(n):
    ans = 0
    while(n):
        ans ^= 1
        n = n&(n-1)
    return ans
# optimized using look up table.
# to be done.

print(parity_optimized(11))