def c(x):
    if(x=="I"):
        return 1
    if(x=="V"):
        return 5
    if(x=="X"):
        return 10
    if(x=="P"):
        return 50
    if(x=="G"):
        return 100
    if(x=="R"):
        return 500
    if(x=="L"):
        return 1000
    return -1
def mrv(m):
    res=0
    p=0
    while(p<len(m)):
        l1=c(m[p])
        if(p+1<len(m)):
            l2=c(m[p+1])
            if(l1>=l2):
                res=res+l1
                p=p+1
            else:
                res=res+l2-l1
                p+=2
        else:
            res=res+l1
            p=p+1
    print(res)
n=input()
mrv(str(n))
