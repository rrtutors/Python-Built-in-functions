x = bytearray('XYZ', 'utf-8')

a = memoryview(x)

print(a[0])
print(bytes(a[0:1]))
