def check(n, i=2):
    if(n==i):
        return 0
    else:
        if n%i == 0:
            return 1
        else:
            return check(n, i+1)

if check(11)==0:
    print("Prime")
else:
    print("Not Prime")