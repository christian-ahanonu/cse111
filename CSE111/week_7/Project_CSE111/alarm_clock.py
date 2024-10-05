
'''
Personal Project: Alarm Clock
Instructor: Thomas Reid
Class: Programming with Functions CSE111
Student: Christian I. Ahanonu
'''


# from time import strftime 
from tkinter import * 
from tkinter import ttk

import time
from datetime import datetime
from pygame import mixer


root = Tk() # This is the main GUI window 
root.title('Alarm Clock') # This is the title at the top of the GUI window

root = ttk.Frame(root, padding='50')
root.grid(row=0, column=0)

 
def setalarm():
    '''sets an alarm by calling alarm clock method 
        by passing the alarmtime as argument;
        Parameter: Nil
        Return: nothing
        ''' 
    # get the hour, minute, and seconds values from the user
    alarmtime=f"{hrs.get()}:{mins.get()}:{secs.get()}"
    print(alarmtime)
    if(alarmtime!="::"):
        # call the alarmclock function and pass in the alarmtime var as the argument
        alarmclock(alarmtime) 

def alarmclock(alarmtime, max_iterations=None):
    '''Retrieve the current time and store it in a specific format
    and compare it against the setalarm.  
    Parameter: 
        alartime: the setalarm value
        max_iterations: No. of times the loops should repeat
    Return: nothing
    ''' 
    iterations = 0

    while max_iterations is None or iterations < max_iterations:
        # delay time by 1 second
        time.sleep(1)

        # The current time stored in a specified formate 
        time_now = datetime.now().strftime("%H:%M:%S")
        print(time_now)

        if time_now==alarmtime:
            # Wakeup label for any time the alarm goes off
            Wakeup = Label(root, font = ('arial', 15, 'bold'),
            text = "Wake up!Wake up!Wake up",bg="DodgerBlue2",fg="white").grid(row=6,columnspan=3)
            print("wake up!")

            mixer.init()
            # change/specify the file path to the song so that when the set alarm time goes off
            # the song will play. If you don't do this the alarm won't go off. For example;
            # if the folder containing all the files is stored in the desktop, copy the file path
            # of the music stored on the desktop and replace it with file path below. 
            mixer.music.load(r'C:\Users\Christian Ahanonu\Desktop\Project_CSE111\AOT.mp3')
            mixer.music.play()
            break

        iterations += 1


# string variables that stores the hour, minute, and second's 
# value entered by the user before setting an alarm 
hrs=StringVar()
mins=StringVar()
secs=StringVar()

# label that displays as "Take a short nap"
greet=Label(root, font = ('arial', 20, 'bold'), 
text="Take a short nap!").grid(row=1,columnspan=3)

# Take a specified hour from the user
hrbtn=Entry(root,textvariable=hrs,width=4,font =('arial', 20, 'bold'))
hrbtn.grid(row=2,column=1)
hrbtn.focus()

# Take the specified minute from the user
minbtn=Entry(root,textvariable=mins,
width=4,font = ('arial', 20, 'bold')).grid(row=2,column=2)

# Take a specified second from the user
secbtn=Entry(root,textvariable=secs,
width=4,font = ('arial', 20, 'bold')).grid(row=2,column=3)

# set alarm button
setbtn=Button(root,text="set alarm",command=setalarm,bg="DodgerBlue2",
fg="white",font = ('arial', 20, 'bold')).grid(row=4,columnspan=3)
  

# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    mainloop()

