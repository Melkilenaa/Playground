var1 = int(input("Enter a number: "))
if var1 % 2 == 0 and var1 % 3 == 0:
    print("FizzBuzz")
elif var1 % 2 == 0:
    print("Fizz")
elif var1 % 3 == 0:
    print("Buzz")
else:
    print("Not Applicable")
