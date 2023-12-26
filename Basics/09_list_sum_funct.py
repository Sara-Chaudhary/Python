def sum(num):
    total=0
    for x in num:
        total+=x
    return total

n=int(input())
l=[]
for i in range(n):
    a= int(input())
    l.append(a)

print(sum(l))
