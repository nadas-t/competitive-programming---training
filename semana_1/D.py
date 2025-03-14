answer=[]
compare=["T","i","m","u","r"]
compare.sort()
test_cases=int(input())
for i in range(test_cases):
    len=int(input())
    s=input()
    list(s).sort()
    if(len!=5):
        answer.append("NO")
    else:
        a=set(compare)
        b=set(s)
        if a == b:
            answer.append("YES")
        else:
            answer.append("NO")
for i in range(test_cases):
    print(answer[i])