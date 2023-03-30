import math
import logging
logging.basicConfig(filename='calculator.log',format='%(asctime)s %(levelname)-8s %(message)s', encoding='utf-8',datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)

def factorial(number):
    ans = 1
    for i in range(2,number+1):
        ans = i*ans
    return ans

def power(base,exponent):
    try:
        return math.pow(base,exponent)
    except Exception as e:
        logging.error(e)
        return('some error occured, please try again')

def squareroot(number):
    try:
        return math.sqrt(number)
    except Exception as e:
        logging.error(e)
        return('some error occured, please try again')

def naturallog(number):
    try:
        return math.log(number)
    except Exception as e:
        logging.error(e)
        return('some error occured, please try again')

def startcalculator(): 
    input("Press Enter to continue...")
    print('Welcome User')
    while True:
        print('Please Input option of your choice')
        print('-----------------********----------------')
        print('1.Square root\n2.factorial\n3.log\n4.power\n5.exit')
        try:
            inputnumber = int(input())
        except Exception as e:
            logging.error(e)
            print('enter number from the above list only.')
            continue
        logging.debug('Option pressed by user:{0}'.format(inputnumber))

        if inputnumber > 5 or inputnumber == 0:
            print('enter number from the above list only')
            continue 


        if inputnumber == 5:
            break
        if inputnumber != 4:
            print('enter number')
            try:
                no = float(input())
            except Exception as e:
                print('please enter no only')
                logging.error(e)
                continue

        if inputnumber == 4:          
            try:
                print('enter base')
                base = float(input())
                print('enter exponent')
                exponent = float(input())
            except Exception as e:
                print('enter no only')
                logging.error(e)
                continue


        if inputnumber == 1:               
            logging.info('[Square Root] - {0}'.format(no))
            result = squareroot(no)
            logging.info('[RESULT - Square Root] - {0}'.format(result))
            print('square root of given no is {0}'.format(result))

        elif inputnumber == 2:
            i = int(no)
            logging.info('[Factorial] - {0}'.format(i))
            result = factorial(i)
            logging.info('[RESULT - Factorial] - {0}'.format(result))
            print('factorial for given no is {0}'.format(result))

        elif inputnumber == 3:
            logging.info('[Natural Log] - {0}'.format(no))
            result = naturallog(no)
            logging.info('[RESULT - Natural Log] - {0}'.format(result))
            print('log of given no is {0}'.format(result))

        elif inputnumber == 4:
            logging.info('[Power] - {0} raised to {1}'.format(base,exponent))
            result = power(base,exponent)
            logging.info('[RESULT- Power] - {0}'.format(result))
            print('base to the power exponent with given values is {0}'.format(result))
            
        else:
            print('please select proper option')

if __name__ == "__main__":
    startcalculator()