x = 2
try:
    print(x)
# except NameError:
#     print("Variable x is not defined")
except Exception as e:
    print("22222. An exception occurred")
    print(e)
except:  # this will catch all exceptions, but it is not recommended to use this. Also the previous exception catch is also similar to this, but it is recommended to use the previous one as it will give more information about the exception. and this will not give any information about the exception.
    print("11111. An exception occurred")
else:
    print("No exception occurred")
finally:
    print("This will always execute")