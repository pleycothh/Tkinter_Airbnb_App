from tkinter import *

root = Tk() # import
root.title( "Simple Calculater")

e = Entry(root,width =50, borderwidth = 2)
e.grid(row = 0, column = 0, columnspan=3, padx=10, pady=10)

#e.insert(0,"Enter your name") # put defult text inside the text box

def myClick():
    # create a Label Widget
    hello = "Hello " + e.get() # get entry value as label
    myLabel1 = Label(root, text=hello)

    # pack label to root window
    myLabel1.grid(row=2)


def button_click(number):
    current = e.get()
    e.delete(0, END) # deleted previous number

    e.insert(0, str(current) + str(number)) # add new number

def button_equal():
    e.delete(0,END)

def button_add():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0,END)

def button_equal():
    second_number = e.get() 
    e.delete(0,END)
    e.insert(0, f_num + int(second_number))

button_1 = Button(root, text="1", padx=50,pady=20,command= lambda:button_click(1)) # lambda: to pass the number
button_2 = Button(root, text="2", padx=50,pady=20,command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=50,pady=20,command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=50,pady=20,command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=50,pady=20,command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=50,pady=20,command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=50,pady=20,command=lambda: button_click)
button_8 = Button(root, text="8", padx=50,pady=20,command=lambda: button_click)
button_9 = Button(root, text="9", padx=50,pady=20,command=lambda: button_click)
button_0 = Button(root, text="0", padx=50,pady=20,command=lambda: button_click)
button_add = Button(root, text="+", padx=50,pady=20,command=button_add)
button_equal = Button(root, text="=", padx=50,pady=20,command=button_equal)



#myButton = Button(root, text="Enter Your Name", pady = 10, command=myClick,fg="blue", bg="red")

#myButton.pack()
#myButton.grid(row=1,column=0)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=0)
button_equal.grid(row=4,column=1)
button_add.grid(row=4,column=2)





# event loop
root.mainloop()
