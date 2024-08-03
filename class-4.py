# even or odd number check program
a = int(input("Enter Any Number:"))

if a%2 == 0 :
    print("This is even number")

else :
    print("This is odd number")




# smallest number check program

a =int(input("Enter First Number a : "))
b =int(input("Enter Second Number b : "))
c =int(input("Enter Third Number c : "))
d =int(input("Enter Fourth Number d : "))
e =int(input("Enter Fifth Number e : "))

if a<b and a<c and a<d and a<e:
    print("a is smallest number")
elif b<a and b<c and b<d and b<e:
    print("b is smallest number")
elif c<a and c<b and c<d and c<e:
    print("c is smallest number")
elif d<a and d<b and d<c and d<e:
    print("d is smallest number")
else:
    print("e is smallest number")



# grading check program

a=int(input("Marks Ovtained in Bangla :"))
if a>100 or a<0:
    print("Invalid Input")
else:
    if a>=80:
        print("You have got A+")
    elif a>=70 and a<80:
        print("You have got A")
    elif a>=60 and a<70:
        print("You have got A-")
    elif a>=50 and a<60:
        print("You have got B")
    elif a>=40 and a<50:
        print("You have got C")
    elif a>=30 and a<40:
        print("You have got D")
    else:
        print("You have got F")