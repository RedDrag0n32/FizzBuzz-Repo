#Fizz Buzz Program


#Function for testing if it is divisible by both 5 and 3
#if it does the function will return true
def FizzBuzz(numberInputted):
    if((numberInputted % 5 == 0) and (numberInputted % 3 == 0)):
        return True

def FizzBuzz(num):
    if((num % 5 == 0) and (num % 3 == 0)):
        return True

#Function for testing if it is divisible by 5
#if it does the function will return true
def Fizz(numberInputted):
    if(numberInputted % 3 == 0):
        return True

#Function for testing if it is divisible by 3
#if it does the function will return true
def Buzz(numberInputted):
    if(numberInputted % 5 == 0):
        return True

def main():
    #number to test against
    number = 1

    #While loop to go through numbers 1 - 100
    while(number <= 100):
        #if our number is divisible by both 3 and 5 it will print fizzbuzz
        if(FizzBuzz(number)):
            print("FizzBuzz")

        #if it is divisible by 3 it will print Fizz
        elif(Fizz(number)):
            print("Fizz")
    
        #if it is divisible by 5 it will print Buzz
        elif(Buzz(number)):
            print("Buzz")

        #if it is not divisible by anything just print the number
        else:
            print(number)

        #increment the number
        number += 1

main()

