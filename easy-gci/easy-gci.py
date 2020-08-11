import math
import sys
while True:

    o = input('Please input n: ')
    if o:
        if o.isdigit():
            n = int(o)
            break
    else:
        print("Please provide a non decimal number and do not input any letters")

if n == 1:
    print('The number of divisors is 1')
    sys.exit(0)

if n == 2 or n == 3:
    print('The number of divisors is 2')
    sys.exit(0)

if n == 4:
    print('The number of divisors is 3')
    sys.exit(0)
#Check if the number is more than 0 and less than or equal to 1000000
if n > 0 and n <= 1000000:
    s = round(math.sqrt(n)) + 1
    divisors = 0
    for divisor in range(1,s):
        if n % divisor == 0:
            divisors += 1
    divisors *= 2
    str_divisors = str(divisors )
    print('Number of divisors: ' + str_divisors)

else:
    print("Please provide a number which is more than 0 and less than or equal to 1000000")
    exit

