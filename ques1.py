import tkinter as tk

def calculate_gst():#  #The try and ValueError are part of the exception handling mechanism in 
    #Python.
    # They are used to handle potential errors that may occur during the execution of a program.
    try:
        original_cost = float(original_cost_entry.get())
        net_price = float(net_price_entry.get())

        gst_rate = ((net_price - original_cost) * 100) / original_cost
        gst_result_label.config(text="GST Rate: {:.2f}%".format(gst_rate))
    except ValueError:
        gst_result_label.config(text="Invalid input. Please enter numbers only.")

# Creating  the main window
window = tk.Tk() #
# It creates the main window or the root window for our Tkinter application.
window.title("GST Tax Finder Calculator") # giving title

# Create the labels and entry fields
original_cost_label = tk.Label(window, text="Original Cost:")
original_cost_label.pack()   # packing the label function
# when we pack a widget into a window, tkinter sizes the window as small as it can be
# while fully encompassing the widget

original_cost_entry = tk.Entry(window)
original_cost_entry.pack()

net_price_label = tk.Label(window, text="Net Price:")
net_price_label.pack()

net_price_entry = tk.Entry(window)
net_price_entry.pack()

calculate_button = tk.Button(window, text="Calculate GST", command=calculate_gst)
calculate_button.pack()  # giving button to program

gst_result_label = tk.Label(window, text="")
gst_result_label.pack()

# Run the main window's event loop
window.mainloop()

#  This mainloop() call will keep your application running
#  until the user closes the window or exits the program.