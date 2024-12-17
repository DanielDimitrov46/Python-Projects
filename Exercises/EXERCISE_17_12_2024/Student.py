from Exercises.EXERCISE_17_12_2024.Person import Person


class Student(Person):
    def __init__(self, first_name, last_name, age, nationality, university, study_year):
        Person.__init__(self, first_name, last_name, age, nationality)
        self.university = university
        self.study_year = study_year
    def __str__(self):
        return f"My name is: {self.first_name} {self.last_name}, i am {self.age} years old. I come from {self.nationality}. I'm at {self.university} university and year is: {self.study_year}"

student1 = Student("Daniel", "Dimitrov", "18", "Ireland", "Harvard", "2019")
print(student1)