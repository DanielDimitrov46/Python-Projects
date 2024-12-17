from Exercises.EXERCISE_17_12_2024.Person import Person


class Lecturer (Person):
    def __init__(self, first_name, last_name, age, nationality, university, experience):
        Person.__init__(self, first_name, last_name, age, nationality)
        self.experience = experience
        self.university = university

    def __str__(self):
        return f"My name is: {self.first_name} {self.last_name}, i am {self.age} years old. I come from {self.nationality}. I'm at {self.university} university and my experinece is: {self.experience}"

