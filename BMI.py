weight=float(input("Enter your weight in kilograms"))
height=float(input("Enter your height in metres"))
bmi=weight/(height ** 2)

if bmi < 18.5 :
    category="You are underweight"
elif 18.5 <= bmi > 25 :
    category="You have Normal Weight"
#elif 18.5 <= bmi <25  :
 #   category="You are Narmal"
elif 25<= bmi <29.9 :
    category="You are Overweight"
else:
    category="Obesse"
print(f"Your BMI is {bmi:.2f} and your classification as Results is {category}")
