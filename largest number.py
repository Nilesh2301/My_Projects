a=int(input("enter the first no."))
b=int(input("enter the second no."))
c=int(input("enter the third no."))

if(a>=b and a>=c):
    print("first no. is largest",a)

elif(b>=c):
    print("second no. is largest",b)

else:
    print("third no. is largest",c)
    
    
number=int(input("write no:")) 
remainder= number %7
if(remainder==0):
    print("multiple")

else:
    print("not a multiple")

