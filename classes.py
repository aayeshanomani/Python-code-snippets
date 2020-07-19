class Person:
    department = 'CSE'

    def set_name(self, newname):
        self.name = newname

p = Person()
Person.set_name(p, 'blue')
print(p.name)