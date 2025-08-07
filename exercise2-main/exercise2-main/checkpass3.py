
def check_pass(l): 
    cap = 0 # to check if its included capital letters
    sm = 0 # for small letters 
    sym = 0 # to find out if it has symbols or any number
    names = [] # i want to add names to a list to use it later.
    for i in l :
        if len(i[1]) >= 8:
            for j in i[1]:
                if "A" <= j <= "Z" :
                    cap += 1
                elif "a" <= j <= "z" :
                    sm += 1
                else :
                    sym += 1
            if cap > 0 and sm > 0 and sym > 0 :
                names.append(i[0])
    return names

l = [("Melika","mLk_A65.2"),("Melina","Meliii"),("Feri","feri_"),("Amir","Amamm_eoeo"),("Riri","Riii36@<")]

a = check_pass(l)
print(a)