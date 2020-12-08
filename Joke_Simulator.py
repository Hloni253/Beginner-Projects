#Joke Simulator -- Note: It is case sensitive

from tkinter import *

def click():
    entered_text=textentry.get()
    output.delete(0.0, END)
    try:
        Joke = myJokes[entered_text]
    except:
        Joke = "sorry the entered text is incorrect"
    output.insert(END, Joke)
window = Tk()
window.title("Unknown Test")
window.configure(background="black")

Lb = Label(window,text="HAHAHAHA:~)",bg="black", fg="green", font="Lucida 15 bold")
Lb.pack()
myLabel = Label(window, text="Click for joke", bg="black", fg="white", font="Roman 10 bold")
myLabel.pack()
textentry = Entry(window, width=30, bg="white")
textentry.pack()
box = Button(window, text="Click", width=5, command=click)
box.pack()
yourLabel = Label(window, text="\nJOKE", bg="black", fg="white", font="none 19 bold")
yourLabel.pack()
output = Text(window, width=80, height=6, wrap=WORD, background="white")
output.pack()
myJokes = {
    "Marriage": "A wife asked her husband \nWhat do you like most about me? \nMy face or my body? \nThe husband looked at her and said \nYour sense of humour", "Husband" : "How can you tell the married man at a wedding \nThey are the ones dancing with every women except their wives"
    }