
def good_array(soma,len):
    if(soma/len==1):
        return True
    else:
        return False


test_cases=int(input())
answer=[]
for i in range(test_cases):
    len=int(input())
    user_input=list(map(int,input().split()))
    soma=sum(user_input)

    if good_array(soma,len):
        m=0
    else:
        if(soma<len):
            m=1
        else:
            m=soma-len
    answer.append(m)
for i in answer:
    print(i)
