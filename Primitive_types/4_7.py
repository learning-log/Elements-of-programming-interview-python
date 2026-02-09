
def poww(x,y):
    if y==0:
        return 1
    elif y%2==1:
        y_2 = poww(x,y//2)
        return y_2*y_2 * x
    else:
        y_2 = poww(x,y//2)
        return y_2*y_2
print(poww(3,5))