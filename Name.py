print("Welcome New Owner \nWhat is your name?")
name = input()
name = str(name)
if len(name) > 5:
    print("Cool name ", name)
elif len(name) < 5:
    print("Dope name", name)
else:
    print("Please give me your name")
    
    
    