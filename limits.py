print("Welcome to limits")

def f(x):
    return (x**2 - 1)/(x - 1) # function f(x) = (x^2 -1 )/(x - 1)
x_values = [0.9,0.99,0.999,1.001,1.1] #values close to 1
for x in x_values:
    print(f"f({x}) = {f(x):.2f}") # Rounds off to 2dp