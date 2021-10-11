import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import  FigureCanvasTkAgg, NavigationToolbar2Tk



###################### load functions ##################################

def load(path="src/listings_summary_dec18.csv"):
    df = pd.read_csv(path)
    new_df = df[['name','host_name', 'neighbourhood', 'room_type', 'price', 'latitude', 'longitude']]
    print(new_df.shape)

    return new_df

def clear_tabel():
   for widgets in second_frame.winfo_children():
      widgets.destroy()


#------------------------------- key search function group --------------------------------------


def get_key(): # key word search by contains
    key = e.get()
    filt = data['name'].str.contains(str(key), na=False) # for string contains from 'everything', check key word
    new_data = data.loc[filt]

    global dynamic_database
    dynamic_database = new_data # store result data into global database

    clear_tabel()  # clear the label
    show_tabel_title(data)  # display the title of data input
    show_tabel_body(new_data)  # display all data from body

    window.geometry("1080x801")
#------------------------------ check box function group--------------------------

def get_selection(): # gerate the key dictionary from check box
    result = {"Sydney":0,"Manly":0,"Leichhardt":0,"Woollahra":0,"North Sydney":0,"Waverley":0,"Mosman":0,"Pittwater":0} #,3:0,4:0,5:0,6:0,7:0,8:0
    if var1.get() == 1:
        var = {"Sydney": 1}
        result.update(var)
      #  checkBox_label.config(text= str(result[1] + result[2]))
    elif var1.get() == 0:
        var = {"Sydney": 0}
        result.update(var)
#--------------------------------------
    if var2.get() == 1:
        var = {"Manly": 1}
        result.update(var)
        #checkBox_label.config(text=str(result[1] + result[2]))
    elif var2.get() == 0:
        var = {"Manly": 0}
        result.update(var)
# --------------------------------------
    if var3.get() == 1:
        var = {"Leichhardt": 1}
        result.update(var)
        # checkBox_label.config(text=str(result[1] + result[2]))
    elif var3.get() == 0:
        var = {"Leichhardt": 0}
        result.update(var)
# --------------------------------------
    if var4.get() == 1:
        var = {"Woollahra": 1}
        result.update(var)
        # checkBox_label.config(text=str(result[1] + result[2]))
    elif var4.get() == 0:
        var = {"Woollahra": 0}
        result.update(var)
# --------------------------------------
    if var5.get() == 1:
        var = {"North Sydney": 1}
        result.update(var)
        # checkBox_label.config(text=str(result[1] + result[2]))
    elif var5.get() == 0:
        var = {"North Sydney": 0}
        result.update(var)
# --------------------------------------
    if var6.get() == 1:
        var = {"Waverley": 1}
        result.update(var)
        # checkBox_label.config(text=str(result[1] + result[2]))
    elif var6.get() == 0:
        var = {"Waverley": 0}
        result.update(var)
# --------------------------------------
    if var7.get() == 1:
        var = {"Mosman": 1}
        result.update(var)
        # checkBox_label.config(text=str(result[1] + result[2]))
    elif var7.get() == 0:
        var = {"Mosman": 0}
        result.update(var)
# --------------------------------------
    if var8.get() == 1:
        var = {"Pittwater": 1}
        result.update(var)
        # checkBox_label.config(text=str(result[1] + result[2]))
    elif var8.get() == 0:
        var = {"Pittwater": 0}
        result.update(var)
# --------------------------------------

    checkBox_label.config(text=str(result)) # display the table based on check box result
    get_checkbox(result) # call convert function for each action loop
    window.geometry("1080x801")

def get_checkbox(dic): # convert key dictionry to list
    new_value = []
    for (key, value) in dic.items():
        if value == 1:
            new_value.append(key)
    get_neighbour(new_value) # call filter function after convert

def get_neighbour(key): # filter the data with key input
    if key == '':
        new_data = data
    else:
        filt = data['neighbourhood'].isin(key)    # file list key input at database
        new_data = data.loc[filt]                 # return the data with filter applied
        # idea: make key global, then only one universal key for key term search
        # new_data = data.loc[filt, 'nane', 'price']

    global dynamic_database
    dynamic_database = new_data

    clear_tabel()              # clear the label
    show_tabel_title(data)     # display the title of data input
    show_tabel_body(new_data)  # display all data from body

#--------------------------------- price slider function group------------------------------------

def min_price(var):
    global min_p
    min_p = min_price_slider.get()
    #print('price:',min_p,'to', max_p)
    get_price()

def max_price(var):
    global max_p
    max_p = max_price_slider.get()
    #print('price:',min_p,'to', max_p)
    get_price()

