import time
from tkinter import *
from tkinter import messagebox
import threading

timer_speed = 0


def restart():
    text_entry_box.delete("1.0", "end")
    text_entry_box.bind("<Key>", threading.Thread(target=countdown).start())


def add_time():
    global timer_speed
    timer_speed = 10


def countdown():
    global timer_speed
    timer = True
    timer_speed = 10
    while timer:
        time.sleep(1)
        timer_speed -= 1
        text_entry_box.bind("<Key>", add_time)
        if timer_speed == 0:
            timer = False
    messagebox.showinfo(title="Time Up", message=f"Time UP!")
    text_entry_box.delete("1.0", "end")

root = Tk()
root.title("Disappearing Text App")
root.minsize(width=1000, height=700)

text_entry_label = Label(root, text="!!Your text clears if you have stop writing for 10 seconds!!")
text_entry_label.grid(row=0, column=1)
text_entry_label.configure(font=("arial", 20, "bold"))

text_entry_box = Text(height=40, width=150, wrap="word")
text_entry_box.grid(row=1, column=1)
text_entry_box.configure(font=("arial", 15))

text_entry_box.bind("<Key>", threading.Thread(target=countdown).start())

restart_button = Button(root, text="RESTART", command=restart)
restart_button.grid(row=2, column=1)
restart_button.configure(font=("arial", 20, "bold"))

root.mainloop()