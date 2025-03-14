def eh_impar(x):
    if(x%2==0):
        return False
    else:
        return True


test_cases=int(input())
answer=[]
for i in range(test_cases):
    numb_coluns=int(input())
    height=list(map(int,input().split()))
    impar=True
    par=True
    for numero in height:
        if eh_impar(numero):
            par=False
        else:
            impar=False
    if(par==False and impar==False):
        answer.append("NO")
    else:
        answer.append("YES")

for i in answer:
    print(i)