import tkinter as tk

root = tk.Tk()
root.title("Hello")
root.geometry("300x200")


box1 = tk.Label(
    root,
    text="Hello tkinter!",
    bg="blue",
    fg="red"

)


box1.pack(
    ipadx=10,
    ipady=10,
    fill="both",
    expand=True

)


box2 = tk.Label(
    root,
    bg="green"
)

box2.pack(
    ipadx=10,
    ipady=10,
    fill="both"
)
root.mainloop()