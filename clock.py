# Developer: Saeed Adam Abdulhamid
# work email : saeed@dcrowdalpha.com
# Instagram : @saeedulkudry
# Date: 2nd Dec 2022
# Time: 6:43am
# Place: Naibawa
# State : Kano
# Country : Nigeria


import datetime
from tkinter import *
from tkinter import ttk
import webbrowser
from tkinter.tix import Balloon

# Instantiate Tk class
app = Tk()



# Stop from resizing
app.resizable(0, 0)

# Define the title bar te
app.title("Project 001")

# Set the height and width of the window
app.geometry("250x200")

# change the app bg to white
app.config(background="white")

# time updater function
def print_date():
    x = datetime.datetime.now()
    my_label.config(text = str(x.strftime("%H:%M:%S %a")))

    # makes the func loop for ever!
    app.after(1000, print_date)

# Label for the first text
my_label = ttk.Label(app, text="Pinned Clock", font=(10), background="white")
my_label.pack()

# Time Placeholder
my_label = ttk.Label(app, text="00:00", font=("Helvetica", 30, "bold"), background="white")
my_label.pack()

# Calls print_date after sec
app.after(1000, print_date)
    


url = "http://saeed.dcrowdalpha.com"
bt = ttk.Button(app, text="Visit me", command=lambda: webbrowser.open(url, 2))
bt.pack()


# Makes the app run
app.mainloop()