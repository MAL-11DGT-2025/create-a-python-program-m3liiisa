def greeting():
    print('Comment ca va')

def greeting_w_name(name):
    print(f'Comment ca va {name}.')

def add(a, b):
    print(a + b)

def minus(a, b):
    print(a - b)

def divide(a, b):
    print(a / b)

def multiply(a, b):
    print(a * b)

#greeting()
#greeting()
#greeting()  #This is going to print the greeting 3 times

#greeting_w_name('Melisa')
#greeting_w_name('Macky')
#greeting_w_name('Simon')  #This prints greeting + name

#add(5, 10)
#add(120, 530)
#add(6, 55)    #This is gonna add the two numbers

#minus(84, 5)
#minus(20, 20)
#minus(1098, 1040)  #This is gonna minus the numbers

operation = input('Which operation do you want to use (+, -, *, /): ')
a = input('Enter your first number: ')
b = input('Enter your second number: ')

if operation == '+':
    add(a, b)
elif operation == '-':
    minus(a, b)
elif operation == '/':
    divide(a, b)
elif operation == '*':
    multiply(a, b)