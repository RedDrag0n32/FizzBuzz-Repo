#Fizz Buzz Program

#number to test against
i = 1

#While loop to go through numbers 1 - 100
while(i <= 100):
    #if our number is divisible by both 3 and 5 it will print fizzbuzz
    if((i % 5 == 0) and (i % 3 == 0)):
        print("FizzBuzz")

    #if it is divisible by 3 it will print Fizz
    elif(i % 3 == 0):
        print("Fizz")
    
    #if it is divisible by 5 it will print Buzz
    elif(i % 5 == 0):
        print("Buzz")

    #if it is not divisible by anything just print the number
    else:
        print(i)

    #increment the number
    i += 1
        

