d=int(input("input date."))
m=int(input("input month.in no."))
y=int(input("input year."))

a=b=0
asq=[0,3,0,3,2,3,2,3,3,2,3,2,3]
while(b<m):
    a+=asq[b]
    b+=1
    if(b>m):
        break
if(y%4==0):
    a=b=0
    asq=[0,3,1,3,2,3,2,3,3,2,3,2,3]
    while(b<m):
        a+=asq[b]
        b+=1
        if(b>m):
            break    


x=(y-1)%400
if(x<100):
    fi=x//4
    u=x+fi+a+d
elif(x<200):
    fi=(x-100)//4
    u=(x-100-fi)+2*fi+d+a+5
elif(x<300):
    fi=(x-200)//4
    u=(x-200-fi)+2*fi+d+a+3
elif(x<400):
    fi=(x-300)//4
    u=(x-300-fi)+2*fi+d+a+1
day=u%7

seq=['2 Monday','3 Tuesday','4 Wednesday','5 Thursday','6 Friday','7 Saturday','1 Sunday']
print(seq[day-1])
input("Enter to exit")



