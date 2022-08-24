# polymorphism ( many + Forms ) the condition of occurrence in different forms
#method Overloading/complie_time polymorphism/static polymorphism
### 1.1 Operator OverLoading
### 1.2 Method OverLoading
### 1.3 Constructor OverLoading

#Operator OverLoading
'''
class Employee:
    def m1(self,x=0,y=0,z=0):
        print('this is zero arguments messege')
    def m1(self, x,y=0,z=0):
        print('one argument passed messege')
    def m1(self, x, y,z=0):
        print('two argument passed messege')
    def m1(self, x, y, z):
        print('565 Three argument passed messege!!!!!!!!')
emp=Employee()
emp.m1(True,False,
'malli')
# Why python does not support Overloading, where as JAVA support overloading
#in JAVA data types should be decleard Expectly because JAVA Is a Static Typed Language
#In Python Data tyes We Are Nor Declead Internally PVM Decleard Because Python Is Dynamically Typed Language
'''
#Constructor OverLoading
class Test:
    def __init__(self):
        print('zero arg constructor called!!!!')

    def __init__(self, eno):
        print('ONE arg constructor called!!!!', eno)

    def __init__(self, eno=None, name=None):
        print('TWO arg constructor called!!!!', eno, name)

    def __init__(self, *x):
        print('Latest TWO arg constructor called!!!!', x)
        print('type(x)', type(x))


    def m1(self):
        print('M1 method got called....')

t = Test() # Error
#t = Test(1001)
#t = Test(1001, 'Jagdeesh')



