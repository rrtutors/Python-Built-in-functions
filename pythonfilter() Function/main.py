
def fun(var):
	x = ['p', 'y', 't', 'h', 'o','n']
	if (var in x):
		return True
	else:
		return False

a = ['p', 'y', 'y', 'o', 'n', 'h', 'p', 'y']

filtered = filter(fun, a)

print('The filtered letters are:')
for s in filtered:
	print(s)
