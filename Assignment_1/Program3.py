#write a program which accepts two number and return addition of those two number


def add(Value1,Value2):
    result = 0
    result = int(Value1) + int(Value2)

    return result



def main():

    print("Enter First Number :")
    No1 = input()

    print("Enter Second Number : ")
    No2 = input()

    Ans = add(No1,No2)

    print("Addition of two number is: ",Ans)


if __name__ == "__main__":
    main()        