import tkinter
import time

window = tkinter.Tk()

# Hier tussen code

AchtergrondList = ["white","yellow","orange", "red", "purple", "black" ]
window.title("My First Window")
window.geometry("50x50")
Aftellen = 6

for i in range(6):
    window.after(2000, window.configure(bg=AchtergrondList[i]))
    window.update()
    print (Aftellen)
    Aftellen -= 1

time.sleep(2)
window.destroy()

# Hier tussen code


window.mainloop()

print ("BOOM!")
