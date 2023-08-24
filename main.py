from tkinter import *
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checked = ""
timer_countdown = "00:00"

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    window.after_cancel(timer_countdown)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    slots_checked.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    # count_down(60 * 25)

    global reps, checked
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # game_on = True
    # while game_on:
    #     reps += 1
    #     if reps % 2 == 1:
    #     #   if it's the 1st/3rd/5th/7th reps
    #         count_down(work_sec)
    #     elif reps % 2 == 0 and reps != 8:
    #     #   if it's the 2nd/4th/6th reps
    #         count_down(short_break_sec)
    #     elif reps == 8:
    #     #   if it's the 8th reps
    #         count_down(long_break_sec)
    #         game_on = False

    reps += 1
    if reps % 8 == 0:
    #   if it's the 8th reps
        timer.config(text="Break", fg=RED)
        count_down(long_break_sec)
        checked += "✅︎"
    elif reps % 2 == 0:
    #   if it's the 2nd/4th/6th reps
        timer.config(text="Break", fg=PINK)
        count_down(short_break_sec)
        checked += "✅︎"
    else:
    #   if it's the 1st/3rd/5th/7th reps
        timer.config(text="Go")
        count_down(work_sec)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count_number):
    # canvas.itemconfig(timer_text, text=count_number)
    # if count_number > 0:
    #     # print(count_number)
    #     window.after(1000, count_down, count_number - 1)

    count_min = math.floor(count_number / 60)
    count_sec = count_number % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    #   https://stackoverflow.com/questions/11328920/is-python-strongly-typed
    #   talk about Python is strongly dynamically typed language.
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    global timer_countdown
    if count_number > 0:
        # print(count_number)
        timer_countdown = window.after(1000, count_down, count_number - 1)
    else:
        start_timer()
        # checked = ""
        # work_sessions = math.floor(reps/2)
        # for _ in range(work_sessions):
        #     checked += "✅︎"
        slots_checked.config(text=checked)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


timer = Label(text="Timer", font=(FONT_NAME, 55), fg=GREEN, bg=YELLOW)
timer.grid(column=1, row=0)

start = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start.grid(column=0, row=2)
# how to get rid of the edge & adjust position to right side?
# simply highlightbackground=YELLOW

reset = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset.grid(column=2, row=2)
# how to get rid of the edge & adjust position to right side?
# simply highlightbackground=YELLOW

slots_checked = Label(bg=YELLOW)
slots_checked.grid(row=3, column=1)
# how to get rid of the edge & adjust position to right side?
# this time is bg=YELLOW




window.mainloop()






