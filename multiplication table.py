#method1
n=int(input("multipliction no."))
i=0
print("multiplication table of",n,":")
while i<=10 :

    print(n*i)
    i+=1

#method2

n=int(input("multiplication no. :"))
print("multiplication table of",n,":")
for i in range (1,11):
    print(n*i)