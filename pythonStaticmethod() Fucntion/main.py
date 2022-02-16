class Multiplier:

  def multiply_numbers(a, b):
    return a * b

c= Multiplier.multiply_numbers

c = staticmethod(Multiplier.multiply_numbers)

d = c(14, 17)
print('The product of 14 and 17 is:', d)

