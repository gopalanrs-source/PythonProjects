def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

total = add(1,2,3,4,5)
print(total)


def try_keyword_args(**kwags):
    for key, value in kwags.items():
        print(f"{key} : {value}")

try_keyword_args(name="John", age=30, city="New York")

def func (a,b,*args, option = False, **kwa):
    print("This is a function that demonstrates the use of *args and **kwargs -----------")
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")
    print(f"option: {option}")
    print(f"kwa: {kwa}")

func(1,2,3,4,5, option = True, name="John", age=30)


#recurssion

def addnum(n):
    if n >=9:
        print(n)
        return n+1
    else:
        print(n)    
        return addnum(n+1)
    
addnum(1) 

def find_factorial(n):
    if n == 0:
        # print(f"Factorial of {n} is 1")
        return 1
    else:
        # print(f"Factorial of {n} is {n} * factorial of {n-1}")
        return n*find_factorial(n-1)
    
num = int(input("Enter a number: "))
if type(num) != int or num < 0:
    print("Please enter a non-negative integer.")
else:
    fact = find_factorial(num)
    print(f"Factorial of {num} is {fact}")



    
    
    