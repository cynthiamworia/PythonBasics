Math = int(input("Mathematics score:"))
Eng = int(input("English score:"))
Kisw = int(input("Kiswahili score:"))
Average = (Math + Eng + Kisw) / 3
if 80 <= Average <= 100:
    print("Grade:A")
elif 70 <= Average <= 79:
    print("Grade:B")
elif 60 <= Average <= 69:
    print("Grade:C")
elif 50 <= Average <= 59:
    print("Grade:D")
elif Average>=0 and Average<=49:
    print("Grade:E")
else:
    print("You have entered the wrong values")

Weight=float(input("Enter your weight:"))
Height=float(input("Enter your height:"))
BMI=Weight/Height
if BMI>35:
    category=("Overweight")
elif BMI>25:
    category="Normal"
elif BMI<25:
    category="Underweight"
print(category)

