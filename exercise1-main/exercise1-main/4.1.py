while True:
    x = input("which one do you want to enter?( C for celsius F for farenheit: )")

    if x.lower() == "c":
        c = float(input("enter Celcius: "))
        f = (1.8*c)+32
        print(f"{c}c is {f}f ")
        break
    elif x.lower() == "f":
        f = float(input("enter Farenheit: "))
        c = (f-32)/1.8
        print(f"{f}f is {c}c ")
        break
    else :
        print("wrong entry!")