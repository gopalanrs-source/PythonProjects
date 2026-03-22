name = "Gopal"
age = 30

def func1():
    global age
    age += 2
    color = 'green'
    def func2(name):
        print(age)
        nonlocal color
        color = 'red'
        print(color)
        print(name)
    func2("Hello")
func1()
