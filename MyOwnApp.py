import customtkinter as ctk


app = ctk.CTk()
app.title("Celcius to Farenheit conversion")
app.geometry("500x400")
CelcFrame =ctk.CTkFrame(master=app, width=340, height=70,
                        bg_color="white", fg_color="white")
CelcFrame.grid(row=0, column=0, padx=5, pady=5)







