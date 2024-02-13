def lookpalindrome():
    n=0
    while n<20 :
        name=str(input("Input name"))
        if name== name[::-1]:
            print("Name is a palindrome")
        else:
            print("Not a palindrome")
        n=n+1
lookpalindrome()