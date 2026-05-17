a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a == b:

    if b == c:
        print("Equilateral")

    else:
        print("Isosceles")

else:

    if a == c:
        print("Isosceles")

    else:

        if b == c:
            print("Isosceles")

        else:
            print("Scalene")