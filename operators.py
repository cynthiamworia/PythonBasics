# arithmetic operators
nambari = int(input("Enter your first number:"))
nambari2 = int(input("Enter your second number:"))
print(nambari + nambari2)
print(nambari - nambari2)
print(nambari * nambari2)
print(nambari / nambari2)
print(nambari % nambari2)
# comparison operators
nambari3 = int(input("Enter the third number:"))
nambari4 = int(input("Enter the fourth number:"))
print(f"{nambari3} is less than {nambari4} {nambari3<nambari4}")
print(f"{nambari3} is not equal to {nambari4} {nambari3!=nambari4}")
print(f"{nambari3} is equal to {nambari4} {nambari3==nambari4}")
print(f"{nambari3} is greater than {nambari4} {nambari3>nambari4}")
print(f"{nambari3} is greater than or equal to {nambari4} {nambari3>=nambari4}")
print(f"{nambari3} is less than or equal to {nambari4} {nambari3<=nambari4}")
nambari5=int(input("Enter the fifth number:"))
nambari6=int(input("Enter the sixth number:"))
print(f"both statements should be true: {nambari5==nambari6 and nambari5>nambari6}")
print(f"one statement should be true: {nambari5==nambari6 or nambari5>nambari6}")