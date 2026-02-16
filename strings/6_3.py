# excel column to int

def colToInt(a):
    ans = 0
    for c in a:
        num = ord(c) - ord("A")+1
        ans = ans*26 + num
    return ans

print(colToInt("D"))