def RelationalOperator(a, b): 
    if a != b :
        if a>b :
            return ">"
        else :
            return "<"
    else :
        return "="
    
n = list(map(int, input().rstrip().split()))
for i in range(0,n[0]):
    a = list(map(int, input().rstrip().split()))
    print(RelationalOperator(a[0], a[1]))

