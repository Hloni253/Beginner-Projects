"""Verify that the sum of even numbers is even, the sum of odd numbers is even, and the sum of even and odd numbers is odd
The challenge is that I have to use if, else, pass, continue and range, and all these conditionals must be used atleast once"""

e = 0
o = 0

pe = False
po = False

for i in range(10):
    if i % 2 == 0:
        if e == True:
            if (i + pe) % 2 == 0:
                print("The sum of "+str(i)+" and "+str(pe)+" is even")
                pe = i
            else:
                pass
        else:
            pe = i
            e = True
    else:
        if o == True:
            if (i + po) % 2 == 0:
                print("The sum of "+str(i)+" and "+str(po)+" is even")
                po = i
            else:
                pass
        else:
            po = i
            o = True
        if e == True:
            if (i + pe) % 2 == 0:
                pass
            else:
                print("The sum of "+str(i)+" and "+str(pe)+" is odd")
        else:
            continue
