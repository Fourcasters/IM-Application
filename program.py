import sqlite3
from sqlite3 import Error
from tkinter import *
from tkinter import ttk
conn = sqlite3.connect("product_details.db")

window = Tk()
window.title("Product Details")
window.geometry('440x350')

product_h1 = StringVar()
product_h2 = StringVar()
product_h3 = StringVar()
product_h4 = StringVar()
product_onhand = [product_h1,product_h2,product_h3,product_h4]

product_a1 = StringVar()
product_a2 = StringVar()
product_a3 = StringVar()
product_a4 = StringVar()
product_avail = [product_a1,product_a2,product_a3,product_a4]


part_h1 = StringVar()
part_h2 = StringVar()
part_h3 = StringVar()
part_h4 = StringVar()
part_onhand = [part_h1,part_h2,part_h3,part_h4]

part_a1 = StringVar()
part_a2 = StringVar()
part_a3 = StringVar()
part_a4 = StringVar()
part_avail = [part_a1,part_a2,part_a3,part_a4]
def update_quantity():
    pass
def all_product_update():
    conn = sqlite3.connect("product_details.db")
    cursor = conn.cursor()
    for i in range(len(product_avail)):
        if product_avail[i].get() != "":
            cursor.execute('''UPDATE product SET product_quantity_available= ? WHERE product_id = ?''', (product_avail[i].get(),i+1))
    print("Product Quantities Updated")
    conn.commit()
    conn.close()

def all_product_update():
    conn = sqlite3.connect("product_details.db")
    cursor = conn.cursor()
    for i in range(len(product_avail)):
        if product_avail[i].get() != "":
            cursor.execute('''UPDATE product SET product_quantity_available= ? WHERE product_id = ?''', (product_avail[i].get(),i+1))
    print("Product Quantities Updated")
    conn.commit()
    conn.close()

def all_part_update():
    conn = sqlite3.connect("product_details.db")
    cursor = conn.cursor()
    for i in range(len(part_avail)):
         if part_avail[i].get() != "":
            cursor.execute('''UPDATE part SET part_quantity_available= ? WHERE part_id = ?''', (part_avail[i].get(),i+1))
    print("Part Quantities Updated")
    conn.commit()
    conn.close()

