import math
import tkinter as tk
from tkinter import Frame,Label,Button
from number_entry import IntEntry


def main():
    root = tk.Tk()

    frm_main = Frame(root)
    frm_main.master.title("Area_Rectangle")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    root.mainloop()

def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "Age:"
    lbl_w = Label(frm_main, text="Width: ")
    lbl_h = Label(frm_main, text="Height: ")

    # Create an integer entry box where the user will enter her age.
    ent_w = IntEntry(frm_main, width=4, lower_bound=0, upper_bound=90)
    ent_h = IntEntry(frm_main, width=4, lower_bound=0, upper_bound=90)

    # Create a label that displays "years"

    # Create a label that displays "Rates:"

    # Create labels that will display the results.
    lbl_area = Label(frm_main, width=6)

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")

    btn_submit = Button(frm_main, text="Submit")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_w.grid(row=0, column=0, padx=3, pady=3)
    ent_w.grid(row=1, column=0, padx=3, pady=3)
    lbl_h.grid(row=0, column=1, padx=3, pady=3)
    ent_h.grid(row=1, column=1, padx=3, pady=3)
    lbl_area.grid(row=2, column=0, padx=3, pady=3)

    btn_submit.grid(row=3,column=2, padx=3, pady=3,columnspan=4, sticky='w')
    btn_clear.grid(row=4, column=2, padx=3, pady=3, columnspan=4, sticky="e")


    # This function will be called each time the user releases a key.
    def calculate():
        """Compute and display the user's slowest
        and fastest beneficial heart rates.
        """
        try:
            # Get the user's age.
            w = int(ent_w.get())
            h = int(ent_h.get())

            area = w * h

            # Display the slowest and fastest benficial
            # heart rates for the user to see.
            lbl_area.config(text=f"{area:.2f}")

        except ValueError as v:
            print(v)
            # When the user deletes all the digits in the age
            # entry box, clear the slowest and fastest labels.
            lbl_area.config(text="")


    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_w.clear()
        ent_h.clear()
        ent_w.focus()

    # Bind the calculate function to the age entry box so
    # that the computer will call the calculate function
    # when the user changes the text in the entry box.
    


    # Bind the clear function to the clear button so
    # that the computer will call the clear function
    # when the user clicks the clear button.
    btn_clear.config(command=clear)
    btn_submit.config(command=calculate)

    # Give the keyboard focus to the age entry box.
    ent_w.focus()

if __name__ == "__main__":
    main()