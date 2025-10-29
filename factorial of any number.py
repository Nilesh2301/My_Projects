#method1
n=int(input("no."))
factorial=1
for i in range(1,n+1):
    factorial*=i
print("factorial of ",n,"is",factorial)

#metho2
n=int(input("no."))
fact=1
i=1
while i<=n:
    fact*=i
    i+=1

print("factorial of",n,"is",fact) 