class Person:
    def __init__(self, first_name, last_name, age, nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality
    def greeting(self):
        print(f"My name is: {self.first_name} {self.last_name}, i am {self.age} years old. I come from {self.nationality}")
# person1 = Person("John", "Smith", "23", "Germany")
# person1.greeting()
# person2 = Person("Daniel", "Dimitrov", "18", "Bulgaria")
# person2.greeting()
# person3 = Person("Kamelia", "Stoqnova", "18", "Ireland")
# person3.greeting()