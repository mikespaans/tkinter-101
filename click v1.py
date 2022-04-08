import tkinter as tk

window = tk.Tk()
window.title("Clicker")
window.geometry("600x300")



Number = 0
def Omhoog():
    global Number
    Number += 1
    TextNumber = tk.IntVar(value= Number) 
    TextNumber = TextNumber.get()
    box1.configure(text= TextNumber)
    Achtergrond()
    return TextNumber

def Omlaag():
    global Number
    Number -= 1
    TextNumber = tk.IntVar(value= Number) 
    TextNumber = TextNumber.get()
    box1.configure(text= TextNumber)
    Achtergrond()
    return TextNumber

def Achtergrond():
    if Number == 0:
        box1.configure(background="grey")
        window.configure(background="grey")
    elif Number > 0:
        box1.configure(background="green")
        window.configure(background="green")
    else:
        box1.configure(background="red")
        window.configure(background="red")

box1 = tk.Label(
    window,
    text= 0,
    background="grey"
)
window.configure(background="grey")
button = tk.Button(text="Up", command=Omhoog)
button.pack(padx=10, pady=10)

box1.pack(
    ipadx=50,
    ipady=30,
    fill="both"
)

Button2 = tk.Button(text="Down", command=Omlaag)
Button2.pack(padx=100, pady=30)







window.mainloop()