# find odd numbers from 1-100
start,end =1,100

for num in range (start,end +1):

    if num%2!=0:
        print(num, end= " ")



# a program to find the area of ​​3 triangles
def triangleArea(heighr,width):
    area = 0.5*(heighr*width)
    print("The area of triangle %0.2f" %area)

triangleArea(5,20)
triangleArea(2,25)
triangleArea(36,20)



# a program to find the sum of 4 numbers
num1 = float(input("Enter the first number a :"))
num2 = float(input("Enter the second number b :"))
num3 = float(input("Enter the third number c :"))
num4 = float(input("Enter the four number d :"))

def sumofFourNumber(a,b,c,d):
    total= a+b+c+d
    return total


result = sumofFourNumber(num1,num2,num3,num4)
print("The sum of four inputed values  : %0.2f " %result)