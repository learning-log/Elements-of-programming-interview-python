# snake string print of string

def snakeString(s):

    ans = ""
    i = 1
    while i<len(s):
        ans += s[i]
        i+=4
    i=0
    while i<len(s):
        ans += s[i]
        i+=2
    i=3
    while i<len(s):
        ans += s[i]
        i+=4
    print(ans)
s = "hello world"
snakeString(s)