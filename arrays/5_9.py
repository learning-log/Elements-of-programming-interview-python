# print all prime numbers.

def printAll(num):
    ans = [1]
    for i in range(2,num+1):
        flag = True
        for num in ans[1:]:
            if i%num==0:
                flag = False
                break
        if flag:
            ans.append(i)
    return ans
def seive(num):
    ans = [1]*(num+1)
    ans[1] = 1
    ans[0] = 0
    result = [1]
    for i in range(2,num+1):
        if ans[i]==1:
            result.append(i)
            for j in range(i*2,len(ans),i):
                ans[j] = 0
    return result
import time
start = time.time()
# print()
seive(190000)
end = time.time()
print(end - start)

start = time.time()
# print(seive(190))
printAll(190000)
end = time.time()
print("mine",end - start)


            
