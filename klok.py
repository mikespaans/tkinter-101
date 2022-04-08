import tkinter as tk
import datetime

Tijd = datetime.datetime.now()

window = tk.Tk()
window.title("De Klok")
window.geometry("300x200")

box1 = tk.Label(
    window,
    
    bg="black",
    fg="white",
)

box1.pack(
    ipadx=10,
    ipady=10,
    fill="both",
    expand=True
)

def klok():
    Tijd = datetime.datetime.now()
    NieuweTijd = str(Tijd.hour) + ":" + str(Tijd.minute) +":" + str(Tijd.second)
    StringVar = tk.StringVar(value=NieuweTijd)
    TijdText = StringVar.get()
    box1.configure(text=TijdText)
    window.after(1000, klok)

window.after(1000, klok)

window.mainloop()