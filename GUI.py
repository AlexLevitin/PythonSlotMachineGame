import customtkinter
import tkinter as tk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("1200x720")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady = 20, padx = 60, fill = "both", expand = True)

label = customtkinter.CTkLabel(master=frame, text="Slot Machine Game", text_color="white",font=("Roboto", 55))
label.pack(pady = 12, padx = 10)

budgetLabel = customtkinter.CTkLabel(master=frame, text="", text_color="white",font=("Roboto", 30))
budgetLabel.pack(pady = 12, padx = 10)

msgLabel = customtkinter.CTkLabel(master=frame, text="", text_color="white",font=("Roboto", 30))
msgLabel.pack(pady = 12, padx = 10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text = "Enter Bet Ammount: ", font=("Roboto", 25), width=250)
entry1.pack(pady = 12, padx = 10)

slotFrame = customtkinter.CTkFrame(master=frame, fg_color="dim gray", corner_radius=50)
slotFrame.pack(pady = 12, padx = 10)


slot1 = customtkinter.CTkLabel(master=slotFrame, text="", text_color="white", font=("Roboto", 30))
slot1.pack(pady = 12, padx = 10, side = "left")

slot2 = customtkinter.CTkLabel(master=slotFrame, text="", text_color="white", font=("Roboto", 30))
slot2.pack(pady = 12, padx = 10, side = "left")

slot3 = customtkinter.CTkLabel(master=slotFrame, text="", text_color="white", font=("Roboto", 30))
slot3.pack(pady = 12, padx = 10, side = "left")

playButton = customtkinter.CTkButton(master=frame, text="Play Game", text_color="white",font=("Comic Sans MS", 50))
playButton.pack(pady = 12, padx = 10)

stam = customtkinter.CTkTextbox(master=frame, width=300)
stam.insert("0.0","GAME RULES: \nPlace your bet(x)\nIf all 3 numbers are the same you win x*2$\nIf 2 of the numbers are the same you win x*1.5$\nIf none of the numbers are the same you lose x$")
stam.pack(pady = 12, padx = 10)

