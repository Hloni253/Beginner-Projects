class Phone:
    def __init__(self, name, color, p_type):
        self.name = name
        self.color = color
        self.p_type = p_type
        
    def op_system(self):
        if self.name == "Samsung":
            print("You are using Android")
        elif self.name == "Hisense":
            print("You're using Android")
        elif self.name == "iPhone":
            print("You are using OS")
            
p1 = Phone("Samsung", "black", "touch")
p2 = Phone("iPhone", "white", "touch")
p1.op_system()
p2.op_system()

class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    def phone_owned(self):
        print(self.name, "is using", self.phone)
        
person1 = Person("John", p1.name)
person2 = Person("Linda", p2.name)

person1.phone_owned()
person2.phone_owned()
        
        
        
        
        
        