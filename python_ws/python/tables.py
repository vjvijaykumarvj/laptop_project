#create the MathsTable using Python
'''
number = int(input('Enter any number'))
value = int(input('Enter any value'))
for value in range(1,1+value):
    print('{} * {} = {} '.format(number,value,number*value))


number=19
value=10
for value in range(1,1+value):
    print(number , '*' , value , '=' , number * value)
'''''
#swaping in python using normal method
'''
a=10
b=20
a,b = b,a
print('a--->',a)
print('b--->',b)
'''
#Using Python Create The Prime Number
'''number = int(input('Enter Any Number'))
if number > 1:
    for i in range(2,number):
        if number % i ==0:
            print(number,'Its not Prime')
            break
    else:
        print(number,'Prime Number')
'''
#Polindrium Checking In Python
'''string=input('Enter a Name')
if string==string[::-1]:
    print('its a polindrium')
else:
    print('not polindrium')
'''
#polindriom in python Using Functions
'''def polindriom(name):
    reversedname=name[::-1]
    if name==reversedname:
        print('Polindriom')
    else:
        print('Not Polindriom')
polindriom('vasusava')
'''

#separate The String And Intigers In List
'''names=[]
numbers=[]
l=['vijay',12,13,17,'das','ghsh',100,'hdjhjd']
for i in l:
    if type(i)==str:
        names.append(i)
    if type(i)==int:
        numbers.append(i)
print('numbers',numbers)
print('names',names)
'''
#compute The Fibonacci numbers in Python
a,b=0,1
n=10
for i in range(n):
    print(b,end=' ')
    a, b = b, a+b






