#method1
n=int(input("no.:"))
sum=0
i=1
while i<=n :
    sum+=i
    i+=1
    
print("total sum =",sum)

#method2
n=int(input("no.:"))
sum=0
for i in range (1,n+1):
    sum+=i
print("total sum=",sum)
