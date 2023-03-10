#Fizz Buzz Program


def FizzBuzz(num):
    if((num % 5 == 0) and (num % 3 == 0)):
        return True

def Fizz(num):
    if(num % 3 == 0):
        return True

def Buzz(num):
    if(num % 5 == 0):
        return True

def main():
    #number to test against
    i = 1

    #While loop to go through numbers 1 - 100
    while(i <= 100):
        #if our number is divisible by both 3 and 5 it will print fizzbuzz
        if(FizzBuzz(i)):
            print("FizzBuzz")

        #if it is divisible by 3 it will print Fizz
        elif(Fizz(i)):
            print("Fizz")
    
        #if it is divisible by 5 it will print Buzz
        elif(Buzz(i)):
            print("Buzz")

        #if it is not divisible by anything just print the number
        else:
            print(i)

        #increment the number
        i += 1

main()

