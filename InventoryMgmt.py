from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

root = Tk()
root.title('Inventory Management - by MetSystems Inc.')
#root.iconbitmap('C:/Users/Jason/Documents/GMU/2021-01-Spring/IT-493_Capstone/ProjectFiles/favicon.ico')
root.geometry("800x950")
root.config(bg="#BDBDBD")

#====Connect to Database====#
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
        topFrame.config(bg="#BDBDBD", width=600)
        topFrame.pack(pady=20)

        midFrame = Frame(top)
        midFrame.config(bg="#BDBDBD")
        midFrame.pack(pady=10)

        bottomFrame = Frame(top)
        bottomFrame.config(bg="#BDBDBD")
        bottomFrame.pack(pady=20)

        #=====header label=====#
        add_label = Label(topFrame, text="          Products          ", fg="#003B6D", bg="#BDBDBD", font="Verdana 36 bold").grid(row=0, pady=20)
        top.geometry("800x950")
        top.config(bg="#BDBDBD")

        #====sort by dropdown====#
        dropDWN = StringVar(topFrame)
        dropDWN.set("Sort By:")

        dd = OptionMenu(topFrame, dropDWN, "ID", "Name", "Price", "QTY Avail.", "QTY On Hand")
        dd.config(width=15, anchor=W)
        dd.grid(row=1, column=0, sticky=E, padx=10)

        okBTN = Button(topFrame, text="GO")#, command=sortBy)
        okBTN.grid(row=1, column=1, sticky=E)

        

        #====SELECT from DB====#
        def selectEntries():
            mycursor = mydb.cursor()
            mycursor.execute("SELECT product_id, product_name, concat('$ ', format(product_price,2)), product_quantity_available, product_quantity_onhand FROM product")
            myresult = mycursor.fetchall()
            count = 0
            for row in myresult:
                prod_tree.insert('', 'end', iid=count, text="", values=(row[0], row[1], row[2], row[3], row[4]))
                count += 1
            mycursor.close()

        #def sortBy():
            #insert SQL script to SELECT and ORDER BY

        #====Treeview====#
        tree_scroll = Scrollbar(midFrame, orient=VERTICAL)
        tree_scroll.pack(side=RIGHT, fill=Y)

        prod_tree = ttk.Treeview(midFrame, yscrollcommand=tree_scroll.set, height=30)
        prod_tree['columns'] = ("ID", "Name", "Price", "Qty Available", "Qty On Hand")
        
        prod_tree.column("#0", width=0, stretch=NO)
        prod_tree.column("ID", width=50, anchor=E)
        prod_tree.column("Name", width=300, anchor=CENTER)
        prod_tree.column("Price", width=100, anchor=E)
        prod_tree.column("Qty Available", width=100, anchor=CENTER)
        prod_tree.column("Qty On Hand", width=100, anchor=CENTER)

        prod_tree.heading("#0", text="")
        prod_tree.heading("ID", text="ID")
        prod_tree.heading("Name", text="Name")
        prod_tree.heading("Price", text="Price")
        prod_tree.heading("Qty Available", text="Qty Available")
        prod_tree.heading("Qty On Hand", text="Qty On Hand")

        
        selectEntries()
        
        prod_tree.pack()
        tree_scroll.config(command=prod_tree.yview)

        def selectItem(a):
            curItem = prod_tree.focus()
            print (prod_tree.item(curItem))
            global y
            x = (prod_tree.item(curItem, 'values'))
            y = (x[0]) 

           

        #a = prod_tree.bind('<ButtonRelease-1>', selectItem)

        prod_tree.bind('<ButtonRelease-1>', selectItem)
        
        #print (a)

        #=====Buttons=====#
        addProductBTN = Button(bottomFrame, text="Add New Product", padx=20, pady=10, font="Verdana 14", command=Products.addProduct)
        addProductBTN.grid(column=0, row=0, padx=20)

        viewProductBTN = Button(bottomFrame, text="View/Edit", padx=20, pady=10, font="Verdana 14", command=Products.viewInfo)
        viewProductBTN.grid(column=1, row=0, padx=20)

        delProductBTN = Button(bottomFrame, text="Delete Product", padx=20, pady=10, font="Verdana 14")#, command=Products.viewInfo)
        delProductBTN.grid(column=2, row=0, padx=20)

      

    

    def viewInfo():
        print (y)


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

        #-----------------------------#
        #====Create Variables====#
        serial_num_var = IntVar()
        item_name_var = StringVar()
        price_listed_var = IntVar()
        price_cost_var = IntVar()
        unit_var = StringVar()
        install_time_var = IntVar()
        delivery_time_var = IntVar()

        
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM product WHERE product_id = {};".format(y))
        myresult = mycursor.fetchall()
           
        for row in myresult:
            serial_num_var.set(row[2]) 
            item_name_var.set(row[3]) 
            price_listed_var.set(row[6]) 
            price_cost_var.set(row[7]) 
            unit_var.set(row[8])
            install_time_var.set(row[10])
            delivery_time_var.set(row[11])
                
        mycursor.close()


         #====Input Field Labels====#
        serial_num_Label = Label(bottomFrame, text="Serial Number: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=0, sticky=W)
        item_name_Label = Label(bottomFrame, text="Item Name: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=1, sticky=W)
        Supplier_Label = Label(bottomFrame, text="Supplier: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=2, sticky=W)
        price_listed_Label = Label(bottomFrame, text="Listed Price: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=3, sticky=W)
        price_cost_Label = Label(bottomFrame, text="Price Cost: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=4, sticky=W)
        unit_Label = Label(bottomFrame, text="Unit: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=5, sticky=W)
        predecessors_Label = Label(bottomFrame, text="Predecessors: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=6, sticky='nw')
        #Row 7 reserved for Treeviews
        install_time_Label = Label(bottomFrame, text="Install Time: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=8, sticky=W)
        install_time_Label2 = Label(bottomFrame, text=" days       ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=8, column=1, sticky=E)
        delivery_time_Label = Label(bottomFrame, text="Est. Delivery Time: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=9, sticky=W)
        delivery_time_Label2 = Label(bottomFrame, text=" days       ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=9, column=1, sticky=E)

        

        #====Input Field Entries====#
        serial_num = Entry(bottomFrame, textvariable=serial_num_var, font=('arial', 16), width=30, justify='center')
        item_name = Entry(bottomFrame, textvariable=item_name_var, font=('arial', 16), width=30, justify='center')
        # dropdown
        dropdown_sup = StringVar(bottomFrame)
        dropdown_sup.set("Choose One")
        dd_sup = OptionMenu(bottomFrame, dropdown_sup, "1", "2", "3") #SQL list of suppliers)
        dd_sup.config(width=53, anchor=W)
        dd_sup.grid(row=2, column=1, pady=5)
        price_listed = Entry(bottomFrame, textvariable=price_listed_var, font=('arial', 16), width=30, justify='center')
        price_cost = Entry(bottomFrame, textvariable=price_cost_var, font=('arial', 16), width=30, justify='center')
        unit = Entry(bottomFrame,  textvariable=unit_var, font=('arial', 16), width=30, justify='center')
        # change to treeview -> predecessors = Entry(bottomFrame2, font=('arial', 16), width=30, justify='center').grid(row=7, column=1)
        tree_scroll = Scrollbar(bottomFrame, orient=VERTICAL)
        tree_scroll.grid(row=6, column=2, rowspan=2, sticky='ns', pady=5)

        pred_tree = ttk.Treeview(bottomFrame, yscrollcommand=tree_scroll.set, height=10)
        pred_tree['columns'] = ("ID", "Serial Number", "Name")
        
        pred_tree.column("#0", width=0, stretch=NO)
        pred_tree.column("ID", width=50, anchor=E)
        pred_tree.column("Serial Number", width=100, anchor=E)
        pred_tree.column("Name", width=210, anchor=CENTER)

        pred_tree.heading("#0", text="")
        pred_tree.heading("ID", text="ID")
        pred_tree.heading("Serial Number", text="Serial #")
        pred_tree.heading("Name", text="Name")
        pred_tree.grid(row=6, rowspan=2, column=1, pady=5)
        tree_scroll.config(command=pred_tree.yview)
        
        install_time = Entry(bottomFrame, textvariable=install_time_var, font=('arial', 16), width=23, justify='center')
        delivery_time = Entry(bottomFrame, textvariable=delivery_time_var, font=('arial', 16), width=23, justify='center')

        #====Grid Inserts====#
        serial_num.grid(row=0, column=1, pady=5)
        item_name.grid(row=1, column=1, pady=5)
        price_listed.grid(row=3, column=1, pady=5)
        price_cost.grid(row=4, column=1, pady=5)
        unit.grid(row=5, column=1, pady=5)
        install_time.grid(row=8, column=1, pady=5, sticky=W)
        delivery_time.grid(row=9, column=1, pady=5, sticky=W)

       
      


    def addProduct():
        top = Toplevel()
        top.title('Add New Item')
        #top.iconbitmap('C:/Users/Jason/Documents/GMU/2021-01-Spring/IT-493_Capstone/ProjectFiles/favicon.ico')
        
        #====Add New Item window frames=====#
        topFrame2 = Frame(top)
        topFrame2.config(bg="#BDBDBD")
        topFrame2.pack(pady=50)

        bottomFrame2 = Frame(top)
        bottomFrame2.config(bg="#BDBDBD")
        bottomFrame2.pack()

        btnFrame2 = Frame(top)
        btnFrame2.config(bg="#BDBDBD")
        btnFrame2.pack(pady=25)

        #=====header label=====#
        add_label = Label(topFrame2, text="Add New Item", fg="#003B6D", bg="#BDBDBD", font="Verdana 36 bold").pack()
        top.geometry("800x950")
        top.config(bg="#BDBDBD")


         #====Input Field Labels====#
        serial_num_Label = Label(bottomFrame2, text="Serial Number: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=0, sticky=W)
        item_name_Label = Label(bottomFrame2, text="Item Name: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=1, sticky=W)
        Supplier_Label = Label(bottomFrame2, text="Supplier: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=2, sticky=W)
        price_listed_Label = Label(bottomFrame2, text="Listed Price: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=3, sticky=W)
        price_cost_Label = Label(bottomFrame2, text="Price Cost: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=4, sticky=W)
        unit_Label = Label(bottomFrame2, text="Unit: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=5, sticky=W)
        predecessors_Label = Label(bottomFrame2, text="Predecessors: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=6, sticky='nw')
        #Row 7 reserved for Treeviews
        install_time_Label = Label(bottomFrame2, text="Install Time: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=8, sticky=W)
        install_time_Label2 = Label(bottomFrame2, text=" days       ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=8, column=1, sticky=E)
        delivery_time_Label = Label(bottomFrame2, text="Est. Delivery Time: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=9, sticky=W)
        delivery_time_Label2 = Label(bottomFrame2, text=" days       ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=9, column=1, sticky=E)

        #====Create Variables====#
        serial_num_var = IntVar()
        item_name_var = StringVar()
        price_listed_var = IntVar()
        price_cost_var = IntVar()
        unit_var = StringVar()
        install_time_var = IntVar()
        delivery_time_var = IntVar()

        #====Input Field Entries====#
        serial_num = Entry(bottomFrame2, textvariable=serial_num_var, font=('arial', 16), width=30, justify='center')
        item_name = Entry(bottomFrame2, textvariable=item_name_var, font=('arial', 16), width=30, justify='center')
        # dropdown
        dropdown_sup = StringVar(bottomFrame2)
        dropdown_sup.set("Choose One")
        dd_sup = OptionMenu(bottomFrame2, dropdown_sup, "1", "2", "3") #SQL list of suppliers)
        dd_sup.config(width=53, anchor=W)
        dd_sup.grid(row=2, column=1, pady=5)
        price_listed = Entry(bottomFrame2, textvariable=price_listed_var, font=('arial', 16), width=30, justify='center')
        price_cost = Entry(bottomFrame2, textvariable=price_cost_var, font=('arial', 16), width=30, justify='center')
        unit = Entry(bottomFrame2,  textvariable=unit_var, font=('arial', 16), width=30, justify='center')
        # change to treeview -> predecessors = Entry(bottomFrame2, font=('arial', 16), width=30, justify='center').grid(row=7, column=1)
        tree_scroll = Scrollbar(bottomFrame2, orient=VERTICAL)
        tree_scroll.grid(row=6, column=2, rowspan=2, sticky='ns', pady=5)

        pred_tree = ttk.Treeview(bottomFrame2, yscrollcommand=tree_scroll.set, height=10)
        pred_tree['columns'] = ("ID", "Serial Number", "Name")
        
        pred_tree.column("#0", width=0, stretch=NO)
        pred_tree.column("ID", width=50, anchor=E)
        pred_tree.column("Serial Number", width=100, anchor=E)
        pred_tree.column("Name", width=210, anchor=CENTER)

        pred_tree.heading("#0", text="")
        pred_tree.heading("ID", text="ID")
        pred_tree.heading("Serial Number", text="Serial #")
        pred_tree.heading("Name", text="Name")
        pred_tree.grid(row=6, rowspan=2, column=1, pady=5)
        tree_scroll.config(command=pred_tree.yview)
        
        install_time = Entry(bottomFrame2, textvariable=install_time_var, font=('arial', 16), width=23, justify='center')
        delivery_time = Entry(bottomFrame2, textvariable=delivery_time_var, font=('arial', 16), width=23, justify='center')

        #====Grid Inserts====#
        serial_num.grid(row=0, column=1, pady=5)
        item_name.grid(row=1, column=1, pady=5)
        price_listed.grid(row=3, column=1, pady=5)
        price_cost.grid(row=4, column=1, pady=5)
        unit.grid(row=5, column=1, pady=5)
        install_time.grid(row=8, column=1, pady=5, sticky=W)
        delivery_time.grid(row=9, column=1, pady=5, sticky=W)

        def write2db():
            ###UPDATE THIS SCRIPT###
            insertNewProduct = """INSERT INTO (product_supplier_id, product_number, product_name, product_quantity_available, \
            product_quantity_onhand, product_price, product_cost, product_unit, product_part_predecessor) \
            VALUES ({},{},{},{},{},{},{},{},{})"""

            product_records = (dropdown_sup, serial_num.get(), item_name.get(), 0, 0, price_listed.get(), price_cost.get(), unit.get(), install_time.get(), delivery_time.get(), int(pred_tree.item(pred_tree.selection(),"ID")))

            with mydb.cursor() as cursor:
                cursor.execute(insertNewProduct, product_records)
                mydb.commit()
                cursor.close()
            
        def clearEntries():
            serial_num_var.set('')
            item_name_var.set('')
            dropdown_sup.set("Choose One")
            price_listed_var.set('')
            price_cost_var.set('')
            unit_var.set('')
            install_time_var.set('')
            delivery_time_var.set('')
            pred_tree.selection_clear() #this might not work

        #====Buttons====#
        save_btn = Button(btnFrame2, text="Save", height=2, width=20, command=write2db).grid(row=0, column=0, padx=10, pady=15)
        clear_btn = Button(btnFrame2, text="Clear", height=2, width=20, command=clearEntries).grid(row=0, column=1, padx=10, pady=15)


class Parts:
    def viewPart():
        top = Toplevel()
        top.title('Inventory Management - by MetSystems Inc.')
        #top.iconbitmap('C:/Users/Jason/Documents/GMU/2021-01-Spring/IT-493_Capstone/ProjectFiles/favicon.ico')
        
        #====window frames=====#
        topFrame = Frame(top)
        topFrame.config(bg="#BDBDBD", width=600)
        topFrame.pack(pady=20)

        midFrame = Frame(top)
        midFrame.config(bg="#BDBDBD")
        midFrame.pack(pady=10)

        bottomFrame = Frame(top)
        bottomFrame.config(bg="#BDBDBD")
        bottomFrame.pack(pady=20)

        #=====header label=====#
        add_label = Label(topFrame, text="          Parts          ", fg="#003B6D", bg="#BDBDBD", font="Verdana 36 bold").grid(row=0, pady=20)
        top.geometry("800x950")
        top.config(bg="#BDBDBD")

        #====sort by dropdown====#
        dropDWN = StringVar(topFrame)
        dropDWN.set("Sort By:")

        dd = OptionMenu(topFrame, dropDWN, "ID", "Name", "Price", "QTY Avail.", "QTY On Hand")
        dd.config(width=15, anchor=W)
        dd.grid(row=1, column=0, sticky=E, padx=10)

        okBTN = Button(topFrame, text="GO")#, command=sortBy)
        okBTN.grid(row=1, column=1, sticky=E)

        

        #====SELECT from DB====#
        def selectEntries():
            mycursor = mydb.cursor()
            mycursor.execute("SELECT part_id, part_name, concat('$ ', format(part_price,2)), part_quantity_available, part_quantity_onhand FROM part")
            myresult = mycursor.fetchall()
            count = 0
            for row in myresult:
                part_tree.insert('', 'end', iid=count, text="", values=(row[0], row[1], row[2], row[3], row[4]))
                count += 1
            mycursor.close()

        #def sortBy():
            #insert SQL script to SELECT and ORDER BY

        #====Treeview====#
        tree_scroll = Scrollbar(midFrame, orient=VERTICAL)
        tree_scroll.pack(side=RIGHT, fill=Y)

        part_tree = ttk.Treeview(midFrame, yscrollcommand=tree_scroll.set, height=30)
        part_tree['columns'] = ("ID", "Name", "Price", "Qty Available", "Qty On Hand")
        
        part_tree.column("#0", width=0, stretch=NO)
        part_tree.column("ID", width=50, anchor=E)
        part_tree.column("Name", width=300, anchor=CENTER)
        part_tree.column("Price", width=100, anchor=E)
        part_tree.column("Qty Available", width=100, anchor=CENTER)
        part_tree.column("Qty On Hand", width=100, anchor=CENTER)

        part_tree.heading("#0", text="")
        part_tree.heading("ID", text="ID")
        part_tree.heading("Name", text="Name")
        part_tree.heading("Price", text="Price")
        part_tree.heading("Qty Available", text="Qty Available")
        part_tree.heading("Qty On Hand", text="Qty On Hand")

        
        selectEntries()
        
        part_tree.pack()
        tree_scroll.config(command=part_tree.yview)

        def selectItem(a):
            curItem = part_tree.focus()
            print (part_tree.item(curItem))
            global y
            x = (part_tree.item(curItem, 'values'))
            y = (x[0]) 

           

        #a = part_tree.bind('<ButtonRelease-1>', selectItem)

        part_tree.bind('<ButtonRelease-1>', selectItem)
        
        #print (a)

        #=====Buttons=====#
        addPartBTN = Button(bottomFrame, text="Add New Part", padx=20, pady=10, font="Verdana 14", command=Parts.addPart)
        addPartBTN.grid(column=0, row=0, padx=20)

        viewPartBTN = Button(bottomFrame, text="View/Edit", padx=20, pady=10, font="Verdana 14", command=Parts.viewInfo)
        viewPartBTN.grid(column=1, row=0, padx=20)

        delPartBTN = Button(bottomFrame, text="Delete Part", padx=20, pady=10, font="Verdana 14")#, command=Parts.viewInfo)
        delPartBTN.grid(column=2, row=0, padx=20)

      

    

    def viewInfo():
        print (y)


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

        #-----------------------------#
        #====Create Variables====#
        serial_num_var = IntVar()
        item_name_var = StringVar()
        price_listed_var = IntVar()
        price_cost_var = IntVar()
        unit_var = StringVar()
        install_time_var = IntVar()
        delivery_time_var = IntVar()

        
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM part WHERE part_id = {};".format(y))
        myresult = mycursor.fetchall()
           
        for row in myresult:
            serial_num_var.set(row[2]) 
            item_name_var.set(row[3]) 
            price_listed_var.set(row[6]) 
            price_cost_var.set(row[7]) 
            unit_var.set(row[8])
            install_time_var.set(row[9])
            delivery_time_var.set(row[10])
                
        mycursor.close()


         #====Input Field Labels====#
        serial_num_Label = Label(bottomFrame, text="Serial Number: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=0, sticky=W)
        item_name_Label = Label(bottomFrame, text="Item Name: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=1, sticky=W)
        Supplier_Label = Label(bottomFrame, text="Supplier: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=2, sticky=W)
        price_listed_Label = Label(bottomFrame, text="Listed Price: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=3, sticky=W)
        price_cost_Label = Label(bottomFrame, text="Price Cost: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=4, sticky=W)
        unit_Label = Label(bottomFrame, text="Unit: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=5, sticky=W)
        #predecessors_Label = Label(bottomFrame, text="Predecessors: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=6, sticky='nw')
        #Row 7 reserved for Treeviews
        install_time_Label = Label(bottomFrame, text="Install Time: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=8, sticky=W)
        install_time_Label2 = Label(bottomFrame, text=" days       ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=8, column=1, sticky=E)
        delivery_time_Label = Label(bottomFrame, text="Est. Delivery Time: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=9, sticky=W)
        delivery_time_Label2 = Label(bottomFrame, text=" days       ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=9, column=1, sticky=E)

        

        #====Input Field Entries====#
        serial_num = Entry(bottomFrame, textvariable=serial_num_var, font=('arial', 16), width=30, justify='center')
        item_name = Entry(bottomFrame, textvariable=item_name_var, font=('arial', 16), width=30, justify='center')
        # dropdown
        dropdown_sup = StringVar(bottomFrame)
        dropdown_sup.set("Choose One")
        dd_sup = OptionMenu(bottomFrame, dropdown_sup, "1", "2", "3") #SQL list of suppliers)
        dd_sup.config(width=53, anchor=W)
        dd_sup.grid(row=2, column=1, pady=5)
        price_listed = Entry(bottomFrame, textvariable=price_listed_var, font=('arial', 16), width=30, justify='center')
        price_cost = Entry(bottomFrame, textvariable=price_cost_var, font=('arial', 16), width=30, justify='center')
        unit = Entry(bottomFrame,  textvariable=unit_var, font=('arial', 16), width=30, justify='center')
        # change to treeview -> predecessors = Entry(bottomFrame2, font=('arial', 16), width=30, justify='center').grid(row=7, column=1)
       
        
        install_time = Entry(bottomFrame, textvariable=install_time_var, font=('arial', 16), width=23, justify='center')
        delivery_time = Entry(bottomFrame, textvariable=delivery_time_var, font=('arial', 16), width=23, justify='center')

        #====Grid Inserts====#
        serial_num.grid(row=0, column=1, pady=5)
        item_name.grid(row=1, column=1, pady=5)
        price_listed.grid(row=3, column=1, pady=5)
        price_cost.grid(row=4, column=1, pady=5)
        unit.grid(row=5, column=1, pady=5)
        install_time.grid(row=8, column=1, pady=5, sticky=W)
        delivery_time.grid(row=9, column=1, pady=5, sticky=W)

       

      


    def addPart():
        top = Toplevel()
        top.title('Add New Item')
        #top.iconbitmap('C:/Users/Jason/Documents/GMU/2021-01-Spring/IT-493_Capstone/ProjectFiles/favicon.ico')
        
        #====Add New Item window frames=====#
        topFrame2 = Frame(top)
        topFrame2.config(bg="#BDBDBD")
        topFrame2.pack(pady=50)

        bottomFrame2 = Frame(top)
        bottomFrame2.config(bg="#BDBDBD")
        bottomFrame2.pack()

        btnFrame2 = Frame(top)
        btnFrame2.config(bg="#BDBDBD")
        btnFrame2.pack(pady=25)

        #=====header label=====#
        add_label = Label(topFrame2, text="Add New Item", fg="#003B6D", bg="#BDBDBD", font="Verdana 36 bold").pack()
        top.geometry("800x950")
        top.config(bg="#BDBDBD")


         #====Input Field Labels====#
        serial_num_Label = Label(bottomFrame2, text="Serial Number: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=0, sticky=W)
        item_name_Label = Label(bottomFrame2, text="Item Name: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=1, sticky=W)
        Supplier_Label = Label(bottomFrame2, text="Supplier: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=2, sticky=W)
        price_listed_Label = Label(bottomFrame2, text="Listed Price: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=3, sticky=W)
        price_cost_Label = Label(bottomFrame2, text="Price Cost: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=4, sticky=W)
        unit_Label = Label(bottomFrame2, text="Unit: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=5, sticky=W)
        #predecessors_Label = Label(bottomFrame2, text="Predecessors: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=6, sticky='nw')
        #Row 7 reserved for Treeviews
        install_time_Label = Label(bottomFrame2, text="Install Time: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=8, sticky=W)
        install_time_Label2 = Label(bottomFrame2, text=" days       ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=8, column=1, sticky=E)
        delivery_time_Label = Label(bottomFrame2, text="Est. Delivery Time: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=9, sticky=W)
        delivery_time_Label2 = Label(bottomFrame2, text=" days       ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=9, column=1, sticky=E)

        #====Create Variables====#
        serial_num_var = IntVar()
        item_name_var = StringVar()
        price_listed_var = IntVar()
        price_cost_var = IntVar()
        unit_var = StringVar()
        install_time_var = IntVar()
        delivery_time_var = IntVar()

        #====Input Field Entries====#
        serial_num = Entry(bottomFrame2, textvariable=serial_num_var, font=('arial', 16), width=30, justify='center')
        item_name = Entry(bottomFrame2, textvariable=item_name_var, font=('arial', 16), width=30, justify='center')
        # dropdown
        dropdown_sup = StringVar(bottomFrame2)
        dropdown_sup.set("Choose One")
        dd_sup = OptionMenu(bottomFrame2, dropdown_sup, "1", "2", "3") #SQL list of suppliers)
        dd_sup.config(width=53, anchor=W)
        dd_sup.grid(row=2, column=1, pady=5)
        price_listed = Entry(bottomFrame2, textvariable=price_listed_var, font=('arial', 16), width=30, justify='center')
        price_cost = Entry(bottomFrame2, textvariable=price_cost_var, font=('arial', 16), width=30, justify='center')
        unit = Entry(bottomFrame2,  textvariable=unit_var, font=('arial', 16), width=30, justify='center')
        # change to treeview -> predecessors = Entry(bottomFrame2, font=('arial', 16), width=30, justify='center').grid(row=7, column=1)
        
        
        install_time = Entry(bottomFrame2, textvariable=install_time_var, font=('arial', 16), width=23, justify='center')
        delivery_time = Entry(bottomFrame2, textvariable=delivery_time_var, font=('arial', 16), width=23, justify='center')

        #====Grid Inserts====#
        serial_num.grid(row=0, column=1, pady=5)
        item_name.grid(row=1, column=1, pady=5)
        price_listed.grid(row=3, column=1, pady=5)
        price_cost.grid(row=4, column=1, pady=5)
        unit.grid(row=5, column=1, pady=5)
        install_time.grid(row=8, column=1, pady=5, sticky=W)
        delivery_time.grid(row=9, column=1, pady=5, sticky=W)

        def write2db():
            ###UPDATE THIS SCRIPT###
            insertNewPart = """INSERT INTO (part_supplier_id, part_number, part_name, part_quantity_available, \
            part_quantity_onhand, part_price, part_cost, part_unit, part_install_time, part_estimated_deliver_time) \
            VALUES ({},{},{},{},{},{},{},{},{},{})"""

            part_records = (dropdown_sup, serial_num.get(), item_name.get(), 0, 0, price_listed.get(), price_cost.get(), unit.get(), install_time.get(), delivery_time.get())

            with mydb.cursor() as cursor:
                cursor.execute(insertNewPart, part_records)
                mydb.commit()
                cursor.close()
            
        def clearEntries():
            serial_num_var.set('')
            item_name_var.set('')
            dropdown_sup.set("Choose One")
            price_listed_var.set('')
            price_cost_var.set('')
            unit_var.set('')
            install_time_var.set('')
            delivery_time_var.set('')
            

        #====Buttons====#
        save_btn = Button(btnFrame2, text="Save", height=2, width=20, command=write2db).grid(row=0, column=0, padx=10, pady=15)
        clear_btn = Button(btnFrame2, text="Clear", height=2, width=20, command=clearEntries).grid(row=0, column=1, padx=10, pady=15)


class Vendors:
    def viewSupplier():
        top = Toplevel()
        top.title('Inventory Management - by MetSystems Inc.')
        #top.iconbitmap('C:/Users/Jason/Documents/GMU/2021-01-Spring/IT-493_Capstone/ProjectFiles/favicon.ico')
        
        #====window frames=====#
        topFrame = Frame(top)
        topFrame.config(bg="#BDBDBD", width=600)
        topFrame.pack(pady=20)

        midFrame = Frame(top)
        midFrame.config(bg="#BDBDBD")
        midFrame.pack(pady=10)

        bottomFrame = Frame(top)
        bottomFrame.config(bg="#BDBDBD")
        bottomFrame.pack(pady=20)

        #=====header label=====#
        add_label = Label(topFrame, text="          Suppliers          ", fg="#003B6D", bg="#BDBDBD", font="Verdana 36 bold").grid(row=0, pady=20)
        top.geometry("800x950")
        top.config(bg="#BDBDBD")

        #====sort by dropdown====#
        dropDWN = StringVar(topFrame)
        dropDWN.set("Sort By:")

        dd = OptionMenu(topFrame, dropDWN, "ID", "Name", "Price", "QTY Avail.", "QTY On Hand")
        dd.config(width=15, anchor=W)
        dd.grid(row=1, column=0, sticky=E, padx=10)

        okBTN = Button(topFrame, text="GO")#, command=sortBy)
        okBTN.grid(row=1, column=1, sticky=E)

        

        #====SELECT from DB====#
        def selectEntries():
            mycursor = mydb.cursor()
            mycursor.execute("SELECT supplier_id, supplier_company, supplier_contact_first, supplier_contact_last, supplier_email, supplier_contact_phone FROM supplier")
            myresult = mycursor.fetchall()
            count = 0
            for row in myresult:
                supplier_tree.insert('', 'end', iid=count, text="", values=(row[0], row[1], row[2], row[3], row[4], row[5]))
                count += 1
            mycursor.close()

        #def sortBy():
            #insert SQL script to SELECT and ORDER BY

        #====Treeview====#
        tree_scroll = Scrollbar(midFrame, orient=VERTICAL)
        tree_scroll.pack(side=RIGHT, fill=Y)

        supplier_tree = ttk.Treeview(midFrame, yscrollcommand=tree_scroll.set, height=30)
        supplier_tree['columns'] = ("ID", "Name", "Contact First Name", "Contact Last Name", "Contact Email", "Contact Phone")
        
        supplier_tree.column("#0", width=0, stretch=NO)
        supplier_tree.column("ID", width=50, anchor=E)
        supplier_tree.column("Name", width=300, anchor=CENTER)
        supplier_tree.column("Contact First Name", width=100, anchor=CENTER)
        supplier_tree.column("Contact Last Name", width=100, anchor=CENTER)
        supplier_tree.column("Contact Email", width=100, anchor=CENTER)
        supplier_tree.column("Contact Phone", width=100, anchor=CENTER)

        supplier_tree.heading("#0", text="")
        supplier_tree.heading("ID", text="ID")
        supplier_tree.heading("Name", text="Name")
        supplier_tree.heading("Contact First Name", text="Contact First Name")
        supplier_tree.heading("Contact Last Name", text="Contact Last Name")
        supplier_tree.heading("Contact Email", text="Contact Email")
        supplier_tree.heading("Contact Phone", text="Contact Phone")

        
        selectEntries()
        
        supplier_tree.pack()
        tree_scroll.config(command=supplier_tree.yview)

        def selectItem(a):
            curItem = supplier_tree.focus()
            print (supplier_tree.item(curItem))
            global y
            x = (supplier_tree.item(curItem, 'values'))
            y = (x[0]) 

           

        #a = supplier_tree.bind('<ButtonRelease-1>', selectItem)

        supplier_tree.bind('<ButtonRelease-1>', selectItem)
        
        #print (a)

        #=====Buttons=====#
        addSupplierBTN = Button(bottomFrame, text="Add New Supplier", padx=20, pady=10, font="Verdana 14", command=Vendors.addSupplier)
        addSupplierBTN.grid(column=0, row=0, padx=20)

        viewSupplierBTN = Button(bottomFrame, text="View/Edit", padx=20, pady=10, font="Verdana 14", command=Vendors.viewInfo)
        viewSupplierBTN.grid(column=1, row=0, padx=20)

        delSupplierBTN = Button(bottomFrame, text="Delete Supplier", padx=20, pady=10, font="Verdana 14")#, command=Vendors.viewInfo)
        delSupplierBTN.grid(column=2, row=0, padx=20)

      

    

    def viewInfo():
        print (y)


        top = Toplevel()
        top.title('Add New Item')
        #top.iconbitmap('C:/Users/Jason/Documents/GMU/2021-01-Spring/IT-493_Capstone/ProjectFiles/favicon.ico')
        
        #====window frames=====#
        topFrame = Frame(top)
        topFrame.config(bg="#BDBDBD")
        topFrame.pack(pady=50)

        bottomFrame = Frame(top)
        bottomFrame.config(bg="#BDBDBD")
        bottomFrame.pack()

        btnFrame = Frame(top)
        btnFrame.config(bg="#BDBDBD")
        btnFrame.pack(pady=0)

        #=====header label=====#
        add_label = Label(topFrame, text="View Record Info", fg="#003B6D", bg="#BDBDBD", font="Verdana 36 bold").pack()
        top.geometry("800x950")
        top.config(bg="#BDBDBD")

        #-----------------------------#
        #====Create Variables====#
        
        supplier_name_var = StringVar()
        contact_first_var = StringVar()
        contact_last_var = StringVar()
        contact_email_var = StringVar()
        contact_phone_var = StringVar()
        address_var = StringVar()
        city_var = StringVar()
        state_var = StringVar()
        zip_var = IntVar()
        

        
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM supplier WHERE supplier_id = {};".format(y))
        myresult = mycursor.fetchall()
           
        for row in myresult:
            supplier_name_var.set(row[1]) 
            contact_first_var.set(row[2]) 
            contact_last_var.set(row[3]) 
            contact_email_var.set(row[4]) 
            contact_phone_var.set(row[5])
            address_var.set(row[6])
            city_var.set(row[7])
            state_var.set(row[8])
            zip_var.set(row[9])
                
        mycursor.close()


         #====Input Field Labels====#
        supplier_name_Label = Label(bottomFrame, text="Supplier Name: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=0, sticky=W)
        contact_first_Label = Label(bottomFrame, text="Contact First Name: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=1, sticky=W)
        contact_last_Label = Label(bottomFrame, text="Contact Last Name: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=2, sticky=W)
        contact_email_Label = Label(bottomFrame, text="Contact Email: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=3, sticky=W)
        contact_phone_Label = Label(bottomFrame, text="Contact Phone: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=4, sticky=W)
        address_Label = Label(bottomFrame, text="Address: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=5, sticky=W)
        city_Label = Label(bottomFrame, text="City: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=6, sticky=W)
        state_Label = Label(bottomFrame, text="State: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=7, sticky=W)
        zip_Label = Label(bottomFrame, text="Zip: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=8, sticky=W)
        
        supplier_name_Entry = Entry(bottomFrame, textvariable=supplier_name_var, font="Verdana 11 bold")
        contact_first_Entry = Entry(bottomFrame, textvariable=contact_first_var, font="Verdana 11 bold")
        contact_last_Entry = Entry(bottomFrame, textvariable=contact_last_var, font="Verdana 11 bold")
        contact_email_Entry = Entry(bottomFrame, textvariable=contact_email_var, font="Verdana 11 bold")
        contact_phone_Entry = Entry(bottomFrame, textvariable=contact_phone_var, font="Verdana 11 bold")
        address_Entry = Entry(bottomFrame, textvariable=address_var, font="Verdana 11 bold")
        city_Entry = Entry(bottomFrame, textvariable=city_var, font="Verdana 11 bold")
        state_Entry = Entry(bottomFrame, textvariable=state_var, font="Verdana 11 bold")
        zip_Entry = Entry(bottomFrame, textvariable=zip_var, font="Verdana 11 bold")
        
        supplier_name_Entry.grid(row=0, column=1, sticky=W, pady=5)
        contact_first_Entry.grid(row=1, column=1, sticky=W, pady=5)
        contact_last_Entry.grid(row=2, column=1, sticky=W, pady=5)
        contact_email_Entry.grid(row=3, column=1, sticky=W, pady=5)
        contact_phone_Entry.grid(row=4, column=1, sticky=W, pady=5)
        address_Entry.grid(row=5, column=1, sticky=W, pady=5)
        city_Entry.grid(row=6, column=1, sticky=W, pady=5)
        state_Entry.grid(row=7, column=1, sticky=E, pady=5)
        zip_Entry.grid(row=8, column=1, sticky=W, pady=5)

        def write2db():
            ###UPDATE THIS SCRIPT###
            insertNewSupplier = """INSERT INTO (supplier_company, supplier_contact_first, supplier_contact_last, supplier_email, \
            supplier_contact_phone, supplier_address, supplier_city, supplier_state, supplier_zip) \
            VALUES ({},{},{},{},{},{},{},{},{})"""

            supplier_records = (supplier_name_Entry.get(), contact_first_Entry.get(), contact_last_Entry.get(), contact_email_Entry.get(), contact_phone_Entry.get(), address_Entry.get(), city_Entry.get(), state_Entry.get(), zip_Entry.get())

            with mydb.cursor() as cursor:
                cursor.execute(insertNewSupplier, supplier_records)
                mydb.commit()
                cursor.close()
            
        def clearEntries():
            supplier_name_var.set('')
            contact_first_var.set('')
            contact_last_var.set('')
            contact_email_var.set('')
            contact_phone_var.set('')
            address_var.set('')
            city_var.set('')
            state_var.set('')
            zip_var.set('')
            

        #====Buttons====#
        save_btn = Button(btnFrame, text="Save", height=2, width=20, command=write2db).grid(row=0, column=0, padx=10, pady=15)
        clear_btn = Button(btnFrame, text="Clear", height=2, width=20, command=clearEntries).grid(row=0, column=1, padx=10, pady=15)

        

    def addSupplier():
        top = Toplevel()
        top.title('Add New Item')
        #top.iconbitmap('C:/Users/Jason/Documents/GMU/2021-01-Spring/IT-493_Capstone/ProjectFiles/favicon.ico')
        
        #====window frames=====#
        topFrame = Frame(top)
        topFrame.config(bg="#BDBDBD")
        topFrame.pack(pady=50)

        bottomFrame = Frame(top)
        bottomFrame.config(bg="#BDBDBD")
        bottomFrame.pack()

        btnFrame = Frame(top)
        btnFrame.config(bg="#BDBDBD")
        btnFrame.pack(pady=0)

        #=====header label=====#
        add_label = Label(topFrame, text="Add New Supplier", fg="#003B6D", bg="#BDBDBD", font="Verdana 36 bold").pack()
        top.geometry("800x950")
        top.config(bg="#BDBDBD")

        #-----------------------------#
        #====Create Variables====#
        
        supplier_name_var = StringVar()
        contact_first_var = StringVar()
        contact_last_var = StringVar()
        contact_email_var = StringVar()
        contact_phone_var = StringVar()
        address_var = StringVar()
        city_var = StringVar()
        state_var = StringVar()
        zip_var = IntVar()

         #====Input Field Labels====#
        supplier_name_Label = Label(bottomFrame, text="Supplier Name: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=0, sticky=W)
        contact_first_Label = Label(bottomFrame, text="Contact First Name: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=1, sticky=W)
        contact_last_Label = Label(bottomFrame, text="Contact Last Name: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=2, sticky=W)
        contact_email_Label = Label(bottomFrame, text="Contact Email: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=3, sticky=W)
        contact_phone_Label = Label(bottomFrame, text="Contact Phone: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=4, sticky=W)
        address_Label = Label(bottomFrame, text="Address: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=5, sticky=W)
        city_Label = Label(bottomFrame, text="City: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=6, sticky=W)
        state_Label = Label(bottomFrame, text="State: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=7, sticky=W)
        zip_Label = Label(bottomFrame, text="Zip: ", bg="#BDBDBD", font="Verdana 11 bold").grid(row=8, sticky=W)
        
        supplier_name_Entry = Entry(bottomFrame, textvariable=supplier_name_var, font="Verdana 11 bold")
        contact_first_Entry = Entry(bottomFrame, textvariable=contact_first_var, font="Verdana 11 bold")
        contact_last_Entry = Entry(bottomFrame, textvariable=contact_last_var, font="Verdana 11 bold")
        contact_email_Entry = Entry(bottomFrame, textvariable=contact_email_var, font="Verdana 11 bold")
        contact_phone_Entry = Entry(bottomFrame, textvariable=contact_phone_var, font="Verdana 11 bold")
        address_Entry = Entry(bottomFrame, textvariable=address_var, font="Verdana 11 bold")
        city_Entry = Entry(bottomFrame, textvariable=city_var, font="Verdana 11 bold")
        state_Entry = Entry(bottomFrame, textvariable=state_var, font="Verdana 11 bold")
        zip_Entry = Entry(bottomFrame, textvariable=zip_var, font="Verdana 11 bold")
        
        supplier_name_Entry.grid(row=0, column=1, sticky=W, pady=5)
        contact_first_Entry.grid(row=1, column=1, sticky=W, pady=5)
        contact_last_Entry.grid(row=2, column=1, sticky=W, pady=5)
        contact_email_Entry.grid(row=3, column=1, sticky=W, pady=5)
        contact_phone_Entry.grid(row=4, column=1, sticky=W, pady=5)
        address_Entry.grid(row=5, column=1, sticky=W, pady=5)
        city_Entry.grid(row=6, column=1, sticky=W, pady=5)
        state_Entry.grid(row=7, column=1, sticky=E, pady=5)
        zip_Entry.grid(row=8, column=1, sticky=W, pady=5)

        def write2db():
            ###UPDATE THIS SCRIPT###
            insertNewSupplier = """INSERT INTO (supplier_company, supplier_contact_first, supplier_contact_last, supplier_email, \
            supplier_contact_phone, supplier_address, supplier_city, supplier_state, supplier_zip) \
            VALUES ({},{},{},{},{},{},{},{},{})"""

            supplier_records = (supplier_name_Entry.get(), contact_first_Entry.get(), contact_last_Entry.get(), contact_email_Entry.get(), contact_phone_Entry.get(), address_Entry.get(), city_Entry.get(), state_Entry.get(), zip_Entry.get())

            with mydb.cursor() as cursor:
                cursor.execute(insertNewSupplier, supplier_records)
                mydb.commit()
                cursor.close()
            
        def clearEntries():
            supplier_name_var.set('')
            contact_first_var.set('')
            contact_last_var.set('')
            contact_email_var.set('')
            contact_phone_var.set('')
            address_var.set('')
            city_var.set('')
            state_var.set('')
            zip_var.set('')
            

        #====Buttons====#
        save_btn = Button(btnFrame, text="Save", height=2, width=20, command=write2db).grid(row=0, column=0, padx=10, pady=15)
        clear_btn = Button(btnFrame, text="Clear", height=2, width=20, command=clearEntries).grid(row=0, column=1, padx=10, pady=15)


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

viewVendorsBTN = Button(bottomFrame, text="View Suppliers", padx=103, pady=20, font="Verdana 16", command=Vendors.viewSupplier)
viewVendorsBTN.pack(pady=20)

updateQuantityBTN = Button(bottomFrame, text="Update Qty", padx=114, pady=20, font="Verdana 16", command=Quantity.updateQty)
updateQuantityBTN.pack(pady=20)


def close_window():
    msg = messagebox.askquestion("Quit", "Are you sure you want to quit?", icon="warning")
    if msg == "yes":
        mydb.close()
        mydb.disconnect()
        print(mydb)
        root.destroy()

root.protocol("WM_DELETE_WINDOW", close_window)



#run the main loop -- this is the program running
root.mainloop()
#=====End DB Connection====#
#mydb.close()
