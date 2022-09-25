class Person:
    def __init__(self, rzdn, n, s, age, ng):
        self.rzd_number = rzdn
        self.name = n
        self.surname = s
        self.age = age
        self.number_group = ng

    def __repr__(self):
        return str(self.rzd_number) + ";" + str(self.name) + ";" + str(self.surname) + ";" + str(self.age) + ";" + str(
            self.number_group)


Persons = []
kol_uch = int(input("Ввидите кол-во учеников kol_uch: "))
for i in range(kol_uch):
    print("Ученик ", i + 1)
    Persons.append(Person(rzdn=input("Введите порядковый номер rzdn: "),
                          n=input("Введите имя n: "),
                          s=input("Введите фамилию s: "),
                          age=input("Введите возраст age: "),
                          ng=input("Введите номер группы ng: ")))

file = open("spisok_uch.txt", 'w')  # with open("spisok_uch.txt", 'w') as file_object:
for person in Persons:  # for persona in Persons:
    file.write(str(person) + '\n')  # file_object.write(str(persona) + '\n')
file.close()

Persons.clear()
file = open("spisok_uch.txt", 'r')
strok_for_read = file.readlines()
file.close()
for i in strok_for_read:
    i = i.strip()
    x = i.split(';')
    Persons.append(Person(*x))

# top5 = sorted(Persons, key=lambda s: s.age, reverse=True)
Persons.sort(key=lambda s: s.age, reverse=True)

file2 = open("top5_age.txt", 'w')
for person in Persons:  # for person in top5:
    file2.write(str(person) + '\n')
file2.close()

names_map = {}
for person in Persons:
    if not person.name in names_map:
        names_map[person.name] = 0
    names_map[person.name] = names_map[person.name] + 1

file3 = open("kol_uch_name.txt", 'w')
for name in names_map:
    file3.write(name + '-' + str(names_map[name]) + '\n')
file3.close()
