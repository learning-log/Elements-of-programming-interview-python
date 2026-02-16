#  convert string to int

def stringToInt(st):
    ans = 0
    for c in st:
        num = ord(c) - ord("0")
        ans = ans*10 + num
    return ans
print(stringToInt("2343"))