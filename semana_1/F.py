dim_matriz=list(map(int,input().split()))
matriz=[]
modelo=["f","a","c","e"]
modelo.sort()
soma=0

for i in range (dim_matriz[0]):
    matriz.append(list(input()))

if (dim_matriz[0]<2 or dim_matriz[1]<2):
    True
else:
    for i in range(dim_matriz[1]-1):
        for j in range(dim_matriz[0]-1):
            compare=[]
            compare.extend([matriz[j][i],matriz[j+1][i],matriz[j][i+1],matriz[j+1][i+1]])
            compare.sort()
            a=set(compare)
            b=set(modelo)
            if a == b:
                soma+=1
print(soma)

            

