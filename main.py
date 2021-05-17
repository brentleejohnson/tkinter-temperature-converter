# Temperature Converter
# Import Tkinter


import tkinter as tk
from tkinter.messagebox import showerror


# root window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("620x400")
root.resizable(False, False)

# helps the conversions of fahrenheit to celcius
fahrenheit_to_celcius = ""


def fahrenheit_to_celcius(f):
    """ Convert fahrenheit to celcius
    """
    result = (f - 32) * 5/9
    G_entry.insert(0, round(result, 2))


def celsius_to_fahrenheit(c):
    result = c*9/5+32
    G_entry.insert(0, round(result, 2))


# activates the one and disables the other
def activate_f_to_c():
    F_entry.config(state=tk.NORMAL)
    C_entry.config(state=tk.DISABLED)
    global fahrenheit_to_celsius
    fahrenheit_to_celsius = "Fahrenheit"


# activates the one and disables the other
def activate_c_to_f():
    C_entry.config(state=tk.NORMAL)
    F_entry.config(state=tk.DISABLED)
    global fahrenheit_to_celsius
    fahrenheit_to_celsius = "Celsius"


def clear_results():
    G_entry.delete(0, tk.END)


def conversion():
    global fahrenheit_to_celsius
    if fahrenheit_to_celsius == "Fahrenheit":
        if test_if_float(float(F_entry.get())):
            fahrenheit_to_celsius(float(F_entry.get()))
        else:
            tk.messagebox.showinfo("Error", " Enter a number")
    elif fahrenheit_to_celsius == "Celsius":
        print(type(F_entry.get()))

        if test_if_float(float(C_entry.get())):

            celsius_to_fahrenheit(float(C_entry.get()))
        else:
            tk.messagebox.showinfo("Error", " Enter a number")


def test_if_float(f):
    if type(f) == float:
        return True
    else:
        return False


def close_program():
    msg_box = tk.messagebox.askquestion("Exit Application", "Are you sure you want to exit the application", icon="warning")
    if msg_box == "yes":
        root.destroy()
    else:
        tk.messagebox.showinfo("Return", "You will now return to the application screen")


# The Fahrenheit symbol and entry window
F_frame = tk.LabelFrame(root, text="Fahrenheit -- Celsius", fg="#660708", width=205, height=125)
F_frame.place(x=80, y=70)
F_entry = tk.Entry(F_frame, bg="#E5383B", width=15, state=tk.DISABLED)
F_entry.place(x=20, y=60)
F_btn = tk.Button(root, text="Activate - Fahrenheit to Celsius", fg="#660708", command=activate_f_to_c)
F_btn.place(x=70, y=200)

# The Celsius symbol and entry window
C_frame = tk.LabelFrame(root, text="Celsius -- Fahrenheit ", fg="#660708", width=205, height=125)
C_frame.place(x=350, y=70)
C_entry = tk.Entry(C_frame, bg="#E5383B", width=15, state=tk.DISABLED)
C_entry.place(x=20, y=60)
C_btn = tk.Button(root, text="Activate - Celsius to Fahrenheit", fg="#660708", command=activate_c_to_f)
C_btn.place(x=340, y=200)

# close program
# calculate conversion and clear buttons
G_entry = tk.Entry(root, bg="#E5383B", width=25)
G_entry.place(x=250, y=300)
btn1 = tk.Button(root, text="Clear", fg="#660708", command=clear_results)
btn1.place(x=500, y=300)
btn2 = tk.Button(root, text="Calculate the conversion", fg="#660708", command=conversion)
btn2.place(x=50, y=300)
btn3 = tk.Button(root, text="Close Program", fg="#660708", command=close_program)
btn3.place(x=470, y=350)


# Run the program
root.mainloop()
