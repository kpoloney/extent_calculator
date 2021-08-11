from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as font

root = Tk()
root.title("Extent Calculator")

ttk.Separator(root, orient=HORIZONTAL).grid(row=1, columnspan=4,sticky="ew")
ttk.Separator(root, orient=HORIZONTAL).grid(row=5, columnspan=4, pady=10,sticky="ew")

# Titles
title_unit = Label(root, text = "Unit")
title_unit['font'] = font.Font(weight='bold', size=14)
title_unit.grid(row=0, column=0)

title_quant = Label(root, text="Quantity")
title_quant['font'] = font.Font(weight='bold', size=14)
title_quant.grid(row=0, column=1)

# title_total = Label(root, text = "Unit total")
# title_total.grid(row=0, col=2)

# Small box
unit1 = Label(root, text = "Archival Box - Small")
unit1['font'] = font.Font(size=11)
unit1.grid(row = 2, column = 0, sticky="w", pady=5)

box_small = Entry(root, text = "Quantity1")
box_small.grid(row = 2, column = 1, pady=5)

# unit_total1 = Label(root, text = "Total")
# unit_total1_content = StringVar()
# unit_total1['textvariable'] = unit_total1_content
# unit_total1.grid(row=1, col = 2)

# standard box
unit2 = Label(root, text = "Archival Box - Standard")
unit2['font'] = font.Font(size=11)
unit2.grid(row = 3, column = 0, sticky='w', pady=5)

box_std = Entry(root, text = "Quantity2")
box_std.grid(row=3, column=1, pady=5)

# unit_total2 = Label(root, text = "Total")
# unit_total2_content = StringVar()
# unit_total2['textvariable'] = unit_total1_content
# unit_total2.grid(row=1, col = 3)

# URC Box
unit3 = Label(root, text = "URC Tote Box")
unit3['font'] = font.Font(size=11)
unit3.grid(row = 4, column = 0, sticky='w', pady=5)

urc = Entry(root, text="Quantity3")
urc.grid(row=4, column=1, pady=5)

# Total all
total  = Label(root, text="Total Extent")
total['font'] = font.Font(weight='bold')
total.grid(row=7, column=0, sticky='w')
result = Label(root, text="Total", bg="white", font="bold", padx=30)
result_content = StringVar()
result['textvariable'] = result_content
result.grid(row = 7, column = 1)

def calc_ext():
    try:
        if len(box_small.get())==0:
            total1 = 0
        else:
            val1 = int(box_small.get())
            total1 = val1 * 6.25
        if len(box_std.get())==0:
            total2 = 0
        else:
            val2 = int(box_std.get())
            total2 = val2*12.5
        if len(urc.get())==0:
            total3 = 0
        else:
            val3 = int(urc.get())
            total3 = val3 * 33.33
        result_content.set(str(total1+total2+total3)+" cm")
    except:
        result_content.set("Invalid value")

calc = Button(root, text="Calculate Total", relief = "groove", bg="light gray", padx=5, pady=5, command=calc_ext)
calc['font'] = font.Font(size=12)
calc.grid(row = 6, column = 1, pady=10, padx=5)

def clear_vals():
    box_small.delete(0,END)
    box_std.delete(0,END)
    urc.delete(0,END)
    result_content.set("")

clear = Button(root, text = "Clear Values", relief = "groove", bg="light gray", padx=5, pady=5, command=clear_vals)
clear['font'] = font.Font(size=12)
clear.grid(row=6, column=0, pady=10)

root.mainloop()