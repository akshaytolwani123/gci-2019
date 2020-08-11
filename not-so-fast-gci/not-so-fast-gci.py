#Not so fast task gci
#By:- Akshay Tolwani
#Username for gici:- akshayprogrammer

#Loop to check if the input from user is valid
while True:
    o = input('Please input n: ')
    if o:
        if o.isdigit():
            n = int(o)
            break
#Check if the number is more than 0 and less than or equal to 1024
if n > 0 and n <= 1024:
    answer = pow(2,n)
    print(answer)
else:
    print("Please provide a number which is more than 0 and less than or equal to 1024")
    exit
