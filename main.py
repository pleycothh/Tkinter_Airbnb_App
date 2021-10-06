from allFunction import *
import tkinter as tk

###################### load functions ##################################
data = load()

###################### create window #########################
window = tk.Tk()
window.title("Simple Text Editor")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

###################### create weidges #############################
# create two frame
fr_buttons = tk.Frame(window)
fr_table = tk.Frame(window)

# create two button under button frame
btn_open = tk.Button(fr_buttons, text="Open")
btn_save = tk.Button(fr_buttons, text="Save As...")

###################### display weidges #############################

# display two frame
fr_buttons.grid(row=0, column=0, sticky="ns")
fr_table.grid(row=0, column=1, sticky="nsew")
#####################################################################

# create & display table under table frame
# r and c tell us where to grid the labels
dRow = 0
r = 0
for rows in data.values:
    c = 0
    print(rows)
    for col in rows:
        # i've added some styling
        label = tk.Label(fr_table, width=0, height=2, text=col)
        label.grid(row=r, column=c)
        c += 1
    r += 1
    dRow += 1
    if dRow == 10:
        break

################################################################

# display button
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)




window.mainloop()