from allFunction import *
import tkinter as tk

###################### load functions ##################################
data = load()

def myClick():
    # create a Label Widget
    hello = "Hello " + e.get() # get entry value as label
    myLabel1 = tk.Label(fr_buttons, text=hello)

    # pack label to root window
    myLabel1.grid(row=5)

###################### window #########################
window = tk.Tk()
window.title("Simple Text Editor")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

###################### frames #############################
# create two frame
fr_buttons = tk.Frame(window,padx=5, pady=5)
fr_table = tk.Frame(window,padx=5, pady=5)
# display two frame
fr_buttons.grid(row=0, column=0, sticky="ns",padx=5, pady=5)
fr_table.grid(row=0, column=1, sticky="nsew",padx=5, pady=5)

###################### buttons #############################
# create two button under button frame
e = tk.Entry(fr_buttons,width =10, borderwidth = 2)


btn_Suburb = tk.Button(fr_buttons, text="Search",command=lambda: myClick())



# display
e.grid(row = 0, column = 0, columnspan=3)
btn_Suburb.grid(row=1, column=0, sticky="ew")




###################### table ###############################

#------------------- title--------------------------
header = data.columns
print(header)
c = 0
for head in header:
    head_label = tk.Label(fr_table, width=0, height=2, text=head)
    head_label.grid(row=0, column=c)
    c += 1


#------------------- body--------------------------
# r and c tell us where to grid the labels
dRow = 0
r = 1
for rows in data.values:
    c = 0
    for col in rows:
        # i've added some styling
        label = tk.Label(fr_table, width=0, height=2, text=col)
        label.grid(row=r, column=c)
        c += 1
    r += 1
    dRow += 1
    if dRow == 10:
        break


###################### loop #############################

window.mainloop()