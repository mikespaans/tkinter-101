import tkinter
import time

window = tkinter.Tk()

# Hier tussen code

AchtergrondList = ["white","yellow","orange", "red", "purple", "black" ]
window.title("My First Window")
Grootte = 50
# WindowGrootte = str(Grootte)+"x"+str(Grootte)
window.geometry("50x50")
Aftellen = 6

for i in range(6):
    print (Aftellen)
    Grootte += 50
    WindowGrootte = str(Grootte)+"x"+str(Grootte)
    Aftellen -= 1
    window.geometry(WindowGrootte)
    window.configure(bg=AchtergrondList[i])
    window.after(2000,window.update())
    # Grootte += 50
    # WindowGrootte = str(Grootte)+"x"+str(Grootte)
    

time.sleep(2)
window.destroy()

# Hier tussen code


window.mainloop()

print ("BOOM!")
