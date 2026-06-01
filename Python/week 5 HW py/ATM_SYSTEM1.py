balance = 1000
amounts = [50, 100, 200, 500]

while True:
    print("\n===== ATM MENU =====")
    print("1 - Show Balance")
    print("2 - Deposit")
    print("3 - Withdraw")
    print("0 - Exit")
    
    choice = input("Choose: ")
    if choice.isdigit():
            choice = int(choice)
    else:
            print ("Enter Numbers Only: ")
    match choice:

        case "1":
            print(f"Current Balance: {balance} SAR")

        case "2":
            while True:
                
                amount = int(input("Deposit (50,100,200,500) or 0 to cancel: "))

                if amount == 0:
                    break
                elif amount in amounts:
                    balance += amount
                    print(f"New Balance: {balance} SAR")
                    break
                else:
                    print("Invalid amount. Try again.")

        case "3":
            while True:
                amount = int(input("Withdraw (50,100,200,500) or 0 to cancel: "))

                if amount == 0:
                    break
                elif amount in amounts:
                    if amount <= balance:
                        balance -= amount
                        print(f"New Balance: {balance} SAR")
                    else:
                        print("Insufficient funds")
                    break
                else:
                    print("Invalid amount. Try again.")

        case "0":
            print("Goodbye!")
            break

        case _:
            print("Invalid menu choice")



