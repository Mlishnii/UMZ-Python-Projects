# why am i doin this? Dunno (why do u want this?!)
suspects = ["A", "B", "C", "D"]

l = [True] # just made a list to add it True/False Values /// 'a3' is always true
def var_change(a2 , b1, b2):
    """It gets the variables which i need to change their values,
    then it will make other variables with opposite values (what's happening =D)"""
    b3 = c2 = not a2
    l.extend([b3,c2,a2])
    
    d1 = not b1
    l.extend([d1, b1])

    d3 = not b2
    l.extend([b2, d3])

    return l


# a1 = True # acts like a placeHolder (makes no difference in main answer)
# c1 = not a1
# c3 = True # acts like a placeHolder (makes no difference in main answer)
# d2 = not c3
# l.extend([c3, d2, a1, c1]) # it has no effect, so i will delete them

for i in suspects:
    # just want to check them in order to see if all conditions are true or not
    if i == "A" :
        a2 = False
        b1 = True
        b2 = False
        var_change(a2, b1, b2)
        if l.count(True) == l.count(False) == 4 :
            print("'A' is thief.")
        l = [True]
    
    if i == "B" :
        a2 = True
        b1 = True
        b2 = True
        var_change(a2, b1, b2)
        if l.count(True) == l.count(False) == 4 :
            print("'B' is thief.")
        l = [True]
        
    if i == "C" :
        a2 = False
        b1 = True
        b2 = True
        var_change(a2, b1, b2)
        if l.count(True) == l.count(False) == 4 :
            print("'C' is thief.")
        l = [True]

    if i == "D" :
        a2 = False
        b1 = False
        b2 = True
        var_change(a2, b1, b2)
        if l.count(True) == l.count(False) == 4 :
            print("'D' is thief.")
        l = [True]
