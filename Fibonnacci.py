a = int(input("First number: "))
b = int(input("Second number: "))
ran = int(input("How many times should it be repeated: "))
c = 0

for i in range(ran):
    c = a + b
    a = b
    b = c
    print(c)