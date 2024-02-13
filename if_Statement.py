nambari=int(input("Enter Number:"))
if nambari%2==0 :
    print(f"{nambari} is an even number")
else:
    print(f"{nambari} is an odd number")

Age=int(input("Please enter your age:"))
if Age>=18:
    print("You can now proceed to voting")
else:
    print("You are not qualified to vote")

Math=int(input("Mathematics score:"))
Eng=int(input("English score:"))
Kisw=int(input("Kiswahili score:"))
Average=(Math+Eng+Kisw)/3
if Average>=80:
    print("Grade:A")
elif Average>=70:
    print("Grade:B")
elif Average>=60:
    print("Grade:C")
elif Average>=50:
    print("Grade:D")
else:
    print("Grade:E")