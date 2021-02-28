from tkinter import *

root = Tk()
root.title('Inventory Management - by MetSystems Inc.')
root.iconbitmap('C:/Users/Jason/Documents/GMU/2021-01-Spring/IT-493_Capstone/ProjectFiles/favicon.ico')
root.geometry("800x950")
root.config(bg="#BDBDBD")


#====Main window frames====
topFrame = Frame(root)
topFrame.config(bg="#BDBDBD")
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
    
    #====Add New Item window frames=====#
    topFrame2 = Frame(top)
    topFrame2.config(bg="#BDBDBD")
    topFrame2.pack(pady=50)

    bottomFrame2 = Frame(top, highlightbackground="white", highlightthickness=4)
    bottomFrame2.config(bg="#BDBDBD")
    bottomFrame2.pack()

    btnFrame2 = Frame(top, highlightbackground="black", highlightthickness=4)
    btnFrame2.config(bg="#BDBDBD")
    btnFrame2.pack(pady=0)

    #=====header label=====#
    add_label = Label(topFrame2, text="Add New Item", fg="#003B6D", bg="#BDBDBD", font="Verdana 36 bold").pack()
    top.geometry("800x950")
    top.config(bg="#BDBDBD")


    #====Input Field Labels====#
    serial_num_Label = Label(bottomFrame2, text="Serial Number: ").grid(row=0)
    item_name_Label = Label(bottomFrame2, text="Item Name: ").grid(row=1)
    description_Label = Label(bottomFrame2, text="Description: ").grid(row=2)
    price_in_Label = Label(bottomFrame2, text="Price In: ").grid(row=3)
    price_out_Label = Label(bottomFrame2, text="Price Out: ").grid(row=4)
    predecessors_Label = Label(bottomFrame2, text="Predecessors: ").grid(row=5)
    install_time_Label = Label(bottomFrame2, text="Install Time: ").grid(row=6)
    delivery_time_Label = Label(bottomFrame2, text="Est. Delivery Time: ").grid(row=7)


    #====Input Field Entries====#
    serial_num = Entry(bottomFrame2).grid(row=0, column=1)
    item_name = Entry(bottomFrame2).grid(row=1, column=1)
    description = Entry(bottomFrame2).grid(row=2, column=1)
    price_in = Entry(bottomFrame2).grid(row=3, column=1)
    price_out = Entry(bottomFrame2).grid(row=4, column=1)
    predecessors = Entry(bottomFrame2).grid(row=5, column=1)
    install_time = Entry(bottomFrame2).grid(row=6, column=1)
    delivery_time = Entry(bottomFrame2).grid(row=7, column=1)


    #====Buttons====#
    save_btn = Button(btnFrame2, text="Save", height=2, width=20).grid(row=0, column=0, padx=10, pady=15)
    clear_btn = Button(btnFrame2, text="Clear", height=2, width=20).grid(row=0, column=1, padx=10, pady=15)


    





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
