
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




