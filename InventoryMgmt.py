from tkinter import *
from tkinter import ttk
import mysql.connector

root = Tk()
root.title('Inventory Management - by MetSystems Inc.')
#root.iconbitmap('C:/Users/Jason/Documents/GMU/2021-01-Spring/IT-493_Capstone/ProjectFiles/favicon.ico')
root.geometry("800x950")
root.config(bg="#BDBDBD")

#====Database====#
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="thisisnotapassword",
    database="inventory_database"
)

print(mydb)

#====Main window frames====#
topFrame = Frame(root)
topFrame.config(bg="#BDBDBD")
topFrame.pack(pady=50)

bottomFrame = Frame(root)
bottomFrame.config(bg="#BDBDBD")
bottomFrame.pack()


header = Label(topFrame, text="Inventory Management", height=2, width=100, fg="#003B6D", bg="#BDBDBD", font="Verdana 36 bold")
header.pack()

class Products:
    def viewProd():
        top = Toplevel()
        top.title('Inventory Management - by MetSystems Inc.')
        #top.iconbitmap('C:/Users/Jason/Documents/GMU/2021-01-Spring/IT-493_Capstone/ProjectFiles/favicon.ico')
        
        #====window frames=====#
        topFrame = Frame(top)
        topFrame.config(bg="#BDBDBD")
        topFrame.pack(pady=50)

        midFrame = Frame(top)
        midFrame.config(bg="#BDBDBD")
        midFrame.pack(pady=10)

        bottomFrame = Frame(top)
        bottomFrame.config(bg="#BDBDBD")
        bottomFrame.pack(pady=20)

        #=====header label=====#
        add_label = Label(topFrame, text="Products", fg="#003B6D", bg="#BDBDBD", font="Verdana 36 bold").pack()
        top.geometry("800x950")
        top.config(bg="#BDBDBD")

        #??? - INSERT 'SORT BY' MODULE HERE - ???#
        #def selectEntries():
        #    mycursor = mydb.cursor()
        #    mycursor.execute("SELECT product_id, product_name, product_price, product_quantity_available, product_quantity_onhand FROM product")
        #    myresult = mycursor.fetchall()
        #    count = 0
        #    for i in myresult:
        #        prod_tree.insert('', 'end', iid=count, text="", values=(row[1], row[2], row[3], row[4], row[5]))
         #       count += 1

        #====Treeview====#
        tree_scroll = Scrollbar(midFrame, orient=VERTICAL)
        tree_scroll.pack(side=RIGHT, fill=Y)

        prod_tree = ttk.Treeview(midFrame, yscrollcommand=tree_scroll.set, height=30)
        prod_tree['columns'] = ("ID", "Name", "Price", "Qty Available", "Qty On Hand")
        
        prod_tree.column("#0", width=0, stretch=NO)
        prod_tree.column("ID", width=50)
        prod_tree.column("Name", width=300, anchor=CENTER)
        prod_tree.column("Price", width=100, anchor=E)
        prod_tree.column("Qty Available", width=100)
        prod_tree.column("Qty On Hand", width=100)

        prod_tree.heading("#0", text="")
        prod_tree.heading("ID", text="ID")
        prod_tree.heading("Name", text="Name")
        prod_tree.heading("Price", text="Price")
        prod_tree.heading("Qty Available", text="Qty Available")
        prod_tree.heading("Qty On Hand", text="Qty On Hand")

        prod_tree.pack()
        tree_scroll.config(command=prod_tree.yview)



        #=====Buttons=====#
        addProductBTN = Button(bottomFrame, text="Add New Product", padx=20, pady=10, font="Verdana 14", command=Products.addProduct)
        addProductBTN.grid(column=0, row=0, padx=20)

        viewProductBTN = Button(bottomFrame, text="View Info", padx=20, pady=10, font="Verdana 14", command=Products.viewInfo)
        viewProductBTN.grid(column=1, row=0, padx=20)

    def viewInfo():
        top = Toplevel()
        top.title('Add New Item')
        #top.iconbitmap('C:/Users/Jason/Documents/GMU/2021-01-Spring/IT-493_Capstone/ProjectFiles/favicon.ico')
        
        #====window frames=====#
        topFrame = Frame(top)
        topFrame.config(bg="#BDBDBD")
        topFrame.pack(pady=50)

        bottomFrame = Frame(top, highlightbackground="white", highlightthickness=4)
        bottomFrame.config(bg="#BDBDBD")
        bottomFrame.pack()

        btnFrame = Frame(top, highlightbackground="black", highlightthickness=4)
        btnFrame.config(bg="#BDBDBD")
        btnFrame.pack(pady=0)

        #=====header label=====#
        add_label = Label(topFrame, text="View Record Info", fg="#003B6D", bg="#BDBDBD", font="Verdana 36 bold").pack()
        top.geometry("800x950")
        top.config(bg="#BDBDBD")


    def addProduct():
        top = Toplevel()
        top.title('Add New Item')
        #top.iconbitmap('C:/Users/Jason/Documents/GMU/2021-01-Spring/IT-493_Capstone/ProjectFiles/favicon.ico')
        
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
        serial_num = Entry(bottomFrame2, font=('arial', 16), width=30, justify='center').grid(row=0, column=1)
        item_name = Entry(bottomFrame2, font=('arial', 16), width=30, justify='center').grid(row=1, column=1)
        description = Entry(bottomFrame2, font=('arial', 16), width=30, justify='center').grid(row=2, column=1)
        price_in = Entry(bottomFrame2, font=('arial', 16), width=30, justify='center').grid(row=3, column=1)
        price_out = Entry(bottomFrame2, font=('arial', 16), width=30, justify='center').grid(row=4, column=1)
        predecessors = Entry(bottomFrame2, font=('arial', 16), width=30, justify='center').grid(row=5, column=1)
        install_time = Entry(bottomFrame2, font=('arial', 16), width=30, justify='center').grid(row=6, column=1)
        delivery_time = Entry(bottomFrame2, font=('arial', 16), width=30, justify='center').grid(row=7, column=1)


        #====Buttons====#
        save_btn = Button(btnFrame2, text="Save", height=2, width=20).grid(row=0, column=0, padx=10, pady=15)
        clear_btn = Button(btnFrame2, text="Clear", height=2, width=20).grid(row=0, column=1, padx=10, pady=15)


