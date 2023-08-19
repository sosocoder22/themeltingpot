from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import time
from datetime import date
import random
from tkinter import filedialog,messagebox
import tempfile
import os
import sqlite3



class IMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Billing Software | Developed By Cvani Phuyel")
        self.root.config(background="#003535")
        self.root.geometry("1500x750+10+10")
        self.root.resizable(True,True)
        self.img=Image.open("billImg.jpg")
        self.imgResize=self.img.resize((200,100),Image.LANCZOS)
        self.icon=ImageTk.PhotoImage(self.imgResize)

        global myList1
        global sum
        global total
        invoiceList=[]
        

        def register():
           global first_name_entry,last_name_entry,num,dob,points
           global custLevel
           global search_num
           custLevel=Toplevel(bg="black")
           custLevel.geometry("500x500+100+100")
           title=Label(custLevel,text="CUSTOMER REGISTRATION FORM",bg="green",fg="white",font=("times new roman",20))
           title.pack(fill=X)
           search_cust=Label(custLevel,text="enter number to search",bg="black",fg="white",font=("times new roman",15))
           search_cust.place(x=20,y=80)
           search_num=Entry(custLevel,bg="white",fg="black",width=20,font=("times new roman",15))
           search_num.place(x=220,y=80)
           
           search_button=Button(custLevel,text="lookup",bg="green",fg="white",command=getData)
           search_button.place(x=390,y=80)

           diffFrame=Frame(custLevel,bg="grey",width=460,height=300)
           diffFrame.place(x=20,y=152)
           
           first_name=Label(diffFrame,text="FIRST NAME",bg="grey",fg="white",font=("times new roman",15),cursor="hand2")
           first_name.place(x=0,y=0)
           first_name_entry=Entry(diffFrame,bg="white",fg="black",width=20,font=("times new roman",15))
           first_name_entry.place(x=180,y=0)

           last_name=Label(diffFrame,text="LAST NAME",bg="grey",fg="white",font=("times new roman",15))
           last_name.place(x=0,y=50)
           last_name_entry=Entry(diffFrame,bg="white",fg="black",width=20,font=("times new roman",15))
           last_name_entry.place(x=180,y=50)

           num_label=Label(diffFrame,text="MOBILE NUMBER",bg="grey",fg="white",font=("times new roman",15))
           num_label.place(x=0,y=100)
           num=Entry(diffFrame,bg="white",fg="black",width=20,font=("times new roman",15))
           num.place(x=180,y=100)

           dob_label=Label(diffFrame,text="BIRTHDAY",bg="grey",fg="white",font=("times new roman",15))
           dob_label.place(x=0,y=150)
           dob=Entry(diffFrame,bg="white",fg="black",width=20,font=("times new roman",15))
           dob.place(x=180,y=150)
           dob.insert(0,"dd/mm/yy")

           points_label=Label(diffFrame,text="LOYALTY POINTS",bg="grey",fg="white",font=("times new roman",15))
           points_label.place(x=0,y=200)
           points=Entry(diffFrame,bg="white",fg="black",width=20,font=("times new roman",15))
           points.place(x=180,y=200)

           save_button=Button(diffFrame,text="SAVE",bg="WHITE",fg="BLACK",width=10,command=sql)
           save_button.place(x=200,y=250)


           
         

        def getData():
           first_name_entry.delete(0,END)
           last_name_entry.delete(0,END)
           num.delete(0,END)
           dob.delete(0,END)
           points.delete(0,END)
           

           conn=sqlite3.connect("cust.db")
           cur=conn.cursor()

           cur.execute('''SELECT * FROM cust''')
           val=cur.fetchall()

           for i in val:
            if(i[2]==search_num.get()):
               first_name_entry.insert(0,i[0])
               last_name_entry.insert(0,i[1])
               num.insert(0,i[2])
               dob.insert(0,i[3])
               points.insert(0,i[4])
           
           
           conn.commit()

           cur.close()
           conn.close()

        def sql():
           tupl=[(first_name_entry.get(),last_name_entry.get(),num.get(),dob.get(),points.get())]
           conn=sqlite3.connect("cust.db")
           cur=conn.cursor()

           cur.execute('''CREATE TABLE IF NOT EXISTS cust(
                       first_name TEXT,last_name TEXT,number TEXT,birthday DATE,points INT
           )''')

           cur.executemany('''INSERT INTO cust VALUES(?,?,?,?,?)''',tupl)

           first_name_entry.delete(0,END)
           last_name_entry.delete(0,END)
           num.delete(0,END)
           dob.delete(0,END)
           points.delete(0,END)

           messagebox.showinfo("information","customer registration completed!")

           custLevel.destroy()
           

           conn.commit()

           

           cur.close()
           conn.close()


       

        def saveData():
            customerName=name.get()
            customerMobile=mobile.get()
            custName.insert(END,customerName)
            custNum.insert(END,customerMobile)
            table1.config(state=DISABLED,text="occupied by"+customerName,font=("times new roman",15))
        
       

        #-------functions to add food items---------------#
       # def new():
          # for item in myList1.curselection():
               #  my_tree.insert(parent="",values=(myList1.get(ANCHOR),1,250),index=END,text="parent")

        def bevList():
            myList1=["afogato","hot chocolate","peach iced tea","iced americano"]
            myList.delete(0,END)
            for item in myList1:
              myList.insert(END,item)

        
              

        def entreeList():
            myList1=["seafood salad","ceaser salad"]
            myList.delete(0,END)
            for item in myList1:
              myList.insert(END,item)
     

        def savoryList():
            myList1=["kebab platter","moroccon roast chicken"]
            myList.delete(0,END)
            for item in myList1:
              myList.insert(END,item)

        def atgList():
            myList1=["sumai-seafood","sumai-chicken","sumai-veg","kung pao cottage cheese","nasi goreng"]
            myList.delete(0,END)
            for item in myList1:
              myList.insert(END,item)
        
        def sevenList():
            myList1=["kalebung's best(thakali)","himalayan platter"]
            myList.delete(0,END)
            for item in myList1:
              myList.insert(END,item)

        def houseList():
            myList1=["kalebung's best(thakali)","himalayan platter"]
            myList.delete(0,END)
            for item in myList1:
              myList.insert(END,item)

        def cakeList():
            myList1=["chocolate cake","red velvet cake","macaron","vanilla pudding","cheesecake","fudge brownies","apple pie"]
            myList.delete(0,END)
            for item in myList1:
              myList.insert(END,item)



       ###---------------function to update the search results----------###
        def update(data):
           myList.delete(0,END)
           #myList.insert(END,data)
           for item in data:
              myList.insert(END,item)
           



       ###--------------------function to check the items--------------###
        def check(e):
           typed=search.get()
           length_of_typed=len(typed)
           if typed=="":
              data=itemList
           else:
              data=[]
              for item in itemList:
                 if typed.lower() in item.lower()[0:length_of_typed]:
                    data.append(str(item))
                    
           update(data)     
         
                    
                    
          #---------------clock-----------------#
        def clock():
           hour=time.strftime("%I")
           minute=time.strftime("%M")
           second=time.strftime("%S")
           am_pm=time.strftime("%p")
           self.clk.config(text=hour+":"+minute+":"+second+" "+am_pm)
           self.clk.after(1000,clock)
        

        ###--------function to select a table---##
        def pickTable():
           global table1
           top=Toplevel()
           top.geometry("500x500+500+100")
           top.resizable(True,True)

           def form():
              global name,mobile,save
              customerForm=Toplevel()
              customerForm.geometry("500x500+500+100")
              #top.destroy()
              nameLabel=Label(customerForm,text="enter name")
              nameLabel.pack()
              name=Entry(customerForm)
              name.pack()
              mobileLabel=Label(customerForm,text="enter number")
              mobileLabel.pack()
              mobile=Entry(customerForm)
              mobile.pack()
              save=Button(customerForm,text="Save",command=saveData)
              save.pack()
              

           frame=Frame(top,bg="#446F66",width=500,height=500).pack()
           table=Label(top,fg="white",bg="#446F66",text="Pick A Table",font=("times new roman",30)).place(x=150,y=0)
           table1=Button(top,fg="black",bg="white",text="Table 1",font=("times new roman",20),command=form)
           table1.place(x=50,y=80)
           table2=Button(top,fg="black",bg="white",text="Table 2",font=("times new roman",20)).place(x=200,y=80)
           table3=Button(top,fg="black",bg="white",text="Table 3",font=("times new roman",20)).place(x=350,y=80)
           table4=Button(top,fg="black",bg="white",text="Table 4",font=("times new roman",20)).place(x=50,y=200)
           table5=Button(top,fg="black",bg="white",text="Table 5",font=("times new roman",20)).place(x=200,y=200)
           table6=Button(top,fg="black",bg="white",text="Table 6",font=("times new roman",20)).place(x=350,y=200)
           table7=Button(top,fg="black",bg="white",text="Table 7",font=("times new roman",20)).place(x=50,y=320)
           table8=Button(top,fg="black",bg="white",text="Table 8",font=("times new roman",20)).place(x=200,y=320)
           table9=Button(top,fg="black",bg="white",text="Table 9",font=("times new roman",20)).place(x=350,y=320)

        

      ##--function to delete  item from listbox----##

        def delete():
           for i in myList.curselection():
              myList.delete(ANCHOR)         

             
        #----------------------FUNCTION TO SELECT AN ITEM FROM THE LISTBOX----------#
        def select():
          global value
          global qty,itm,price
          for i in myList.curselection():
              value=int(entryBox.get())
              itm=myList.get(i)
              qty=value
              price=priceTag[myList.get(i)]*value
              invoice=[itm,qty,price]
              my_tree.insert(parent="",index=END,text="Parent",values=( myList.get(i),value,priceTag[myList.get(i)]*value))
              #billTree.insert(parent="",index=END,text="Parent",values=( myList.get(i),value,priceTag[myList.get(i)]*value))
              invoiceList.append(invoice)
              
            #delete()

      #-------------------------funtion to calculate the bill---------------####
        def add():
              global sum
              sum=0
              for i in my_tree.get_children():
                 values=(my_tree.item(i)["values"])
                 sum +=values[2]
              
          
              my_tree.insert(parent="",values=("Total Amount","",sum),index=END)
              
              total.config(state=DISABLED)
              receipt.config(state=NORMAL)
              #billTree.insert(parent="",values=("Total Amount","",sum),index=END)




        
       ##----FUNCTION TO CLEAR ALL THE RECORDS----###
        def clear_record():
          # display.destroy()
           display.delete(1.0,END)
           global billNo
           billNo=str(random.randint(1,10000))
           total.config(state=NORMAL)
           receipt.config(state=DISABLED)
          
           for i in my_tree.get_children():
              my_tree.delete(i)
              #billTree.delete(i)
              invoiceList.clear()

              
              
           

        ##----FUNCTION TO DELETE ALL THE RECORDS----###
        def delete_record():
           selected=my_tree.selection()
           my_tree.delete(selected)
           total.config(state=NORMAL)
           
          
               
               
            

           
              
           

       ##----FUNCTION TO PRINT THE BILL----###

        def getBill():
           
          
           global billTree
           #display.delete(1.0,END)
           today=str(date.today())
           #select=my_tree.selection()
           billNo=str(random.randint(1,10000))
           generate="        THE MELTING POT BILL\n\n" +" Receipt No:  BIll " + billNo +"    "+ today+ "\n ******************\n" \
                     #  + "Items" + "                       "+"Cost Of Items"+"\n*****************************\n" 
           
           
           

           display.insert(END,generate)
           display.insert(END," item"+"  "+"qty"+"  "+"price"+"\n")
           display.insert(END,"------------------\n")
           for i in invoiceList:
              display.insert(END,i[0]+"\n \t" +str(i[1])+"   "+str(i[2])+"\n")
           display.insert(END,"total amount"+"\t\t"+"            "+ str(sum))
           display.insert(END,"\n\n Thank You,We'd love to have you again!")
              

           
          # print(my_tree.detach())
           #billTree.insert(parent="",index=END,values=(select))
           #for i in myList.curselection():
              #billTree.insert(parent="",index=END,values=i)
             # print(my_tree.get_children())
             #display.insert(END,i)

         ###_----------function to save the file--------###
        def save():
           global url
           if display.get(1.0,END)=='\n':
              pass
           else:
              url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
              if url==None:
                 pass
              else:
                 bill_data=display.get(1.0,END)
                 url.write(bill_data)
                 url.close()
                 messagebox.showinfo('Information','Your Bill Is Succesfully Saved')

        def print_file():
           text=display.get(1.0,'end-1c')
           file=tempfile.mktemp(".txt")
           open(file,"w").write(text)
           os.startfile(file,"print")
           print("error")
           
              
        
          
        priceTag={
           "cheese cake":300,
           "red velvet cake":200,
           "nasi goreng":350,
           "kung pao cottage cheese":200,
           "sumai-veg":300,
           "sumai-chicken":650,
           "sumai-seafood":700,
           "ceaser salad":650,
           "seafood salad":200,
           "moroccon roast chicken":800,
           "kebab platter":750,
           "afogato":300,
           "hot chocolate":170,
           "peach iced tea":250,
           "iced americano":150,
           "kalebung's best(thakali)":300,
           "himalayan platter":350,
           "chocolate cake":170,
           "macaron":50,
           "vanilla pudding":120,
           "cheesecake":220,
           "fudge brownies":130,
           "apple pie":170

        }
        
              


       
       
        #-----HEADING-----#
        lbl=Label(self.root,text="THE MELTING POT BILLING",image=self.icon, compound=LEFT,font={"times new roman",200,"bold"},background="#002525",fg="#ffffff",anchor="w").place(x=0,y=0,relwidth=1,height=100)
       
       
        #-----CLOCK-------#
        self.clk=Label(self.root,text="", font=("times new roman",15),bg="#003535",fg="white")
        self.clk.place(x=1350,y=60,width=150,height=30)
        clock()
        

        


        #-----LEFT MENU----#
        left_menu=Frame(self.root,bg="black")
        left_menu.place(x=2,y=100,width=200,height=800)

        menu=Label(left_menu,text="MENU",font=("times new roman",30,"bold"),bg="black",fg="white").pack(side=TOP,fill=X)

        #-----buttons------#
        bevBtn=Button(left_menu,bg="white",fg="black",text="Beverages",font=("times new roman",17),activebackground="#003535",activeforeground="white",cursor="hand2",command=bevList).pack(side=TOP,fill=X)

        entree=Button(left_menu,bg="white",fg="black",text="Entree",font=("times new roman",17),activebackground="#003535",activeforeground="white",cursor="hand2",command=entreeList).pack(side=TOP,fill=X)

        savory=Button(left_menu,bg="white",fg="black",text="Savory Gourmets",font=("times new roman",17),activebackground="#003535",activeforeground="white",cursor="hand2",command=savoryList).pack(side=TOP,fill=X)
        
        atg=Button(left_menu,bg="white",fg="black",text="Around The Globe",font=("times new roman",17),activebackground="#003535",activeforeground="white",cursor="hand2",command=atgList).pack(side=TOP,fill=X)

        sevenSisters=Button(left_menu,bg="white",fg="black",text="Seven Sisters",font=("times new roman",17),activebackground="#003535",activeforeground="white",cursor="hand2",command=sevenList).pack(side=TOP,fill=X)

        House=Button(left_menu,bg="white",fg="black",text="House Specials",font=("times new roman",17),activebackground="#003535",activeforeground="white",cursor="hand2",command=houseList).pack(side=TOP,fill=X)

        Cakes=Button(left_menu,bg="white",fg="black",text="Cakes",font=("times new roman",17),activebackground="#003535",activeforeground="white",cursor="hand2",command=cakeList).pack(side=TOP,fill=X)


       ###--------------------creating customer registration form---------##
        customer=Button(left_menu,bg="green", fg="white",text='Customer Registration',font=("times new roman",15),command=register).pack(side=TOP,fill=X)
        #------------toplabel---------#
        topLabel=Frame(self.root,bg="black")
        topLabel.place(x=202,y=100,relwidth=1,height=50)

        newOrder=Button(topLabel,text="New Order",bg="#ba0000",fg="white",font=("times new roman",17),cursor="hand2",command=pickTable).pack(side=LEFT,fill=Y)
      
        #searchLabel=Label(topLabel,text="search items",font=("times new roman",15),fg="white",bg="black",padx=10).pack(fill=Y,side=LEFT)

        search=Entry(topLabel,width=20,bg="white",font=("calibri",15))
        search.pack(side=LEFT,fill=Y,padx=120)
        search.insert(0,"search items")
        search.focus()
        
        search.bind("<KeyRelease>",check)

        custName=Entry(topLabel,width=20,bg="white",font=("calibri",15))
        custName.pack(side=LEFT,padx=100)

        custNum=Entry(topLabel,width=20,bg="white",font=("calibri",15))
        custNum.pack(side=LEFT)

       # lookUp=Button(topLabel,text="look up",bg="green",fg="white",width=10)
       # lookUp.pack(side=LEFT,fill=Y)



        


         #----------creating the search frame-------------#
        searchFrame=Frame(self.root,bg="black")
        searchFrame.place(x=202,y=150,relheight=1,width=470)

   
       ##--------------------search result box-----------##
       
        myList=Listbox(searchFrame,font=("calibri",15),bg="white",fg="black")
        myList.pack(side=TOP,fill=BOTH,expand=True,pady=10,padx=30)
        itemList=["kebab platter","moroccon roast chicken","seafood salad","ceaser salad","sumai-seafood","sumai-chicken","sumai-veg",
                      "kung pao cottage cheese","nasi goreng","red velvet cake","cheese cake"]
        for item in itemList:
            myList.insert(0,item)

        entryBox=Entry(myList)
        entryBox.place(x=100,y=490,width=30,height=40)
        entryBox.insert(END,1)        

        selectButton=Button(searchFrame,text="Select",bg="#003535",fg="white",padx=15,bd=5,font=("times new roman",15),command=select).place(x=200,y=500)



        ##---------------------------bill section--------------------##
        billFrame=Frame(self.root,background="white").place(x=700,y=150,relheight=0.73,width=500)

        myScrollbar=Scrollbar(billFrame,orient=VERTICAL)
        myScrollbar.place(x=1200,y=150,relheight=0.73)

       ## item1=Label(billFrame,text="ITEMS",fg="white",bg="#003535",font=("times new roman",15))
       # item1.place(x=720,y=150)

       # qty=Label(billFrame,text="QUANTITY",fg="white",bg="#003535",font=("times new roman",15))
        #qty.place(x=880,y=150)

       # amount=Label(billFrame,text="AMOUNT",fg="white",bg="#003535",font=("times new roman",15))
       # amount.place(x=1070,y=150)

       # itemBox=Label(billFrame,bg="#003535",fg="white",text="")
       # itemBox.place(x=710,y=190,relheight=1,width=480)

        ##----------styling treeview-----##
        style=ttk.Style()
        
        style.configure("Treeview",
                        background="#003535",
                        foreground="white",
                        fieldbackground="grey",
                        font=("calibri",12),
                        rowheight=30)
        
        style.map("Treeview",background=[("selected","green")])

        my_tree=ttk.Treeview(billFrame)
        myScrollbar.config(command=my_tree.yview)
        my_tree.place(x=710,y=170,relheight=0.6,width=480)
        my_tree["columns"]=("ITEMS","QUANTITY","AMOUNT")
        my_tree.column("#0",anchor=W,width=10)
        my_tree.column("ITEMS",anchor=CENTER,width=200)
        my_tree.column("QUANTITY",anchor=CENTER,width=120)
        my_tree.column("AMOUNT",anchor=CENTER,width=150)
        
        my_tree.heading("#0",text="",anchor=W)
        my_tree.heading("ITEMS",text="ITEMS",anchor=CENTER)
        my_tree.heading("QUANTITY",text="QUANTITY",anchor=CENTER)
        my_tree.heading("AMOUNT",text="AMOUNT",anchor=CENTER)

       # my_tree.bind("<Double 1>",double_click)


        ###--------------section for total buttons---------##
        delete=Button(billFrame,bg="green",fg="white",text="Delete",padx=5,font=("times new roman",20),bd=5,command=delete_record).place(x=705,y=635)
        total=Button(billFrame,bg="green",fg="white",text="Total",padx=5,font=("times new roman",20),bd=5,command=add,state=NORMAL)
        total.place(x=810,y=635)
        save=Button(billFrame,bg="green",fg="white",text="Save",padx=5,font=("times new roman",20),bd=5,command=save).place(x=900,y=635)
        receipt=Button(billFrame,bg="green",fg="white",text="Receipt",padx=5,font=("times new roman",20),bd=5,command=getBill,state=DISABLED)
        receipt.place(x=985,y=635)
        clear=Button(billFrame,bg="green",fg="white",text="Clear",padx=5,font=("times new roman",20),bd=5,command=clear_record)
        clear.place(x=1100,y=635)

        #####---------bill generator frame---------###
        bill=Frame(root,bg="white")
        bill.place(x=1240,y=150,width=250,relheight=0.8)

        billLable=Label(bill,text="Billing Section",bg="green",fg='white',font=("times new roman",25),width=15)
        billLable.pack()

        display=Text(bill,fg="black",font=("times new roman",12,"bold"),bg="white")
        display.pack(side=TOP)

        cash=Button(bill,text="Cash",bg="green",fg="white",padx=5,bd=5,font=("times new roman",20),command=print_file)
        cash.place(relx=0,rely=0.84,width=120,height=50)

        card=Button(bill,text="Card",bg="green",fg="white",padx=5,bd=5,font=("times new roman",20),command=print_file)
        card.place(relx=0.5,rely=0.84,width=120,height=50)
        






        #------------bottom label----------------------------#
        bottomLabel=Label(self.root,text="Application created by Cvani Phuyel \n For any queries contact:8972422059",font=("calibri",13),bg="#003535",fg="white").pack(side=BOTTOM,fill=X)

       #-------------------databse functionality-------------###
        
        
        '''def insert():
           row=[num.get(),first_name_entry.get(),last_name_entry.get(),points.get]
           cur.execute("INSERT INTO customer(mobile,first Name,Last Name,points) values(row)")
           db.commit()
           messagebox.showinfo(title="saved",message="Registration Completed")'''
        
        
       



   


        

        

        


        

        

var1 =StringVar



root=Tk()
lbl1=IMS(root)



root.mainloop()


    