number= int(input('enter any number'))
if number > 1:
    for i in range(2,number):
        if number % 2 == 0:
            print('not prime')
            break
    else:
        print('prime number')

