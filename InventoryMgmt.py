from tkinter import *

root = Tk()
root.title('Inventory Management - by MetSystems Inc.')
root.iconbitmap('C:/Users/Jason/Documents/GMU/2021-01-Spring/IT-493_Capstone/ProjectFiles/favicon.ico')


topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)


header = Label(topFrame, text="Inventory Management", fg="#003B6D", bg="#BDBDBD", font="Verdana 36 bold")
header.pack()

def openAdd():
    top = Toplevel()
    top.title('Add New Item')
    top.iconbitmap('C:/Users/Jason/Documents/GMU/2021-01-Spring/IT-493_Capstone/ProjectFiles/favicon.ico')
    #test label
    test_label = Label(top, text="Add New Item", fg="#003B6D", bg="#BDBDBD", font="Verdana 36 bold").pack()


newItemBTN = Button(bottomFrame, text="Add New Item", padx=300, pady=10, command=openAdd).pack()






#run the main loop -- this is the program running
root.mainloop()
