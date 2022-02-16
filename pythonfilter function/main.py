
x = 3
def func():
    y = 7
    z = x * y
    globals()['x'] = z
    print(z)
func()
