try:
    number = int(input("Enter a number: "))
    print(number)
    x = 10/0
except ZeroDivisionError as err:
    print(err)

except ValueError:
    print("Invalid Input")