# Q2
import tkinter as tk
from tkinter import messagebox
import calendar # importing calendar module

def show_calendar():
    year = year_entry.get()
 #The try and ValueError are part of the exception handling mechanism in 
 #Python.
 # They are used to handle potential errors that may occur during the execution of a program.

    try:
        year = int(year)
        cal = calendar.calendar(year)
        calendar_text.delete("1.0", tk.END)
        calendar_text.insert(tk.END, cal)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid year.")

window = tk.Tk()  # it creates the main window or root window for our tinkter program
window.title("Calendar Application")  # giving title

year_label = tk.Label(window, text="Enter Year:")
year_label.pack()
# packing the label function
# when we pack a widget into a window, tkinter sizes the window as small as it can be
# while fully encompassing the widget
year_entry = tk.Entry(window)
year_entry.pack()

show_calendar_button = tk.Button(window, text="Show Calendar", command=show_calendar)
show_calendar_button.pack()   # giving button

calendar_text = tk.Text(window)
calendar_text.pack()

window.mainloop()
#  This mainloop() call will keep your application running
#  until the user closes the window or exits the program.
