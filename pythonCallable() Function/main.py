def func_callable():
   x = 4
   y = 6
   z = x^y
   return z
a = func_callable
print(callable(a))
print(a)
b=func_callable()
print(b)