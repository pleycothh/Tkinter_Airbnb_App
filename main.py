import pandas as pd
import tkinter as tk
#from tkinter import *
#from PIL import ImageTK, Image


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

def get_neighbour(key): # filter the data with key input
    if key == '':
        new_data = data
    else:
        print('key', key)
        filt = data['neighbourhood'].isin(key)    # file list key input at database
        new_data = data.loc[filt]                 # return the data with filter applied
      # idea: make key global, then only one universal key for key term search

 #   print('new data', new_data)
    clear_tabel()              # clear the label
    show_tabel_title(data)     # display the title of data input
    show_tabel_body(new_data)  # display all data from body
    #return new_data


def print_selection(): # gerate the key dictionary from check box
    result = {"Sydney":0,"Manly":0} #,3:0,4:0,5:0,6:0,7:0,8:0
    if var1.get() == 1:
        var = {"Sydney": 1}
        result.update(var)
      #  checkBox_label.config(text= str(result[1] + result[2]))
    elif var1.get() == 0:
        var = {"Sydney": 0}
        result.update(var)
       # checkBox_label.config(text=str(result[1] + result[2]))

    if var2.get() == 1:
        var = {"Manly": 1}
        result.update(var)
        #checkBox_label.config(text=str(result[1] + result[2]))
    elif var2.get() == 0:
        var = {"Manly": 0}
        result.update(var)

    checkBox_label.config(text=str(result)) # display the table based on check box result
    get_checkbox(result) # call convert function for each action loop

def get_checkbox(dic): # convert key dictionry to list
    new_value = []
    for (key, value) in dic.items():
        if value == 1:
            new_value.append(key)
  #  print(type(new_value))
    get_neighbour(new_value) # call filter function after convert

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
    status = tk.Label(fr_table, text="item received : "+str(len(data_input))+" of 36662", bd=1).grid(row=r+2, column=0)

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
keyWord_label = tk.Label(fr_buttons, text="Enter Key Word below:")           # create label
e = tk.Entry(fr_buttons,width =10, borderwidth = 2)                          # text box
btn_Suburb = tk.Button(fr_buttons, text="Search",command=getKey)             # search button
suburb_label = tk.Label(fr_buttons, text="Choice Suburb below:")             # create label

#----------- check box ------------------

var1 = tk.IntVar()
var2 = tk.IntVar()
#var3 = tk.IntVar()
#var4 = tk.IntVar()
#var5 = tk.IntVar()
#var6 = tk.IntVar()
#var7 = tk.IntVar()
#var8 = tk.IntVar()
btn_Checkbutton_1 = tk.Checkbutton(fr_buttons, text="Sydney", variable=var1, onvalue=1, offvalue=0,command=print_selection)    # Radio Buttons
btn_Checkbutton_2 = tk.Checkbutton(fr_buttons, text="Manly" , variable=var2, onvalue=1, offvalue=0,command=print_selection)     # Radio Buttons
#btn_Checkbutton_3 = tk.Checkbutton(fr_buttons, text="Leichhardt", variable=var3, onvalue=1, offvalue=0,command=print_selection)    # Radio Buttons
#btn_Checkbutton_4 = tk.Checkbutton(fr_buttons, text="Wollahra", variable=var4, onvalue=1, offvalue=0,command=print_selection)    # Radio Buttons
#btn_Checkbutton_5 = tk.Checkbutton(fr_buttons, text="North Sydney", variable=var5, onvalue=1, offvalue=0,command=print_selection)    # Radio Buttons
#btn_Checkbutton_6 = tk.Checkbutton(fr_buttons, text="Waverley", variable=var6, onvalue=1, offvalue=0,command=print_selection)    # Radio Buttons
#btn_Checkbutton_7 = tk.Checkbutton(fr_buttons, text="Mosman", variable=var7, onvalue=1, offvalue=0,command=print_selection)    # Radio Buttons
#btn_Checkbutton_8 = tk.Checkbutton(fr_buttons, text="Pittwater", variable=var8, onvalue=1, offvalue=0,command=print_selection)    # Radio Buttons

checkBox_label = tk.Label(fr_buttons, bg='white', width=20, text='empty')



keyWord_label.grid(row = 0, column = 0)                                   # label
e.grid(row = 1, column = 0, columnspan=3)                                # text box
btn_Suburb.grid(row=2, column=0, sticky="ew")                            # search button
suburb_label.grid(row = 3, column = 0)                                   # label

btn_Checkbutton_1.grid(row=4, column=0)                                        # check Buttons
btn_Checkbutton_2.grid(row=5, column=0)                                        # check Buttons
#btn_Checkbutton_3.grid(row=6, column=0)                                        # check Buttons
#btn_Checkbutton_4.grid(row=7, column=0)                                        # check Buttons
#btn_Checkbutton_5.grid(row=8, column=0)                                        # check Buttons
#btn_Checkbutton_6.grid(row=9, column=0)                                        # check Buttons
#btn_Checkbutton_7.grid(row=10, column=0)                                        # check Buttons
#btn_Checkbutton_8.grid(row=11, column=0)                                        # check Buttons
checkBox_label.grid(row=12, column=0)

###################### right frame ###############################


###################### loop #############################

window.mainloop()