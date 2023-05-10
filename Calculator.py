import customtkinter as ctk

currentText = "0"
num = 0
op = ""



def addText(str):
    global currentText
    if float(currentText) == 0 and str != '.' and '.' not in currentText:

        currentText = ""
    currentText = currentText + str
    calcLabel.configure(text=currentText)





app = ctk.CTk()
app.geometry("350x500")
app.title("Calculator")
app.configure(bg_color="white", fg_color="white")

calcFrame =ctk.CTkFrame(master=app, width=340, height=70,
                        bg_color="white", fg_color="white")
calcFrame.grid(row=0, column=0, padx=5, pady=5)

calcLabel = ctk.CTkLabel(master=calcFrame, text="0", width=330, height=70,
                         anchor="e", font=ctk.CTkFont(size=50))
calcLabel.grid(row=0, column=0, padx=5)

btnFrame = ctk.CTkFrame(master=app, width=340, height=400,
                        bg_color="white", fg_color="white")
btnFrame.grid(row=1, column=0, padx=5, pady=5)



# row=0
btnCE = ctk.CTkButton(master=btnFrame, text="CE", width=75, height=65,
                      font=ctk.CTkFont(size=30),
                      fg_color="gray", bg_color="white")
btnCE.grid(row=0, column=0, padx=2, pady=2)

btnBack = ctk.CTkButton(master=btnFrame, text="<--", width=75, height=65,
                      font=ctk.CTkFont(size=30),
                      fg_color="gray", bg_color="white")
btnBack.grid(row=0, column=1, padx=2, pady=2)

btnPercent = ctk.CTkButton(master=btnFrame, text="%", width=75, height=65,
                      font=ctk.CTkFont(size=30),
                      fg_color="gray", bg_color="white")
btnPercent.grid(row=0, column=2, padx=2, pady=2)

btnDivision = ctk.CTkButton(master=btnFrame, text="÷", width=75, height=65,
                      font=ctk.CTkFont(size=30),
                      fg_color="gray", bg_color="white")
btnDivision.grid(row=0, column=3, padx=2, pady=2)

btn7 = ctk.CTkButton(master=btnFrame, text="7", width=75, height=65,
                      font=ctk.CTkFont(size=30),
                      fg_color="gray75", bg_color="white",
                     command=lambda : addText("7"))
btn7.grid(row=1, column=0, padx=2, pady=2)

btn8 = ctk.CTkButton(master=btnFrame, text="8", width=75, height=65,
                      font=ctk.CTkFont(size=30),
                      fg_color="gray75", bg_color="white",
                     command=lambda : addText("8"))
btn8.grid(row=1, column=1, padx=2, pady=2)

btn9 = ctk.CTkButton(master=btnFrame, text="9", width=75, height=65,
                      font=ctk.CTkFont(size=30),
                      fg_color="gray75", bg_color="white",
                     command=lambda : addText("9"))
btn9.grid(row=1, column=2, padx=2, pady=2)

btnMultiplication = ctk.CTkButton(master=btnFrame, text="x", width=75, height=65,
                      font=ctk.CTkFont(size=30),
                      fg_color="gray", bg_color="white")
btnMultiplication.grid(row=1, column=3, padx=2, pady=2)

btn4 = ctk.CTkButton(master=btnFrame, text="4", width=75, height=65,
                      font=ctk.CTkFont(size=30),
                      fg_color="gray75", bg_color="white",
                     command=lambda : addText("4"))
btn4.grid(row=2, column=0, padx=2, pady=2)

btn5 = ctk.CTkButton(master=btnFrame, text="5", width=75, height=65,
                      font=ctk.CTkFont(size=30),
                      fg_color="gray75", bg_color="white",
                     command=lambda : addText("5"))
btn5.grid(row=2, column=1, padx=2, pady=2)

btn6 = ctk.CTkButton(master=btnFrame, text="6", width=75, height=65,
                      font=ctk.CTkFont(size=30),
                      fg_color="gray75", bg_color="white",
                     command=lambda : addText("6"))
btn6.grid(row=2, column=2, padx=2, pady=2)

btnminus = ctk.CTkButton(master=btnFrame, text="-", width=75, height=65,
                      font=ctk.CTkFont(size=30),
                      fg_color="gray", bg_color="white")
btnminus.grid(row=2, column=3, padx=2, pady=2)

btn1 = ctk.CTkButton(master=btnFrame, text="1", width=75, height=65,
                      font=ctk.CTkFont(size=30),
                      fg_color="gray75", bg_color="white",
                     command=lambda: addText("1"))
btn1.grid(row=3, column=0, padx=2, pady=2)

btn2 = ctk.CTkButton(master=btnFrame, text="2", width=75, height=65,
                      font=ctk.CTkFont(size=30),
                      fg_color="gray75", bg_color="white",
                     command=lambda: addText("1"))
btn2.grid(row=3, column=1, padx=2, pady=2)

btn3 = ctk.CTkButton(master=btnFrame, text="3", width=75, height=65,
                      font=ctk.CTkFont(size=30),
                      fg_color="gray75", bg_color="white",
                     command=lambda: addText("3"))
btn3.grid(row=3, column=2, padx=3, pady=2)

btnPlus = ctk.CTkButton(master=btnFrame, text="+", width=75, height=65,
                      font=ctk.CTkFont(size=30),
                      fg_color="gray", bg_color="white")
btnPlus.grid(row=3, column=3, padx=3, pady=2)

btnPlusMinus = ctk.CTkButton(master=btnFrame, text="+/-", width=75, height=65,
                      font=ctk.CTkFont(size=30),
                      fg_color="gray75", bg_color="white")
btnPlusMinus.grid(row=4, column=0, padx=2, pady=2)

btn0 = ctk.CTkButton(master=btnFrame, text="0", width=75, height=65,
                      font=ctk.CTkFont(size=30),
                      fg_color="gray75", bg_color="white",
                     command=lambda: addText("0"))
btn0.grid(row=4, column=1, padx=2, pady=2)

btnDot = ctk.CTkButton(master=btnFrame, text=".", width=75, height=65,
                      font=ctk.CTkFont(size=30),
                      fg_color="gray75", bg_color="white",
                       command=lambda: addText("."))
btnDot.grid(row=4, column=2, padx=3, pady=2)

btnequals = ctk.CTkButton(master=btnFrame, text="=", width=75, height=65,
                      font=ctk.CTkFont(size=30),
                      fg_color="gray", bg_color="white")
btnequals.grid(row=4, column=3, padx=3, pady=2)

app.mainloop()