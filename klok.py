import tkinter as tk
import datetime

Tijd = datetime.datetime.now()



window = tk.Tk()
window.title("De Klok")
window.geometry("300x200")

box1 = tk.Label(
    window,
    
    # text= klok(),
    # window.config(text= str(Tijd.hour) + ":" + str(Tijd.minute) +":" + str(Tijd.second)),

    bg="black",
    fg="white",
    # window.after(1000, window.update())
)

# time.sleep(1)
# box1.configure(text= klok())



box1.pack(
    ipadx=10,
    ipady=10,
    fill="both",
    expand=True
)
# NieuweTijd = str(Tijd.hour) + ":" + str(Tijd.minute) +":" + str(Tijd.second)

def klok():
    Tijd = datetime.datetime.now()
    NieuweTijd = str(Tijd.hour) + ":" + str(Tijd.minute) +":" + str(Tijd.second)
    StringVar = tk.StringVar(value=NieuweTijd)
    TijdText = StringVar.get()
    box1.configure(text=TijdText)
    print (StringVar)
    # box1.update()
    window.after(1000, klok)
    
    
   

window.after(1000, klok)



window.mainloop()