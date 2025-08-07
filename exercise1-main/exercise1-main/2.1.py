input("Please enter you bank account pin: ")
while True:
    print("Which action do you want to do? ")
    print("1.Transfer")
    print("2. Withdrawal")
    print("3. Balance Enquiry")
    x = int(input("Enter action number: "))
    if x == 1 :
        input("Please enter Destination card number: ")
        input("Please enter the amount: ")
        a = input("Do you want to continue? (y/n)")
        if a == "y":
            continue
        elif a == "n":
            break
    elif x == 2:
        input("Please enter the amount of cash you want: ")
        a = input("Do you want to continue? (y/n)")
        if a == "y":
            continue
        elif a == "n":
            break
    elif x == 3:
        print("Your balance amount is : **** ")
        a = input("Do you want to continue? (y/n)")
        if a == "y":
            continue
        elif a == "n":
            break
    else :
        continue
