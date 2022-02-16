
class Python:
	name = "Python3"
	version = 3
x = Python()
print("Is python present ? " + str(hasattr(x, 'name')))
print("Is version present ? " + str(hasattr(x, 'version')))
