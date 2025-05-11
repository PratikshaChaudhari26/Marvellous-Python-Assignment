#Write a Program Which display first 10 even numbers 

def even(value):   
   for i in range(1,2*value+1) : 
      if i % 2 == 0 :
         print(i)
      i = i +1
even(10)


