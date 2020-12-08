#Program to play monopoly against

things = [6, 8, 9, 16, 18, 19, 26, 27, 29, 31, 32, 34]
please = [1, 3, 11, 13, 14, 21, 23, 24, 37, 39]
port = [5, 12, 15, 25, 28, 35]
skap = [2, 17, 33]
kans = [7,22,36]
pay = [4, 38]

a = 100000
b = 0
num = 0

while True:
    print("My amount is " + str(a))
    c = str(input("Gain or loss "))
    if c == "g":
        d = int(input("How much money do I gain? "))
        a = a + d
        print(a)
    elif c == "l":
        e = int(input("How much money do I lose? "))
        a = a - e
        print(a)
    else:
        print("Oh well")
        
    f = int(input("Roll "))
    b = b + f
    ber = b // 40
    if ber > num:
        print(num, ber)
        print("Time to get my salary")
        a = a + 20000
        num = ber
        print(a)
    g = b % 40
    print(g)

    for thing in things:
        if g == thing:
            h = str(input("Is it owned? "))
            if h == "y":
                print("Shit")
                i = int(input("Amount "))
                a = a - i
            else:
                print("Suck on it Hloni")

    for pleased in please:
        if g == pleased:
            j = str(input("Do I own it? "))
            if j == "y":
                house = str(input("Do I own all properties? "))
                if house == "y":
                    if a > 90000:
                        print("I'm buying a hotel")
                        hotel = int(input("How much is it? "))
                        a = a - hotel
                    elif a > 40000 and a < 90000:
                        print("I'm buying a house")
                        house = int(input("How much is it? "))
                        a = a - house
                    else:
                        print("Maybe next time")
                else:
                    print("Shit")
            elif j == "n":
                if a > 40000:
                    print("I'm buying it")
                    k = int(input("How much is it? "))
                    if k > 30000:
                        print("That is steep")
                    a = a - k
                    print(a)
                    
    for air in port:
        if g == air:
            l = str(input("Who own it? "))
            if l == "i":
                print("Shit")
                m = int(input("How much? "))
                a = a - m
            elif l == "m":
                print("Cool")
            else:
                if a > 40000:
                    print("I'm buying it")
                    a = a - 20000
                else:
                    print("I'm not buying it")
                    
    for kan in kans:
        if g == kan:
            print("Read me my chance Hloni")
            n = str(input("Do I gain or do I lose? "))
            if n == "g":
                o = int(input("How much do I gain? "))
                a = a + o
            elif n == "l":
                p = int(input("How much do I lose? "))
                a = a - p
            else:
                print("Whatever")
                
    for kap in skap:
        if g == kap:
            print("Read me my chest Hloni")
            q = str(input("Do I gain or do I lose? "))
            if q == "g":
                r = int(input("How much do I gain? "))
                a = a + r
            elif q == "l":
                s = int(input("How much do I lose? "))
                a = a - s
            else:
                print("Whatever")
                
    for payed in pay:
        if g == payed:
            print("Shit")
            if payed == 4:
                a = a - 20000
            else:
                a = a - 10000
            
    if a <= 0:
        print("Shit I lose, congrats you win Hloni")
        break
            