class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('Get name')
        return self._name

    def set_name(self, value):
        print('Set name to ' + value)
        self._name = value

    def del_name(self):
        print('Deleting name')
        del self._name

    name = property(get_name, set_name, del_name, 'Name property')

p = Person('Calvin')
print(p.name)
p.name = 'Clein'
del p.name