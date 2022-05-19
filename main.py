# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def sum(a, b):
    print(a+b)

def mul(a, b):
    print(a*b)

def div(a, b):
    print(a/b)
def first_function():
    print("this is first function")

def second_function():
    print("this is second function")

def third_function():
    print("this is third function")

def fib(a):
    if a <= 1:
        return 1
    return fib(a-1)+fib(a-2)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(fib(5))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