def get_price(): # filter the data with key input

    filt = (data['price'] >= min_p)   # file list key input at database
    new_data = data.loc[filt]         # return the data with filter applied

 #   print('new data', new_data)
    clear_tabel()              # clear the label
    show_tabel_title(data)     # display the title of data input
    show_tabel_body(new_data)  # display all data from body

#--------------------------------- plot price function group --------------------------------------
def load_price():

    try:
        price = dynamic_database["price"]
    except:
        price =  data["price"]

    pp=[]
    for i in price:
        pp.append(i)
    pp.sort()
    pw = pp[:35500]
    return pw

def price_graph():
    bnb_price = load_price()
    plt.hist(bnb_price, 50)
    plt.show()

#---------------------------------------- map plot-------------------------------------------
def load_position(data):
    try:
        data = dynamic_database.values
    except:
        data = data.values
   # data = data.values
    pos = []
    latt = []
    lonn = []
    for row in data:
        lat = row[5]
        lon = row[6]
        position = [lat, lon]
        pos.append(position)

    for cor in pos:
        if -33.695 > cor[0] > -34.005 and 151.323 > cor[1] > 150.631:
            latt.append(cor[0])
            lonn.append(cor[1])
        else:
            pass
    return latt, lonn

def map_graph():
    lat, lon = load_position(data)
    img = plt.imread('src/map_2.png')
    fig, ax = plt.subplots()
    # [151,151,35] , [-34.15, -33.5]
    ax.imshow(img, extent=[150.6310, 151.3258, -34.0088, -33.6950])
    ax.scatter(lon, lat, s=0.1, alpha=0.5)

    plt.show()

#--------------------------------- display tabel function group --------------------------------------

def show_tabel_body(data_input):

    body = data_input.head(50)  # show first ten value
    r = 1
    for rows in body.values:
        c = 0
        for col in rows:
            # i've added some styling
            label = tk.Label(second_frame, width=0, height=2, text=col)
            label.grid(row=r, column=c)
            c += 1
        r += 1

    # display the data status after table
    status = tk.Label(second_frame, text="item received : "+str(len(data_input))+" of 36662", bd=1).grid(row=r+2, column=0)
    return body

def show_tabel_title(data_input):
    header = data_input.columns
    c = 0

    for head in header:
        head_label = tk.Label(second_frame, width=0, height=2, text=head)
        head_label.grid(row=0, column=c)
        c += 1

############################ window ##############################
data = load() # load all data
min_p = 0
max_p = 0



window = tk.Tk()
window.geometry("1024x800")
#window.resizable(False,False)
window.title("Airbnb analysis app")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

###################### create frames #############################
# -------------------- create two frame -----------------------------
fr_buttons = tk.Frame(window,width=500, height=100,padx=5, pady=5)     # create left frame
fr_table = tk.Frame(window,padx=5, pady=5)                             # create right frame

# display two frame
fr_buttons.grid(row=0, column=0, sticky="ns",padx=5, pady=5)           # display left frame
fr_table.grid(row=0, column=1, sticky="nsew",padx=5, pady=5)           # display right frame

# ------------------------create secondary control frame --------------------------
fr_searchKey = tk.Frame(fr_buttons, width=500,padx=5, pady=5)
fr_checkBox = tk.Frame(fr_buttons, width=500,padx=5, pady=5)
fr_sliderPrice = tk.Frame(fr_buttons, width=500,padx=5, pady=5)
fr_actionPlot = tk.Frame(fr_buttons, width=500,padx=5, pady=5)

# display secondary control frame
fr_searchKey.grid(row=0, column=0, sticky="ns",padx=5, pady=5)
fr_checkBox.grid(row=1, column=0, sticky="ns",padx=5, pady=5)
fr_sliderPrice.grid(row=2, column=0, sticky="ns",padx=5, pady=5)
fr_actionPlot.grid(row=3, column=0, sticky="ns",padx=5, pady=5)

#--------------------- scroll bar in second frame -----------------

my_canvas = tk.Canvas(fr_table)
my_canvas.pack(side=LEFT,fill=BOTH, expand=1)

# add scrollbar
my_scrollbar_V = ttk.Scrollbar(fr_table, orient=tk.VERTICAL, command=my_canvas.yview)
my_scrollbar_H = ttk.Scrollbar(fr_table, orient=tk.
                               HORIZONTAL, command=my_canvas.xview)

my_scrollbar_V.pack(side=RIGHT, fill=tk.Y)
my_scrollbar_H.pack(side=BOTTOM, fill=tk.X)

