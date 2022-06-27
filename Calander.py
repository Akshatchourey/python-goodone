# Finding leap and century year.

year=int(input("enter the year"))
if(year%4==0):
    if(year%100==0):
        print(year,"is a centuary year")
        if(year%400==0):
            print("and a leap year")
    else:
        print(year,"is a leap year but not a century year")
else:
    print("year is not a leap year")


a = input("enter to exit")