def productDetails():
    conn = sqlite3.connect("product_details.db")
    newWindow = Toplevel(window)

    newWindow.title("Product Details")

    newWindow.geometry("1114x150")
    e=Label(newWindow,width=15,text='Product Id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=0)
    e=Label(newWindow,width=15,text='Product Supplier Id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=1)
    e=Label(newWindow,width=15,text='Product No',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=2)
    e=Label(newWindow,width=15,text='Product Name',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=3)
    e=Label(newWindow,width=15,text='Product Quantity Available',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=4)
    e=Label(newWindow,width=15,text='Product Quantity on Hand',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=5)
    e=Label(newWindow,width=15,text='Product Price',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=6)
    e=Label(newWindow,width=15,text='Product Cost',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=7)
    e=Label(newWindow,width=15,text='Product Unit',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=8)
    e=Label(newWindow,width=15,text='Product Part Predecessor',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=9)
    cursor = conn.cursor()

    cursor.execute('''SELECT * from product''')

    rows = cursor.fetchall();
    i = 0
    for row in rows: 
        for j in range(len(row)):
            e = Label(newWindow,width=15, text=row[j],borderwidth=2, relief='ridge',anchor='w',bg='white') 
            e.grid(row=i+1, column=j) 
        i=i+1


    conn.commit()
    conn.close()

def partDetails():
    conn = sqlite3.connect("product_details.db")
    newWindow = Toplevel(window)

    newWindow.title("Part Details")

    newWindow.geometry("1000x150")
    e=Label(newWindow,width=15,text='Part Id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=0)
    e=Label(newWindow,width=15,text='Part Supplier Id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=1)
    e=Label(newWindow,width=15,text='Part Serial No',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=2)
    e=Label(newWindow,width=15,text='Part Name',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=3)
    e=Label(newWindow,width=15,text='Part Quantity Available',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=4)
    e=Label(newWindow,width=15,text='Part Quantity on Hand',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=5)
    e=Label(newWindow,width=15,text='Part Price',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=6)
    e=Label(newWindow,width=15,text='Part Cost',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=7)
    e=Label(newWindow,width=15,text='Part Unit',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=8)

    cursor = conn.cursor()

    cursor.execute('''SELECT * from part''')

    rows = cursor.fetchall();
    i = 0
    for row in rows: 
        for j in range(len(row)):
            e = Label(newWindow,width=15, text=row[j],borderwidth=2, relief='ridge',anchor='w',bg='white') 
            e.grid(row=i+1, column=j) 
        i=i+1


    conn.commit()
    conn.close()


def createGUI():
    conn = sqlite3.connect("product_details.db")
    #newWindow = Toplevel(window)

    #newWindow.title("Part Details")

    #newWindow.geometry("450x150")
    part=Label(window,width=15,text='Part Id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    part.grid(row=0,column=0)
    part=Label(window,width=15,text='Part Name',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    part.grid(row=0,column=1)
    part=Label(window,width=30,text='Part Quantity Available',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    part.grid(row=0,column=2,columnspan=2)

    cursor = conn.cursor()

    cursor.execute('''SELECT * from part''')

    rows = cursor.fetchall();
    i = 0
    for row in rows:
        col = 0 
        for j in range(len(row)):
            
            if j == 0:
                part = Label(window,width=15, text=row[j],borderwidth=2, relief='ridge',anchor='w',bg='white') 
                part.grid(row=i+1, column=col)
                col += 1                    
            elif j == 3:
                part = Label(window,width=15, text=row[j],borderwidth=2, relief='ridge',anchor='w',bg='white') 
                part.grid(row=i+1, column=col)
                col += 1
            elif j == 4:
                part = Entry(window,width=15, textvariable=part_avail[i],bd=0)#,borderwidth=2, relief='ridge',anchor='w',bg='white')
                part.grid(row=i+1, column=col)
                col += 1  
              #i=i+1   
        part = ttk.Button(window, text ="Update", command = update_quantity)#,borderwidth=2, relief='ridge',anchor='w',bg='white')
        part.grid(row=i+1, column=col)       
        i=i+1
    i = i + 2
    update_all_part = ttk.Button(window, text ="Save All Updates", command = all_part_update).grid(row=i,column=0)
    
    conn.commit()
    conn.close()
    i = i + 2
    conn = sqlite3.connect("product_details.db")
    # newWindow = Toplevel(window)

    # newWindow.title("Product Details")

    # newWindow.geometry("430x150")
    product=Label(window,width=15,text='Product Id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    product.grid(row=i+1,column=0)
    product=Label(window,width=15,text='Product Name',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    product.grid(row=i+1,column=1)
    product=Label(window,width=30,text='Product Quantity Available',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    product.grid(row=i+1,column=2,columnspan=2)
    cursor = conn.cursor()

    cursor.execute('''SELECT * from product''')

    rows = cursor.fetchall();
    i = i + 1
    
    counter = 0
    for row in rows:
        col = 0 
        for j in range(len(row)):
            
            if j == 0:
                product = Label(window,width=15, text=row[j],borderwidth=2, relief='ridge',anchor='w',bg='white') 
                product.grid(row=i+1, column=col)
                col += 1                    
            elif j == 3:
                product = Label(window,width=15, text=row[j],borderwidth=2, relief='ridge',anchor='w',bg='white') 
                product.grid(row=i+1, column=col)
                col += 1
            elif j == 4:
                product = Entry(window,width=15, textvariable=product_avail[counter],bd=0)#,borderwidth=2, relief='ridge',anchor='w',bg='white')
                product.grid(row=i+1, column=col)
                col += 1  
                counter += 1
              #i=i+1   
        product = ttk.Button(window, text ="Update", command = update_quantity)#,borderwidth=2, relief='ridge',anchor='w',bg='white')
        product.grid(row=i+1, column=col)       
        i=i+1
    update_all_product = ttk.Button(window, text ="Save All Updates", command = all_product_update).grid(row=i+2,column=0)
    
    conn.commit()
    conn.close()
    product = ttk.Button(window, text ="Product", command = productDetails).grid(row=i + 4,column=1)
    part = ttk.Button(window, text ="Part", command = partDetails).grid(row= i + 4,column=2)

def main():
    createGUI()
    window.mainloop()
main()