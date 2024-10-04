array1 = [64,34,25,12,22,11,90]
n = len(array1)
for i in range(0,n):
    for j in range(i+1,n):
        if(array1[i]>array1[j]):
            temp = array1[i]
            array1[i]= array1[i]
            array1[j]= temp
print(array1)
