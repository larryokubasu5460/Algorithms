fibonacci_cache={}
def fibonacci_memo(data):
    if data in fibonacci_cache:
        return fibonacci_cache[data]
    if data == 1:
            value = 1
    elif data == 2:
            value = 1
    elif data > 2:           
            value =  fibonacci_memo(data -1) + fibonacci_memo(data -2)
    fibonacci_cache[data] = value
    return value

for i in range(1, 201):
     print("fib({}) = ".format(i), fibonacci_memo(i))