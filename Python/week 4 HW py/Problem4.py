number = int(input("Enter a number: "))
if number < -100:
    print("Negative large")
elif number < 0:
    print("Negative small")
elif number == 0:
    print("Zero")
elif number <= 100:
    print("Positive small")
else:
    print("Positive large")