# configure
my_canvas.configure(yscrollcommand=my_scrollbar_V.set)
my_canvas.configure(xscrollcommand=my_scrollbar_H.set)

my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

# second_frame
second_frame = tk.Frame(my_canvas)
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")



###################### Left frame ############################
keyWord_label = tk.Label(fr_searchKey, text="Search by key word:")           # create label
e = tk.Entry(fr_searchKey,width =10, borderwidth = 2)                          # text box
btn_Search = tk.Button(fr_searchKey, text="Search",command=get_key)             # search button

#----------- check box ------------------
suburb_label = tk.Label(fr_checkBox, text="Choice Suburb below:")             # create label
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()
var6 = tk.IntVar()
var7 = tk.IntVar()
var8 = tk.IntVar()
btn_Checkbutton_1 = tk.Checkbutton(fr_checkBox, text="Sydney", variable=var1, onvalue=1, offvalue=0,command=get_selection)    # Radio Buttons
btn_Checkbutton_2 = tk.Checkbutton(fr_checkBox, text="Manly" , variable=var2, onvalue=1, offvalue=0,command=get_selection)     # Radio Buttons
btn_Checkbutton_3 = tk.Checkbutton(fr_checkBox, text="Leichhardt", variable=var3, onvalue=1, offvalue=0,command=get_selection)    # Radio Buttons
btn_Checkbutton_4 = tk.Checkbutton(fr_checkBox, text="Woollahra", variable=var4, onvalue=1, offvalue=0,command=get_selection)    # Radio Buttons
btn_Checkbutton_5 = tk.Checkbutton(fr_checkBox, text="North Sydney", variable=var5, onvalue=1, offvalue=0,command=get_selection)    # Radio Buttons
btn_Checkbutton_6 = tk.Checkbutton(fr_checkBox, text="Waverley", variable=var6, onvalue=1, offvalue=0,command=get_selection)    # Radio Buttons
btn_Checkbutton_7 = tk.Checkbutton(fr_checkBox, text="Mosman", variable=var7, onvalue=1, offvalue=0,command=get_selection)    # Radio Buttons
btn_Checkbutton_8 = tk.Checkbutton(fr_checkBox, text="Pittwater", variable=var8, onvalue=1, offvalue=0,command=get_selection)    # Radio Buttons

checkBox_label = tk.Label(fr_checkBox, bg='white', width=20, text='empty')

#----------- price slider ------------------
min_price_label = tk.Label(fr_sliderPrice, text="Min price:")           # create label
min_price_slider = tk.Scale(fr_sliderPrice, from_=0, to=500,orient=tk.HORIZONTAL, command=min_price)
max_price_label = tk.Label(fr_sliderPrice, text="Max price:")           # create label
max_price_slider = tk.Scale(fr_sliderPrice, from_=0, to=500,orient=tk.HORIZONTAL, command=max_price)

#----------- action plot ------------------
btn_price = tk.Button(fr_actionPlot, height = 2, width = 20, text="Show Price Figure",command=price_graph,padx=5, pady=5)             # search button
btn_map = tk.Button(fr_actionPlot,height = 2, width = 20, text="Show Map", command=map_graph,padx=5, pady=5)

########### display from here:##############

keyWord_label.grid(row = 0, column = 0)                                  # label
e.grid(row = 1, column = 0, columnspan=3)                                # text box
btn_Search.grid(row=2, column=0, sticky="ew")                            # search button

# check box
suburb_label.grid(row = 0, column = 0)                                   # label
btn_Checkbutton_1.grid(row=1, column=0)                                        # check Buttons
btn_Checkbutton_2.grid(row=2, column=0)                                        # check Buttons
btn_Checkbutton_3.grid(row=3, column=0)                                        # check Buttons
btn_Checkbutton_4.grid(row=4, column=0)                                        # check Buttons
btn_Checkbutton_5.grid(row=5, column=0)                                        # check Buttons
btn_Checkbutton_6.grid(row=6, column=0)                                        # check Buttons
btn_Checkbutton_7.grid(row=7, column=0)                                       # check Buttons
btn_Checkbutton_8.grid(row=8, column=0)                                       # check Buttons
checkBox_label.grid(row=9, column=0)

#----------- price slider ------------------

min_price_label.grid(row=0, column=0)
min_price_slider.grid(row=2, column=0)
max_price_label.grid(row=3, column=0)
max_price_slider.grid(row=4, column=0)


#----------- action plot ----------------------
btn_price.grid(row=0, column=0,padx=5, pady=5)
btn_map.grid(row=1, column=0,padx=5, pady=5)



###################### loop #############################

window.mainloop()