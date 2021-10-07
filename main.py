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

def getKey(name):
    new_data = data[data['name'] == name]
    # modify the database

    # create new database
    print('get key')
    # update the result
    return new_data
  #  print(name)

def show_tabel_body(data_input):
    r = 0
    for rows in data_input.values:
        c = 0
        for col in rows:
            # i've added some styling
            label = tk.Label(fr_table, width=0, height=2, text=col)
            label.grid(row=r, column=c)
            c += 1
        r += 1

def show_tabel_title(data_input):
    header = data_input.columns
    c = 0
    for head in header:
        head_label = tk.Label(fr_table, width=0, height=2, text=head)
        head_label.grid(row=0, column=c)
        c += 1
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


btn_Suburb = tk.Button(fr_buttons, text="Search",command=lambda: getKey)



# display
e.grid(row = 0, column = 0, columnspan=3)
btn_Suburb.grid(row=1, column=0, sticky="ew")




###################### table ###############################

#------------------- title--------------------------




show_tabel_title(data) # display the title of data input

#------------------- body--------------------------
# r and c tell us where to grid the labels

body = data.head(10) # show first ten value

show_tabel_body(body) # display all data from body




###################### loop #############################

window.mainloop()