marks=int(input("Enter Marks:"))

if marks>=80 and marks<=100 :
    print("You Have an A")
elif marks>=60 and marks<=79 :
    print("You Have a B")
elif marks>=40 and marks<=59 :
    print("You Have a C")
elif marks>=20 and marks<=39 :
    print("You Have a D")
elif marks>=0 and marks<=19 :
    print("You Have FAILED terribly")
else :
    print("WRONG INPUT")
