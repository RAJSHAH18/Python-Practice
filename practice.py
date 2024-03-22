n=int(input())
c=0
i=1
for i in range (1,n+1):
    if n%i==0 and n/i==i:
        c+=1
if c>0:
    print(True)
else:
    print(False)



