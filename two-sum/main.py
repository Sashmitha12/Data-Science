n=int(input())
l=list(map(int,input().split()))
target=int(input())
for i in range(n):
    for j in range(i+1,n):
        if l[i]+l[j] == target:
            print(i ,",",i+1)
    