class Parts:
    def viewPart():
        top = Toplevel()
        top.title('Inventory Management - by MetSystems Inc.')
        #top.iconbitmap('C:/Users/Jason/Documents/GMU/2021-01-Spring/IT-493_Capstone/ProjectFiles/favicon.ico')
        
        #====Add New Item window frames=====#
        topFrame2 = Frame(top)
        topFrame2.config(bg="#BDBDBD")
        topFrame2.pack(pady=50)

        #=====header label=====#
        add_label = Label(topFrame2, text="Parts", fg="#003B6D", bg="#BDBDBD", font="Verdana 36 bold").pack()
        top.geometry("800x950")
        top.config(bg="#BDBDBD")

    def addPart():
        top = Toplevel()
        top.title('Add New Item')
        #top.iconbitmap('C:/Users/Jason/Documents/GMU/2021-01-Spring/IT-493_Capstone/ProjectFiles/favicon.ico')
        
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


class Vendors:
    def viewVendor():
        top = Toplevel()
        top.title('Inventory Management - by MetSystems Inc.')
        #top.iconbitmap('C:/Users/Jason/Documents/GMU/2021-01-Spring/IT-493_Capstone/ProjectFiles/favicon.ico')
        
        #====Add New Item window frames=====#
        topFrame2 = Frame(top)
        topFrame2.config(bg="#BDBDBD")
        topFrame2.pack(pady=50)

        #=====header label=====#
        add_label = Label(topFrame2, text="Vendors", fg="#003B6D", bg="#BDBDBD", font="Verdana 36 bold").pack()
        top.geometry("800x950")
        top.config(bg="#BDBDBD")

    def addVendor():
        top = Toplevel()
        top.title('Add New Item')
        #top.iconbitmap('C:/Users/Jason/Documents/GMU/2021-01-Spring/IT-493_Capstone/ProjectFiles/favicon.ico')
        
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


class Quantity:
    def updateQty():
        top = Toplevel()
        top.title('Inventory Management - by MetSystems Inc.')
        #top.iconbitmap('C:/Users/Jason/Documents/GMU/2021-01-Spring/IT-493_Capstone/ProjectFiles/favicon.ico')
        
        #====Add New Item window frames=====#
        topFrame2 = Frame(top)
        topFrame2.config(bg="#BDBDBD")
        topFrame2.pack(pady=50)

        #=====header label=====#
        add_label = Label(topFrame2, text="Update Quantity", fg="#003B6D", bg="#BDBDBD", font="Verdana 36 bold").pack()
        top.geometry("800x950")
        top.config(bg="#BDBDBD")




    





def openView():
    top = Toplevel()
    top.title('View All')
    #top.iconbitmap('C:/Users/Jason/Documents/GMU/2021-01-Spring/IT-493_Capstone/ProjectFiles/favicon.ico')
    #test label
    test_label = Label(top, text="View All", fg="#003B6D", bg="#BDBDBD", font="Verdana 36 bold").pack()


viewProductsBTN = Button(bottomFrame, text="View Products", padx=100, pady=20, font="Verdana 16", command=Products.viewProd)
viewProductsBTN.pack(pady=20)

viewPartsBTN = Button(bottomFrame, text="View Parts", padx=119, pady=20, font="Verdana 16", command=Parts.viewPart)
viewPartsBTN.pack(pady=20)

viewVendorsBTN = Button(bottomFrame, text="View Vendors", padx=103, pady=20, font="Verdana 16", command=Vendors.viewVendor)
viewVendorsBTN.pack(pady=20)

updateQuantityBTN = Button(bottomFrame, text="Update Qty", padx=114, pady=20, font="Verdana 16", command=Quantity.updateQty)
updateQuantityBTN.pack(pady=20)




#run the main loop -- this is the program running
root.mainloop()
