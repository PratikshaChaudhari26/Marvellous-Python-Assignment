#Write a Program which accepts no from user check whether number is positive or negative or zero
def  PosiveNUm():
    
    print("Enter First No : ")
    No = int(input())

    if (No > 0 ):
        print("Positive")

    elif(No < 0):
        print("Negative")

    else:
        print("zero")    
           

PosiveNUm()