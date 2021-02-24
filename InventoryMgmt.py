from tkinter import *

root = Tk()
root.title('Inventory Management - by MetSystems Inc.')
root.iconbitmap('C:/Users/Jason/Documents/GMU/2021-01-Spring/IT-493_Capstone/ProjectFiles/favicon.ico')
root.geometry("800x950")
root.config(bg="#BDBDBD")


topFrame = Frame(root)
topFrame.config(bg="#000000")
topFrame.pack(pady=50)

bottomFrame = Frame(root)
bottomFrame.config(bg="#BDBDBD")
bottomFrame.pack()


header = Label(topFrame, text="Inventory Management", height=2, width=100, fg="#003B6D", bg="#BDBDBD", font="Verdana 36 bold")
header.pack()

def openAdd():
    top = Toplevel()
    top.title('Add New Item')
    top.iconbitmap('C:/Users/Jason/Documents/GMU/2021-01-Spring/IT-493_Capstone/ProjectFiles/favicon.ico')
    #test label
    test_label = Label(top, text="Add New Item", fg="#003B6D", bg="#BDBDBD", font="Verdana 36 bold").pack()

def openView():
    top = Toplevel()
    top.title('View All')
    top.iconbitmap('C:/Users/Jason/Documents/GMU/2021-01-Spring/IT-493_Capstone/ProjectFiles/favicon.ico')
    #test label
    test_label = Label(top, text="View All", fg="#003B6D", bg="#BDBDBD", font="Verdana 36 bold").pack()


newItemBTN = Button(bottomFrame, text="Add New Item", padx=200, pady=20, font="Verdana 16", command=openAdd)
newItemBTN.pack(pady=100)

viewAllBTN = Button(bottomFrame, text="View All", padx=235, pady=20, font="Verdana 16", command=openView)
viewAllBTN.pack(pady=100)




#run the main loop -- this is the program running
root.mainloop()
