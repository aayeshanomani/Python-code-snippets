people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]

#option 1
hello1 = 'hello'

for person in people:
    print(lambda person:(person.split()[0] + ' ' + person.split()[-1]))
    print(split_title_and_name(person) == (lambda person:(person.split()[0] + ' ' + person.split()[-1])))
    #print('hello'+(lambda person: person+'5'))

#option 2
#list(map(split_title_and_name, people)) == list(map(???))
