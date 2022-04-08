import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
import random

window = tk.Tk()
window.title("Grabbelton")
window.geometry("400x300")

GrabbelLijst = ["speelgoed auto", "bestuurbare auto", "fluitje", "doosje lego", "duikbril", "voetbal", "sleutelhanger", "balletjes pistool", "nerf gun", "waterpistool", "stuiterbal"]
def KnopDrukken():
    RandomItem = random.choice(GrabbelLijst)
    GrabbelLijst.remove(RandomItem)
    box1.configure(text= ItemTekst())
    showinfo("Item Gegrabbeld", "Gefeliciteerd, je hebt een " +RandomItem+" gegrabbeld!")
    
    return RandomItem


button = tk.Button(text="grabbelen", command=KnopDrukken)
button.pack(pady=80, padx=30)

def ItemTekst():
    AantalItems = tk.IntVar(value= len(GrabbelLijst))
    AantalDoorgeven = AantalItems.get()
    return AantalDoorgeven

box1 = tk.Label(
    window,
    text= ItemTekst()
    
)

box1.pack(
    ipadx= 50,
    ipady= 50,
    fill= "both"
)



window.mainloop()