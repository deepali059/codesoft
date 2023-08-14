from tkinter import *
import random
import string

root = Tk()
root.geometry("400x280")
root.title("Password Generator")

##### INITIAL VARIABLES
title = StringVar()
choice = IntVar()
lengthlabel = StringVar()
passlength = IntVar()
symbols = "!§$%&/()=?{[]}*+'#~,;.:-_'<>"
poor = string.ascii_uppercase + string.ascii_lowercase
average = string.ascii_uppercase + string.ascii_lowercase + string.digits
advanced = poor + average + symbols


##### FUNCTIONS
def selection():
    choice.get()


def callback():
    Isum.config(text=passgen())


Isum = Label(root, text="")
Isum.pack(side=BOTTOM)

password = str(callback)


# Password generation script - joins a random symbol to the string for how many times set in the spinbox
def passgen():
    global password
    password = ""
    if choice.get() == 1:
        return password.join(random.sample(poor, passlength.get()))
    elif choice.get() == 2:
        return password.join(random.sample(average, passlength.get()))
    elif choice.get() == 3:
        return password.join(random.sample(advanced, passlength.get()))


# Copies the current password to the clipboard
def copytoclipboard():
    global password
    print(password)
    Isum.clipboard_clear()
    Isum.clipboard_append(password)
    Isum.update()


##### USER INTERFACE
label = Label(root, textvariable=title).pack()
title.set("The strength of the password:")

R1 = Radiobutton(root, text="Uppercase and Lowercase", variable=choice, value=1, command=selection).pack(anchor=CENTER)
R2 = Radiobutton(root, text="Uppercase, Lowercase, Digits", variable=choice, value=2, command=selection).pack(
    anchor=CENTER)
R3 = Radiobutton(root, text="Uppercase, Lowercase, Digits, Symbols", variable=choice, value=3, command=selection).pack(
    anchor=CENTER)

lengthlabel.set("Password length: (4 to 20)")
lengthtitle = Label(root, textvariable=lengthlabel).pack()

spinboxlength = Spinbox(root, from_=4, to_=20, textvariable=passlength, width=13).pack()

passgenButton = Button(root, text="Generate Password", command=callback)
passgenButton.pack()

copyButton = Button(root, text="Copy Password to Clipboard", command=copytoclipboard)
copyButton.pack(side=BOTTOM)

root.mainloop()

