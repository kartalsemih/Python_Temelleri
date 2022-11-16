#global scope
x='global x'

def function():
    #local scope
    #x='local x'
    print(x)

function()
print(x)

#########################

#global
name='çınar'

def changename(new_name):
    #local
    global name
    name=new_name
    print(name)

changename('ada')
print(name)

##########################

name = 'global string'

def greeting():
    #name='çınar'

    def hello():
        #name='ada'
        print('hello '+name)

    hello()

greeting()


##############################


x=50

def test():
    global x
    print(f'x : {x}')

    x=100
    print(f'changed x to {x}')

test()
print(x)
