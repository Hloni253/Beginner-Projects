#Joke Simulator -- Note:Just click!

from tkinter import *
def click():
    output.delete(0.0, END)
    Jokes = myJokes[1]
    output.insert(END, Jokes)
def flick():
    output.delete(0.0, END)
    Jokes = myJokes[2]
    output.insert(END, Jokes)
def slick():
    output.delete(0.0, END)
    Jokes = myJokes[3]
    output.insert(END, Jokes)
def lick():
    output.delete(0.0, END)
    Jokes = myJokes[4]
    output.insert(END, Jokes)
window = Tk()
window.title("Joke GUI")
window.configure(background="yellow")
label = Label(window, text="HAHAHA:~)", bg="yellow", fg="black", font="broadway 20 bold")
label.pack()
Husband = Button(window, text="Husband", width=7, command=click)
Husband.pack()
Dirty = Button(window, text="Dirty", width=5, command=flick)
Dirty.pack()
Patient = Button(window, text="Patient", width=7, command=slick)
Patient.pack()
Drunk = Button(window, text="Drunk", width=5, command=lick)
Drunk.pack()
myLabel = Label(window, text="JOKE", bg="yellow", fg="black", font="Cooper 17 bold")
myLabel.pack()
output = Text(window, width=50, height=15, wrap=WORD, background="yellow")
output.pack()
myJokes = {
    1 : "Many years ago when I was 23, I got married to a widow.\nThis widow had a grown up daughter.\nMyfather fell in love with her and they married.\nThis made my father my son-in-law and it changed my life.\nMy daughter was my mother too because she was my father's wife.\nAfter a few years I had a baby boy and it complicated matters further\nMy son became my father's brother-in-law", 2 : "A man sent an SMS to his boss:\nI can't come to work, sick\nBoss SMS back:When I'm sick I usually kiss my wife\n2 hours later, SMS to the boss\nI'm better now and your house is lovely", 3: "Patient: My hair keeps falling out what can you give me to keep it in?\nDoctor:A shoebox", 4 : "A number 12 walks into a bar and asks for a beer\n Sorry I can't serve you, states the barman\nWhy not?, asks the number\nYou are under 18,replied the barman"
    }