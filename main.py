import time
from tkinter import *
from datetime import datetime

root = Tk()
root.title("Day of the Week")
root.geometry("500x500")

def resetDay():
    with open('day.txt', 'w') as f:
        f.write("0")

def checkTxt():
    with open('day.txt', 'r') as e:
        read = e.read()
        if read == "":
            print("The txt file is empty.")
            resetDay()
        return read
    
def checkDay(read):
    read = int(read)
    if read == 0:
        return "A"
    elif read == 1:
        return "B"
    elif read == 2:
        return "C"
    elif read == 3:
        return "D"
    elif read == 4:
        return "E"
    elif read == 5:
        return "F"
    else:
        resetDay()

def updateDate():
    global day
    day = checkDay(read)
    day_label.config(text=day)
    
def changeDay(boolean):
    global read
    global day
    get_day = int(read)
    if boolean:
        if get_day+1 == 6:
            get_day = -1
        with open('day.txt', 'w') as f:
            f.write(str(get_day+1))
            read = str(get_day+1)
    else:
        if get_day-1 == -1:
            get_day = 1
        with open('day.txt', 'w') as f:
            f.write(str(get_day-1))
            read = str(get_day-1)
    updateDate()

"""
def update_time():
    curr_time = datetime.now().strftime("%H:%M:%S")
    print(curr_time)
"""
read = checkTxt()


if read != "":
    with open('day.txt', 'w') as f:
        f.write(read)
    day = checkDay(read)
    print(day)
    letter_label = Label(root,font="Arial 20 bold",text="Letter Day:")
    letter_label.place(x=185,y=200)
    day_label = Label(root,font="Arial 50 bold",text=day)
    day_label.place(x=225,y=250)
    prev_button = Button(root, text="previous", command = lambda: changeDay(False))
    prev_button.place(x=10,y=450)
    add_button = Button(root, text="next", command = lambda: changeDay(True))
    add_button.place(x=70,y=450)
else:
    print("Restarting day of the week...")
    time.sleep(2)
    print("Please restart program to use.")
    time.sleep(5)

root.mainloop()
