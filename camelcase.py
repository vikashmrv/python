def convert(a): 
    if(len(a) == 0): 
        return
    s1 ='' 
    s1+=a[0].upper() 
    for i in range(1, len(a) - 1): 
        if(a[i] ==' '): 
            s1+=a[i + 1].upper() 
            i+=1
        elif(a[i - 1]!=' '): 
            s1+=a[i]  
    print(s1)      
def main(): 
    s =input()
    convert(s)   
if __name__=="__main__": 
    main()
