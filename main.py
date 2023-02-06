from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count_number):
    if count_number >= 0:
        print(count_number)
        window.after(1000, count_down, count_number - 1)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

count_down(10)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


timer = Label(text="Timer", font=(FONT_NAME, 55), fg=GREEN, bg=YELLOW)
timer.grid(column=1, row=0)

start = Button(text="Start", highlightbackground=YELLOW)
start.grid(column=0, row=2)
# how to get rid of the edge & adjust position to right side?
# simply highlightbackground=YELLOW

reset = Button(text="Reset", highlightbackground=YELLOW)
reset.grid(column=2, row=2)
# how to get rid of the edge & adjust position to right side?
# simply highlightbackground=YELLOW

slots_checked = Label(text="✅", font=(FONT_NAME, 20), bg=YELLOW)
slots_checked.grid(row=3, column=1)
# how to get rid of the edge & adjust position to right side?
# this time is bg=YELLOW




window.mainloop()





