print ("Welcome to my shoy.")
print("\nBiskit Section.\t\tNamkin Section")
print("\n1.parlay = 5Rs\t\t5.Motalal=100Rs\n2.bitania = 10Rs\t6.Akshat Namkines=2000Rs\n3.gooday = 20Rs\n4.crackjeck = 30Rs")

first_b=int(input("\nwhich biskit/namkin do you want.   Enter the serial No of biskit."))
a=int(input("how many do you want"))

if(first_b==1):
    first_b=5
elif(first_b==2):
    first_b=10
elif(first_b==3):
    first_b=20
elif(first_b==4):
    first_b=30
elif(first_b==5):
    first_b=100
elif(first_b==6):
    first_b=2000    
else:
    print("You have not entered any thing.\nPlease sujest how can we improve our survice.")
    print("\n1.Program logic.\n2.presentation.\n3.charactor.\n4.'Anotherissue.")
    su=int(input("Input the majre problem you face from bouve problems. Wrisht"))
    if(su==1):
        print("we will try to improve Program logic")
    elif(su==2):
        print("we will try to improve presentation")
    elif(su==1):
        print("we will try to improve charactor")
    else:
        print("we will surefully try to improve our program.")
    first_b=int(first_b)
   
first_b*=a

yes=bool(input("do you want more\nif not click enter"))

while(yes==1):
    print("1.parlay = 5Rs\t5.Motalal=100Rs\n2.bitania = 10Rs\t6.Akshat Namkines=2000Rs\n3.gooday = 20Rs\n4.crackjeck = 30Rs")
    second_b=int(input("\nwhich biskit do you want now. Ehter the ser.no"))
    a=int(input("how many do you want"))
    if(second_b==1):
        second_b=5
    elif(second_b==2):
        second_b=10
    elif(second_b==3):
        second_b=20
    elif(second_b==5):
         second_b=100
    elif(second_b==6):
         second_b=2000    
    else:
        second_b=30

    second_b*=a
    first_b+=second_b
    print("till now your Totle is = ",first_b,"Rs")
    yes=bool(input("do you want more\nif not click enter"))
    if(yes==0):
        break

print("------------------------")
print ("thankyu for shoping.")
print("\nGrandTotle = ",first_b,"Rs/-")

a=input("enter to exit")









