def print_buzz(numList):
    if not random_numList:
        print("Please input values into list")
    for num in numList:
        if(num % 3 == 0 and num % 5 == 0):
            print("FizzBuzz")
        else:
            if (num % 3 == 0):
                print("Fizz")
            elif (num % 5 == 0):
                print("Buzz")
            else:
                print("Number is neither divisible by 3 or 5")

random_numList = [5,3,11,19,21,5,10,12,30]

print_buzz(random_numList)
