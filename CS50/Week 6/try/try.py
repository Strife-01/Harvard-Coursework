class Person() :
    
    def __init__(self, name, age) :
        self.name = name
        self.age = age
    
    def change_name(self, name) :
        self.name = name

    def change_age(self, age) :
        self.age = age

    def print_person(self) :
        print("This person's name is {} and they are {} years old.".format(self.name, self.age))


def main() :
    nr_people = get_int("How many people do you have in DB? ")
    list_people = people_init(nr_people)
    print_people(list_people, nr_people)


def get_int(string) :
    number = None
    while True :
        number = input(string)
        try :
            number = int(number)
            break
        except : continue
    return number


def people_init(number) :
    l = list()
    for num in range(number) :
        name = input("Name: ")
        age = None
        while True :
            age = input(f"{name}'s age is: ")
            try :
                age = int(age)
                break
            except : continue
        person = Person(name, age)
        l.append(person)
    return l


def print_people(list_people, number) :
    for num in range(number) :
        person = list_people[num]
        person.print_person()


main()
