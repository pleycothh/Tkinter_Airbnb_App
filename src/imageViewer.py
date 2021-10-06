from  tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title('learn')
############Frame##############

frame = LabelFrame(root, text="This is my frame", padx=5, pady=5) # pad inside of frame
frame.pack(padx=10,pady=10) # pad outside the frame

##########################
# instate of use root, I can use frame
button_quit = Button(frame, text="E", command=root.quit)
button_quit.pack()



root.mainloop()
