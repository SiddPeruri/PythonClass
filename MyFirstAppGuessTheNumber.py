import customtkinter as ctk

app = ctk.CTk()
app.geometry("350x500")
app.title("Guess the Number!")
app.configure(bg_color="white", fg_color="white")

EntNum = customtkinter.CTkButton(app, text="CTkButton", command=EntNum)

import random

#get a number between 1-9
num = random.randint(1,45)

guess=False
while not guess:
    #ask user to guess a random number
user=int(input("Guess the number between 1 and 45: "))
if user < num: #the user guess is lower
    print("Too low")
elif user > num: #The user guess is higher
    print("Too high!")
else: #The user guessed it correctly
    print("Nice job! You guessed it correctly!")
    break




=======
#simple app created using customtkinter
import customtkinter as ctk

def enter_clicked():
    #print("Enter clicked")
    name = nameEntry.get()
    address = addressEntry.get()
    print(name)
    print(address)
strList = [name,address]
   info = '\n'.join(strList)
   infoLabel.configure(text=info)

app = ctk.CTk()
app.title("My First App")
app.geometry("500x400")

nameLabel = ctk.CTkLabel(app, text="Name: ")
nameLabel.grid(row=0, column=0)

nameEntry = ctk.CTkEntry(app, placeholder_text="Enter your name")
nameEntry.grid(row=0, column=1)

nameAddress = ctk.CTkLabel(app, text="Address: ")
nameAddress.grid(row=1, column=1)

addressEntry = ctk.CTkEntry(app, placeholder_text="Enter your address")
addressEntry.grid(row=1, column=1)

enterButton = ctk.CTkButton(app, text="Enter", command=enter_clicked)
enterButton.grid(row=2, column=1)


infoLabel = ctk.CTkLabel(app, text="")
infoLabel.grid(row=4, column=1)



app.mainloop()
>>>>>>> origin/master
