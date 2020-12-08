import random

a = {'hloni':'the greatest', 'john':'another guy', 'jacob':'another dude', 'dude':'the greatest guy','yugo':'i dont know','temari':'Gaaras sister','gaara':'sand controller'}
me = list(a)
d = True
l = 0

print("Welcome to science dict game\nIf you guess the correct term to the definition you win")

while d == True:
    num = len(me) - 1
    o = random.randint(0,num)
    u = me[o]
    print(a[u])
    i = str(input())
    if i == u:
        l = l + 1
        print(l)
    elif i == 'EXIT':
        d = False
    else:
        print("Loser")
        
        
