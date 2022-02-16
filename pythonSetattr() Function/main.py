
class ILP:
	my_var = 'ILovePython'

my_object = ILP()

print("Before setattr variable name : ", my_object.my_var)

setattr(my_object, 'my_var', 'ILovePython')

print("After setattr variable name : ", my_object.my_var)
