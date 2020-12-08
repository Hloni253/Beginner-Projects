class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def person(self):
        print("Hi my name is ", self.name, " and I'm a ", self.gender, " who is ", self.age, " years old")
        
Name = str(input("What is your name: "))
Age = int(input("How old are you: "))
Gender = str(input("Gender: "))

p1 = Person(Name, Age, Gender)
p1.person()