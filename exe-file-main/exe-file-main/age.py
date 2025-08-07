#چون هدف این تکلیف ساختن exe بود، من دیگه برنامه رو پیچیده ش نکردم.
while True:
    x = int(input("Which one do you want to enter?\n1:Shamsi\n2:Miladi\n:"))
    if x == 2:
        year = int(input("Please enter year of your BirthDay:"))
        age = 2024-year
        if age >=100:
            print("you must be Dead BRO!")
        else:
            print(f"You have {age} years OLD!")
        a = input("Do u want to do it again?(y/n)")
        if "y" in a.lower():
            continue
        elif "n" in a.lower():
            break
    elif x == 1:
        year = int(input("Please enter year of your BirthDay:"))
        age = 1403-year
        if age>=100:
            print("you must be Dead BRO!")
        else:
            print(f"You have {age} years OLD!")
        a = input("Do u want to do it again?(y/n)")
        if "y" in a.lower():
            continue
        elif "n" in a.lower():
            break
    else :
        print("Wrong Entry!")
        continue


while True:
    pass