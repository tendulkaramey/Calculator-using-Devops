import math
import logging
logging.basicConfig(filename='calculator.log',format='%(asctime)s %(levelname)-8s %(message)s', encoding='utf-8',datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)

def factorial(number):
    ans = 1
    for i in range(2,number+1):
        ans = i*ans
    return ans

def power(base,exponent):
    return math.pow(base,exponent)

def squareroot(number):
    return math.sqrt(number)

def naturallog(number):
    return math.log(number)

def startcalculator(): 
    input("Press Enter to continue...")
    print('Welcome User')
    while True:
        print('Select the option')
        print('-----------------********----------------')
        print('1.Square root\n2.factorial\n3.log\n4.power\n5.exit')
        inputnumber = int(input())
        if inputnumber == 5:
            break
        if inputnumber == 1:
            print('enter number')
            no = float(input())
            logging.info('[Square Root] - {0}'.format(no))
            result = squareroot(no)
            logging.info('[RESULT - Square Root] - {0}'.format(result))
            print('square root of given no is {0}'.format(result))
        elif inputnumber == 2:
            print('enter the no to find factorial')
            #check if no else error
            i = int(input())
            logging.info('[Factorial] - {0}'.format(i))
            result = factorial(i)
            logging.info('[RESULT - Factorial] - {0}'.format(result))
            print('factorial for given no is {0}'.format(result))
        elif inputnumber == 3:
            print('enter the no to find log')
            no = float(input())
            logging.info('[Natural Log] - {0}'.format(no))
            result = naturallog(no)
            logging.info('[RESULT - Natural Log] - {0}'.format(result))
            print('log of given no is {0}'.format(result))
        elif inputnumber == 4:
            print('enter base')
            base = float(input())
            print('enter exponent')
            exponent = float(input())
            logging.info('[Power] - {0} raised to {1}'.format(base,exponent))
            result = power(base,exponent)
            logging.info('[RESULT- Power] - {0}'.format(result))
            print('base to the power exponent with given values is {0}'.format(result))
        else:
            print('please select proper option')

if __name__ == "__main__":
    startcalculator()