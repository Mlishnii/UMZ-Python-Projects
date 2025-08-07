from threading import Timer
import random

def exam_numbers():
    tr = 0
    fa = 0
    for _ in range(5):
        x = "0101"
        bin_num = "".join(random.sample(x,4))
        print(bin_num)
        dec_num = int(bin_num,2)
        
        t = Timer(15, lambda: print("\nTime is Over Bro!"))
        t.start()
        dec = int(input("Please enter Decimal form: "))
        t.cancel()
        if dec_num == dec :
            print("YES!!!")
            tr += 1
        else:
            print("Wrong!")
            fa += 1
    return tr , fa
    


correct,wrong = exam_numbers()
print(f" correct answers : {correct} \n wrong answers: {wrong}")