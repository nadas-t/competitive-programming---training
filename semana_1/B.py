test_cases=int(input())
answer=[]

for i in range(test_cases):
    blank_space=0
    blank_space_new=0
    len=int(input())

    user_input=list(map(int,input().split()))
    for j in range(len):
        if(user_input[j]==0 ):
            blank_space_new+=1
            if(j==(len-1)):
                if(blank_space_new>blank_space):
                    blank_space=blank_space_new
        else:
            if(blank_space_new>blank_space):
                blank_space=blank_space_new
            blank_space_new=0
    answer.append(blank_space)
for i in range(test_cases):
    print(answer[i])


    




