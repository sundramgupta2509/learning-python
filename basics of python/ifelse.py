# Entering age for voting and driving

age = int( input("enter  the  no : "))
print(type(age))
print()   # int
if(age>=18):
    print("can vote and drive")  
    print()
else:
    print(" cannot vote and drive ")
    print()


#  different    color for traffic

light = str(input("Color of light visible: "))

if(light=="red"):
    print("STOP")
    print()
elif (light=="green"):
    print("GO")
    print()
elif(light=="yellow"):
    print("WAIT") 
    print() 

number = int(input("ENTER THE NUMBER : "))

if(number>=5):
    print("Number is greater than 5")
    print()
elif(number>=100):
    print("Number is greater than 100")
    print()
else:
    print("THE NUMBER IS LESS THAN 5 AND 100 BOTH.")  

marks=float(input("ENTER THE MARKS OBTAINED: "))

if(marks>=90 and marks<=100):
    print("Grade = 'A'")
    print()

elif(marks>=80 and marks<90):
    print("Grade = 'B'")
    print()

elif(marks>=70 and marks<80):
    print("Grade = 'C'")
    print()

else:
    print("Grade = 'D'")
    print()

# Nesting

Age=int(input("Enter the age :"))

if(Age>=18):
    if(Age<=80):
       print("can drive")
    else:
        print("Cannot drive")
else:
    print("Strictly prohibited to drive")

# To check the number whether it is ODD or EVEN.

number=int(input("ENTER THE NUMBER: "))

if(number%2==0):
    print("Even")
else:
    print("ODD")

# Greatest of three numbers.

a = float(input("enter first number: "))
b = float(input("enter second number: "))
c = float(input("enter third value: "))

if(a>b and a>=c):
    print("First number is largest.")
elif(b>=a and b>=c):
    print("Second number is largest.")
else:
    print("Third number is largest.")

