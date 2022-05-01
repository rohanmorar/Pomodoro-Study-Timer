from tkinter import *
from turtle import color, screensize
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
count = 0
timer = None
# ---------------------------- WINDOW POP-UP ------------------------------- # 
def window_pop_up():
        window.lift()
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    window.after_cancel(timer)
    check_mark.configure(text="")
    canvas.itemconfig(timer_text, text=f"00:00")
    title_label.configure(title_label, text = "Pomodoro")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def s_button_click():
    global reps
    global count
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.configure(title_label, text = "Recess 🥳")
        count_down(long_break_sec)
        window_pop_up()

    elif reps % 2 == 0:
        title_label.configure(title_label, text = "Break 😮‍💨")
        count_down(short_break_sec)
        window_pop_up()
    else:
        title_label.configure(text = "Focus 🧠")
        count_down(work_sec)
        window_pop_up()
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    
    if count_sec == 0:
        count_sec ="00"
    elif -1 < count_sec < 10:
        count_sec = f"0{count_sec}" 
    if count_min == 0:
        count_min = "00"
    elif -1 < count_min < 10:
        count_min = f"0{count_min}" 

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        s_button_click()
        t = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            t += "✔︎"
        check_mark.configure(text=t, fg="green", font=(FONT_NAME, 40, "normal"))

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx= 100, pady= 50, bg = GREEN)

canvas = Canvas(width=200, height = 224, bg=GREEN, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image = img)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

# count_down(5)

start_button = Button(text="START",highlightbackground=GREEN,command=s_button_click)
start_button.grid(column=1,row=3)

reset_button = Button(text="RESET",highlightbackground=GREEN, command=reset_timer)
reset_button.grid(column=3,row=3)

title_label = Label(text="Pomodoro",highlightthickness=0, bg=GREEN, font=(FONT_NAME, 50, "bold"), fg="green")
title_label.grid(column=2,row=0)

check_mark = Label(bg=GREEN, fg=GREEN)
check_mark.grid(column=2,row=4)

canvas.grid(column=2,row=2, padx=25,pady=25)

window.mainloop()