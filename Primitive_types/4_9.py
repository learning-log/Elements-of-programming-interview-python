import math


def checkPalin(num):
    n = math.floor(math.log10(num)) + 1
    # print(n)
    mask = 10**(n-1)


    while n>0:
        print(n)
        if num//mask != num%10:
            return False
        num = num % mask
        num = num // 10
        mask = mask//100
        n = n-2

    return True


print(checkPalin(898898))