import pandas as pd
import tkinter as tk

###################### load functions ##################################

def load(path="src/listings_summary_dec18.csv"):
    df = pd.read_csv(path)
    return df

def clear_tabel():
   for widgets in fr_table.winfo_children():
      widgets.destroy()

#------------------------------- functions --------------------------------------

def getKey():
    key = e.get()
    if key == '':
        new_data = data
    else:
        new_data = data[data['neighbourhood'] == key]

    print(new_data)
    clear_tabel()              # clear the label
    show_tabel_title(data)     # display the title of data input
    show_tabel_body(new_data)  # display all data from body
    #return new_data



#--------------------------------- show --------------------------------------

def show_tabel_body(data_input):
    body = data_input.head(16)  # show first ten value
    r = 1
    for rows in body.values:
        c = 0
        for col in rows:
            # i've added some styling
            label = tk.Label(fr_table, width=0, height=2, text=col)
            label.grid(row=r, column=c)
            c += 1
        r += 1

    # display the data status after tabel
    status = tk.Label(fr_table, text="data recived: "+ str(len(data_input)) +" of 36662", bd=1).grid(row=r+2, column=0)

def show_tabel_title(data_input):
    header = data_input.columns
    c = 0
    for head in header:
        head_label = tk.Label(fr_table, width=0, height=2, text=head)
        head_label.grid(row=0, column=c)
        c += 1


############################ window ##############################
data = load() # load all data

window = tk.Tk()
window.title("Simple Text Editor")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

###################### create frames #############################
# create two frame
fr_buttons = tk.Frame(window,width=500, height=100,padx=5, pady=5)     # create left frame
fr_table = tk.Frame(window,width=100, height=100,padx=5, pady=5)       # create right frame

# display two frame
fr_buttons.grid(row=0, column=0, sticky="ns",padx=5, pady=5)           # display left frame
fr_table.grid(row=0, column=1, sticky="nsew",padx=5, pady=5)           # display right frame


###################### Left frame ############################
suburb_label = tk.Label(fr_buttons, text="Enter Suburb below")         # create label
e = tk.Entry(fr_buttons,width =10, borderwidth = 2)                    # text box
btn_Suburb = tk.Button(fr_buttons, text="Search",command=getKey)       # search button



suburb_label.grid(row = 0, column = 0)                                 # label
e.grid(row = 1, column = 0, columnspan=3)                              # text box
btn_Suburb.grid(row=2, column=0, sticky="ew")                          # search button


###################### right frame ###############################


###################### loop #############################

window.mainloop()