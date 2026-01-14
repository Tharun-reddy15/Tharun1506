def add(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

add(10,20)
print(sub(100,20))

def hello(greeting='Hello', name='world'):
    print('%s, %s!' % (greeting,name))
hello('Greetings')

def print_params(*params):
    print(params)
print_params('Testing')
print_params(1,2,3)

def print_params_3(**params):
    print(params)
print_params_3(x=1,y=2,z=3)