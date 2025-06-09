def main_welcome(func):
    def sub_function():
        print("Hello Asif")
        func()
        print("Welcome to the world of Python")
    return sub_function()

def simple_function():
    print("This is a simple function")    

main_welcome(simple_function)



def great():
    return "Hello Asif"

def falling_function(func): 
    return func()

a = falling_function(great)
print(a)
