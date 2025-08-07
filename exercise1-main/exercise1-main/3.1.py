while True:
    x = input("Which one do u want to do? (sum, difference, multiple, divide)")
    y = float(input("Number 1 :"))
    z = float(input("Number 2 :"))
    if x.lower() == "sum":
        print(y+z)
        break
    elif x.lower() == "difference":
        print(y-z)
        break
    elif x.lower() == "multiple":
        print(y*z)
        break
    elif x.lower() == "divide":
        print(y/z)
        break
    else :
        print("wrong action type Bro! Check it AGAIN.")