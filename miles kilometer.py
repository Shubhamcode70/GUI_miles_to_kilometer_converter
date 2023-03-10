from tkinter import *


window = Tk()
# window.minsize(width=300, height=150)
# print(window.grid_size())
window.title("Miles to Kilometer Converter")
window.config(padx=200, pady=200,)

miles_entry = Entry(width=15, font=("Helvetica",12,"normal"), borderwidth=5)
miles_entry.grid(column=2, row=1)

def converter():
    cons = 1.609344
    miles = float(miles_entry.get())
    km = miles * cons
    km_label = Label(text=f"{km} Kilometer", font=("Helvetica",12,"normal"))
    km_label.config(height=2)
    km_label.grid(column=2, row=3)


miles_label = Label(text='Miles', font=("Helvetica",12,"bold"))
miles_label.config(width=7, height=2)
miles_label.grid(column=1, row=1)

equal_label = Label(text=f'Equal to', font=("Helvetica",12,"bold"))
equal_label.config(width=7, height=2, )
equal_label.grid(column=1, row=3, sticky='nsew')


ent_button = Button(text="Calculate", command=converter)
ent_button.config(width=15)
ent_button.grid(column=2, row=4, sticky='nw')
window.mainloop()
