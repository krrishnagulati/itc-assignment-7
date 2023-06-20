import tkinter as tk

def button_click(number):#This function is called when a number button (0-9) is clicked
    current = input_field.get()
    input_field.delete(0, tk.END)
    input_field.insert(tk.END, current + str(number))

def button_clear(): #This function is called when the clear button ("C") is clicked.
    input_field.delete(0, tk.END)

def button_operation(operation):#This function is called when an operation button (+, -, *, /) is clicked.
    current = input_field.get()
    input_field.delete(0, tk.END)
    input_field.insert(tk.END, current + operation)

def button_equal():#This function is called when the equal button (=) is clicked.
    expression = input_field.get()
 #The try and ValueError are part of the exception handling mechanism in 
 #Python.
 # They are used to handle potential errors that may occur during the execution of a program.
    try:
        result = eval(expression)
        input_field.delete(0, tk.END)
        input_field.insert(tk.END, result)
    except:
        input_field.delete(0, tk.END)
        input_field.insert(tk.END, "Error")

window = tk.Tk()  # it creates the main window or root window for our tinkter program
window.title("Calculator")  # giving title

input_field = tk.Entry(window, width=30)
input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_1 = tk.Button(window, text="1", padx=20, pady=10, command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", padx=20, pady=10, command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", padx=20, pady=10, command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", padx=20, pady=10, command=lambda: button_click(4))
button_5 = tk.Button(window, text="5", padx=20, pady=10, command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", padx=20, pady=10, command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", padx=20, pady=10, command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", padx=20, pady=10, command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", padx=20, pady=10, command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", padx=20, pady=10, command=lambda: button_click(0))
# creating nine "buttons" for first nine different digits
# padx is used to specify the horizontal padding, which adds extra space
#  to the left and right of the button's text or contents.

#pady is used to specify the vertical padding,
#  which adds extra space above and below the button's text or contents

button_add = tk.Button(window, text="+", padx=20, pady=10, command=lambda: button_operation("+"))
button_subtract = tk.Button(window, text="-", padx=20, pady=10, command=lambda: button_operation("-"))
button_multiply = tk.Button(window, text="*", padx=20, pady=10, command=lambda: button_operation("*"))
button_divide = tk.Button(window, text="/", padx=20, pady=10, command=lambda: button_operation("/"))

button_clear = tk.Button(window, text="C", padx=20, pady=10, command=button_clear)
button_equal = tk.Button(window, text="=", padx=20, pady=10, command=button_equal)

# Positioning the buttons on the grid inbuilt function of tkinter using rows and columns

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=0)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

button_clear.grid(row=4, column=1)
button_equal.grid(row=4, column=2)


window.mainloop()
#  This mainloop() call will keep your application running
#  until the user closes the window or exits the program.
