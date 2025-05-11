#Write a program which contain one function named as CHKnum().which accept one parameter as number. if number is even then it should display "even number" otherwise display "Odd number".EnvironmentError


def ChNum():
  
  print("Enter the number: ")
  No = int(input())

  if (No % 2 ==0):
    print("Even number")

  else:
    print("Odd number")   

ChNum()
