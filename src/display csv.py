import pandas as pd
import csv
from tkinter import *
from PIL import ImageTk, Image



root = Tk()
root.title('learn')
########################### data ###########################
#df = pd.read_csv('src/listings_summary_dec18.csv')
#data = df.values
#head = df.to_string()

with open('src/listings_summary_dec18.csv', newline="") as file:
    reader = csv.reader(file)


    # r and c tell us where to grid the labels
    dRow = 0
    r = 0
    for col in reader:
        c = 0
        for row in col:
            # i've added some styling
            label = Label(root, width=10, height=2, text=row, relief=RIDGE)
            label.grid(row=r, column=c)
            c += 1
        r += 1
        dRow += 1
        if dRow == 10:
            break

root.mainloop()






########################### label ####################
#myLabel1 = Label(root, text= title)
#myLabel2 = Label(root, text= head)

# pack label to root window
#myLabel1.pack()
#myLabel2.pack()

#root.mainloop()
