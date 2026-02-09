# reverse the digit of a given number.
def reve(n):
    ans = 0
    while n:
        digit = n%10
        # print(digit)
        ans = ans*10 + digit
        n = n//10
        # print(n)
    return ans
print(reve(867))