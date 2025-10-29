name=input("what's your name?->")
place=input("where are you from->?")
MoNo=int(input("enter your number->"))
country=input("which country you went?->")


visit=input("where do you want to visit?-> ")
residence=input("where are you staying here")


print("Welcome to",country,"MR",name)
print("Oo... you are from",place,"nice place")
w=input("do you have visa?->?")
if (w=="yes"):
    print("great")

else:
    print("why do't have visa?")
    reason=input("what's the reason don't have visa?->")
    print("MR",name,":",reason ,"sorry for that")
    print("ME:","it's okay")

age=int(input("enter your age->"))
if(60>age>=18 ):
    print("if you want to drive or drink then you can drive as well as drink")



else:
    print("if you want to drive or drink then you cann't do" )

print("nice place",visit)
print("but will be costly")


y=input("would you like to go?->")


if(y=="yes"): 
    print("okay ")

else:
    print("right decision")
    print("YOU CAN GO in cheap cities, if you want to")

r=input("would you like to go in cheaper cities?->?")


if(r=="yes"):
    print("okay") 
    w=input("where will you want to go")
    print("MR",name,":can we go ?->")
    print("me:","ofcourse")
    print("nice city ",w<"you are selected")
else:
    print("not a problem")



f=input("would you like to eat?->")    

if (f=="yes"):
    s=input("what do you want to eat?->")
    print("wow , nice dish", s)

else:
    print("no problem")
