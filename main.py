#By Andrew Wang
import time
from tkinter import *
from datetime import datetime

root = Tk()
root.title("Day of the Week")
root.geometry("500x500")

def resetDay():
    with open('day.txt', 'w') as f:
        f.write("0")

def catchErrors():
    try:
        with open('day.txt', 'r') as e:
            read = e.read()
    except:
        print("The txt file does not exist")
        print("Creating new txt file...")
        time.sleep(3)
        f= open("day.txt","w+")

def checkTxt():
    catchErrors()
    with open('day.txt', 'r') as e:
        read = e.read()
        if read == "" or len(read) > 1:
            print("The txt file is empty or invalid.")
            resetDay()
        elif len(read) == 1:
            if not str(read).isdigit():
                print("The txt file contains an invalid input.")
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
    print(str(datetime.now().strftime("%A, %B %d, %Y")) + " | Letter Day: " + day)
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

def update_time():
    
    curr_time = datetime.now().strftime("%H:%M:%S")
    curr_day = datetime.now().strftime("%A")
    
    time.config(text=curr_time)
    root.after(1000, update_time)
    if str(curr_time) == "24:00:00":
        weekday_label.config(text=curr_day)
        if str(curr_day) == "Saturday" or (curr_day) == "Sunday":
            print("Today is a weekend! No School!")
        else:
            changeDay(True)

print("Day of the week: By Andrew Wang")
print("")
read = checkTxt()

if (read != "") and (not len(read)>1) and (read.isdigit()):
    with open('day.txt', 'w') as f:
        f.write(read)
    day = checkDay(read)
    print(str(datetime.now().strftime("%A, %B %d, %Y")) + " | Letter Day: " + day)
    letter_label = Label(root,font="Arial 20 bold",text="Letter Day:")
    letter_label.place(x=185,y=200)
    day_label = Label(root,font="Arial 50 bold",text=day)
    day_label.place(x=225,y=250)
    prev_button = Button(root, text="previous", command = lambda: changeDay(False))
    prev_button.place(x=10,y=450)
    add_button = Button(root, text="next", command = lambda: changeDay(True))
    add_button.place(x=70,y=450)
    time = Label(root, font="Arial 20 bold", text=datetime.now().strftime("%H:%M:%S"))
    time.place(x=380,y=450)
    weekday_label = Label(root, font="Arial 15 bold", text=datetime.now().strftime("%A"))
    weekday_label.place(x=380,y=420)
    update_time()
else:
    print("Restarting day of the week...")
    time.sleep(2)
    print("Please restart program to use.")
    time.sleep(5)

root.mainloop()
