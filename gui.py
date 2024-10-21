from tkinter import *
from PIL import Image, ImageTk
import action 
import speech_to_text 

def User_send():
    send = entry1.get()
    bot = action.Action(send)
    text.insert(END, "Me --> " + send + "\n")
    if bot is not None:
        text.insert(END, "Bot <-- " + str(bot) + "\n")
    if bot == "ok sir":
        root.destroy()  
    entry1.delete(0, END)

def ask():
    ask_val = speech_to_text.speech_to_text()
    if ask_val is not None:
        bot_val = action.Action(ask_val)
        text.insert(END, "Me --> " + ask_val + "\n")
        if bot_val is not None:
            text.insert(END, "Bot <-- " + str(bot_val) + "\n")
        if bot_val == "ok sir":
            root.destroy()
    else:
        text.insert(END, "Me --> No input detected.\n")

def delete_text():
    text.delete("1.0", "end")

def on_entry_click(event):
    if entry1.get() == "Message AI Assistant":
        entry1.delete(0, "end")
        entry1.config(fg="#333")

def on_focusout(event):
    if entry1.get() == "":
        entry1.insert(0, "Message AI Assistant")
        entry1.config(fg="#a9a9a9")

root = Tk()
root.geometry("550x675")
root.title("AI Assistant")
root.resizable(False, False)
root.config(bg="#b39cd0")

# Main Frame
Main_frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
Main_frame.config(bg="#b0a8b9")
Main_frame.grid(row=0, column=1, padx=55, pady=10)

# Text Label 
Text_label = Label(Main_frame, text="AI Assistant", font=("comic Sans ms", 14, "bold"), bg="#fbeaff")
Text_label.grid(row=0, column=0, padx=20, pady=10)

# Image 
Display_Image = ImageTk.PhotoImage(Image.open("image/assistant.png"))
Image_Label = Label(Main_frame, image=Display_Image)
Image_Label.grid(row=1, column=0, pady=20)

# Add a text widget
text = Text(root, font=('Courier 10 bold'), bg="#4e8397", fg="#fff6ff")
text.grid(row=2, column=0)
text.place(x=100, y=375, width=375, height=100) 


entry1 = Entry(root, justify=CENTER, bg="#d5cabd", fg="#a9a9a9", font=("Arial", 14))
entry1.insert(0, "Message AI Assistant")
entry1.place(x=100, y=500, width=350, height=50)

entry1.bind("<FocusIn>", on_entry_click)
entry1.bind("<FocusOut>", on_focusout)

button1 = Button(root, text="Ask", bg="#008b74", fg="white", pady=16, padx=40, borderwidth=1, relief=RIDGE, font=("Arial", 14), command=ask)
button1.place(x=70, y=575)

button2 = Button(root, text="Send", bg="#296073", fg="white", pady=16, padx=40, borderwidth=1, relief=RIDGE, font=("Arial", 14), command=User_send)
button2.place(x=400, y=575)

button3 = Button(root, text="Delete", bg="#c34a36", fg="white", pady=16, padx=40, borderwidth=1, relief=RIDGE, font=("Arial", 14), command=delete_text)
button3.place(x=225, y=575)

root.mainloop()