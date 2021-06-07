from tkinter import *
from tkinter import messagebox,ttk,filedialog
import tkinter
from tkinter.font import Font
from PIL import Image, ImageTk
import mysql.connector
import os
from mysql.connector import Error
import Backend__Admin
import time
class AdminPage():
#   Functions
    def dashboard(self):
        
        self.dashboardButton = Button(self.frame1, text='Dashboard', bg='#464b53', fg='#F5F5F5', font=("Frankin Gothic Medium", 12), borderwidth=1,relief='flat',command=self.dashboardButton)
        self.dashboardButton.place(x=0, y=0, width=157, height=50)

        self.categoryButton = Button(self.frame1, text='Category', bg='#464b53', fg='#F5F5F5', font=("Frankin Gothic Medium", 12), borderwidth=1,relief='flat',command=self.categoryButton)
        self.categoryButton.place(x=0, y=55, width=157, height=50)

        self.subcategoryButton = Button(self.frame1, text='Sub-Category', bg='#464b53', fg='#F5F5F5', font=("Frankin Gothic Medium", 12), borderwidth=1,relief='flat',command=self.subCategoryButton)
        self.subcategoryButton.place(x=0, y=110, width=157, height=50)

        self.brandButton = Button(self.frame1, text='Brand', bg='#464b53', fg='#F5F5F5', font=("Frankin Gothic Medium", 12), borderwidth=1,relief='flat',command=self.brandButton)
        self.brandButton.place(x=0, y=165, width=157, height=50)

        self.productButton = Button(self.frame1, text='Product', bg='#464b53', fg='#F5F5F5', font=("Frankin Gothic Medium", 12), borderwidth=1,relief='flat',command=self.productButton)
        self.productButton.place(x=0, y=220, width=157, height=50)

        self.inventoryButton = Button(self.frame1, text='Inventory', bg='#464b53', fg='#F5F5F5', font=("Frankin Gothic Medium", 12), borderwidth=1,relief='flat',command=self.inventoryButton)
        self.inventoryButton.place(x=0, y=275, width=157, height=50)

        self.searchButton = Button(self.frame1, text='Search', bg='#464b53', fg='#F5F5F5', font=("Frankin Gothic Medium", 12), borderwidth=1,relief='flat',command=self.searchButton)
        self.searchButton.place(x=0, y=330, width=157, height=50)

        self.cartButton = Button(self.frame1, text='Cart', bg='#464b53', fg='#F5F5F5', font=("Frankin Gothic Medium", 12), borderwidth=1,relief='flat',command=self.cartButton)
        self.cartButton.place(x=0, y=385, width=157, height=50)

        # self.customerDetailsButton = Button(self.frame1, text='Customer Details', bg='#464b53', fg='#F5F5F5', font=("Frankin Gothic Medium", 12), borderwidth=1,relief='flat',command=self.customerDetails)
        # self.customerDetailsButton.place(x=0, y=440, width=157, height=50)

        self.reportButton = Button(self.frame1, text='Report', bg='#464b53', fg='#F5F5F5', font=("Frankin Gothic Medium", 12), borderwidth=1,relief='flat',command=self.reportButton)
        self.reportButton.place(x=0, y=440, width=157, height=50)



        self.addCategoryButton =  Button(self.root, text='Add Category', bg='#464b53', fg='#F5F5F5', font=("Frankin Gothic Medium", 12), borderwidth=1,relief='flat',command=self.addCategoryButton)
        self.manageCategoryButton =  Button(self.root, text='Manage Category', bg='#464b53', fg='#F5F5F5', font=("Frankin Gothic Medium", 12), borderwidth=1,relief='flat',command=self.manageCategoryButton)

        self.addSubCategoryButton =  Button(self.root, text='Add Sub-Category', bg='#464b53', fg='#F5F5F5', font=("Frankin Gothic Medium", 12), borderwidth=1,relief='flat',command=self.addSubCategoryButton)
        self.manageSubCategoryButton =  Button(self.root, text='Manage Sub-Category', bg='#464b53', fg='#F5F5F5', font=("Frankin Gothic Medium", 12), borderwidth=1,relief='flat' ,command=self.manageSubCategoryButton)
        
        self.addbrandButton =  Button(self.root, text='Add Brand', bg='#464b53', fg='#F5F5F5', font=("Frankin Gothic Medium", 12), borderwidth=1,relief='flat' ,command=self.addbrandButton)
        self.managebrandButton =  Button(self.root, text='Manage Brand', bg='#464b53', fg='#F5F5F5', font=("Frankin Gothic Medium", 12), borderwidth=1,relief='flat'  ,command=self.managebrandButton)
        
        self.addproductButton =  Button(self.root, text='Add Product', bg='#464b53', fg='#F5F5F5', font=("Frankin Gothic Medium", 12), borderwidth=1,relief='flat' ,command=self.addproductButton)
        self.manageproductButton =  Button(self.root, text='Manage Product', bg='#464b53', fg='#F5F5F5', font=("Frankin Gothic Medium", 12), borderwidth=1,relief='flat',command=self.manageproductButton)


        self.welcomeAdminButton =  Button(self.frame2, text = 'Welcome Admin', bg='#464b53', fg='#F5F5F5', font=("Frankin Gothic Medium", 10), borderwidth=2,relief='flat'  ,command=self.welcomeAdminButton)
        self.welcomeAdminButton.place(x=0,y=0, height=33)

        self.changePasswordButton =  Button(self.frame2, text = 'Change Password', bg='#464b53', fg='#F5F5F5', font=("Frankin Gothic Medium", 10), borderwidth=2,relief='flat'  ,command=self.changepasswordbutton)
        self.changePasswordButton.place(x=108,y=0, height=33)

        self.logoutButton =  Button(self.frame2, text = 'Logout', bg='#464b53', fg='#F5F5F5', font=("Frankin Gothic Medium", 10), borderwidth=2,relief='flat'  ,command=self.logoutButton)
        self.logoutButton.place(x=320,y=0, height=33)

        x=1
        self.thresholdButton=Button(self.frame2, text = ('Threshold: ',x), bg='#464b53', fg='#F5F5F5', font=("Frankin Gothic Medium", 10), borderwidth=2,relief='flat'  ,command=self.thresholdButton)
        self.thresholdButton.place(x=225,y=0, height=33)

    def dashboardButton(self):
        self.buttonName='dashboardButton'
        self.hide_unhideButton(self.buttonName)
        admin=AdminPage(root)
            
    def categoryButton(self):
        self.buttonName='categoryButton'
        self.hide_unhideButton(self.buttonName)
        self.frame1.tkraise()
        self.addCategoryButton.place(x=156, y=125, width=157, height=25)
        self.manageCategoryButton.place(x=156, y=150, width=157, height=25) 
        
    def subCategoryButton(self):
        self.buttonName='subCategoryButton'
        self.hide_unhideButton(self.buttonName)
        self.frame1.tkraise()
        self.addSubCategoryButton.place(x=156, y=180, width=160, height=25)
        self.manageSubCategoryButton.place(x=156, y=205, width=160, height=25)
             
    def brandButton(self):
        self.buttonName='brandButton'
        self.hide_unhideButton(self.buttonName)        
        self.frame1.tkraise()
        self.addbrandButton.place(x=156, y=235, width=160, height=25)
        self.managebrandButton.place(x=156, y=260, width=160, height=25)
         
    def productButton(self):
        self.buttonName='productButton'
        self.hide_unhideButton(self.buttonName)
        self.frame1.tkraise()
        self.addproductButton.place(x=156, y=290, width=160, height=25)
        self.manageproductButton.place(x=156, y=315, width=160, height=25)
         
    def inventoryButton(self):
        self.buttonName='cartButton'
        self.frame1.tkraise()
        self.hide_unhideButton(self.buttonName)
        Backend__Admin.inventory(self)
        
         
    def searchButton(self):
        self.buttonName='searchButton'
        self.frame1.tkraise()
        self.hide_unhideButton(self.buttonName)
        for widgets in self.frame3.winfo_children():
            widgets.destroy()

        searchLabel=Label(self.frame3,font=Font(family="Times New Roman",size=15),text="Search for :")
        searchLabel.place(x=10,y=70)
        searchEntry = Entry(self.frame3, font=Font(family="Times New Roman",size=15))
        searchEntry.place(x=120, y=70)

        searchByLabel =Label(self.frame3,font=Font(family="Times New Roman",size=15),text="Search by :")
        searchByLabel.place(x=350, y=70)
        searchByComboBox= ttk.Combobox(self.frame3, state="readonly")
        searchByComboBox["values"]=['Product Name','Brand','Sub-Category','Category']
        searchByComboBox.set("Select")
        searchByComboBox.place(x=455,y=70,height=28)

        orderByLabel =Label(self.frame3,font=Font(family="Times New Roman",size=15),text="Sort order :")
        orderByLabel.place(x=650, y=70)
        orderByComboBox= ttk.Combobox(self.frame3, state="readonly")
        orderByComboBox["values"]=['Ascending','Descending']
        orderByComboBox.set("Select")
        orderByComboBox.place(x=750,y=70,height=28)


        searchButton =Button(self.frame3, font=Font(family="Times New Roman",size=12), text=("Search"), anchor=CENTER ,relief=SOLID,command=lambda: Backend__Admin.search(self,searchEntry.get(),searchByComboBox.get(),orderByComboBox.get()))
        searchButton.place(x=900, y=70,width=100)
        
        
         
    def cartButton(self):
        self.buttonName='cartButton'
        self.frame1.tkraise()
        self.hide_unhideButton(self.buttonName)
        Backend__Admin.showCart(self)
        

         
    def customerDetails(self):
        self.buttonName='customerDetails'
        self.frame1.tkraise()
        self.hide_unhideButton(self.buttonName)
         
    def reportButton(self):
        # self.frame1.tkraise()
        Backend__Admin.showTransact(self)
         
    def hide_unhideButton(self,buttonName):
        print(buttonName)
        subButtonList=(self.addCategoryButton,self.manageCategoryButton,self.addSubCategoryButton,self.manageSubCategoryButton,self.addbrandButton,
                                self.managebrandButton,self.addproductButton,self.manageproductButton)
        for i in subButtonList:
            print(i)
            if(i!=buttonName):
                i.place_forget()
        


    def addCategoryButton(self):
        #self.frame3.tkraise()
        self.addCategoryButton.place_forget()
        self.manageCategoryButton.place_forget()
        for widgets in self.frame3.winfo_children():
            widgets.destroy()
            
        titleFont = Font(family="Times New Roman",size=25, weight="bold")
        labelFont = Font(family="Times New Roman",size=15)
        entryFont = Font(family="Times New Roman",size=14)
        buttonFont = Font(family="Times New Roman",size=18)

        
        titleLabel = Label(self.frame3, bg='gray', text ='Add Category', font=titleFont)
        titleLabel.place(x=30, y=10)

        frame = Frame(self.frame3)
        frame.place(x=30, y=200, width=950, height=300)

        boxLabel = Label(frame, relief='solid')
        boxLabel.place(x=0, y=0, width=950, height=300)

        boxTitleLabel = Label(frame, text ='Add Category', font=labelFont, relief=SOLID, anchor=W)
        boxTitleLabel.place(x=0, y=0, width=950, height=30)

        addCategoryLabel = Label(frame, text ='Category Name :', font=labelFont, anchor=E)
        addCategoryLabel.place(x=30, y=50)

        addCategoryEntry = Entry(frame, font=entryFont)
        addCategoryEntry.place(x=190, y=50)
        

        statusLabel = Label(frame, text ='Status :', font=labelFont, anchor=E)
        statusLabel.place(x=105, y=100)

        status =tkinter.StringVar()
        status.set("Inactive")
        statusCheckButton = Checkbutton(frame,variable=status,  textvariable=status,font=entryFont, height=1,offvalue = 'Inactive',
                          onvalue = 'Active')
        statusCheckButton.place(x=190, y=100)
        
        addCategoryButton = Button(frame, text ='Add Category', font=buttonFont)
        addCategoryButton.place(x=65, y=200)
        addCategoryButton.config(command=lambda:[Backend__Admin.AddCategory(status.get(),addCategoryEntry.get()), addCategoryEntry.delete(0,END), statusCheckButton.deselect()])
          
    def manageCategoryButton(self):
        self.addCategoryButton.place_forget()
        self.manageCategoryButton.place_forget()
        Backend__Admin.manageCategory(self)
        return

    def manageCategoryButtonFront(self):
                def recursion():
                    time.sleep(.5)
                    Backend__Admin.manageCategory(self)
                    self.manageCategoryButtonFront()
                self.addCategoryButton.place_forget()
                self.manageCategoryButton.place_forget()
                for widgets in self.frame3.winfo_children():
                    widgets.destroy()
                titleFont = Font(family="Times New Roman",size=25, weight="bold")
                labelFont = Font(family="Times New Roman",size=20)
                entryFont = Font(family="Times New Roman",size=14)
                buttonFont = Font(family="Times New Roman",size=18)

                frame3 = Frame(self.frame3, bg='#1c748c')
                frame3.place(x=0, y=0, height = 685, width= 1240)
                
                titleLabel = Label(frame3, bg='gray', text ='Manage Category', font=titleFont)
                titleLabel.place(x=30, y=10)

                Mainframe = Frame(frame3)
                Mainframe.place(x=10, y=100, width=1170, height=570)
                Mainframe1=Frame(Mainframe)
                
                
                myCanvas=Canvas(Mainframe1,width=1150,height=450)
                myScrollBar=ttk.Scrollbar(Mainframe1,orient=VERTICAL,command=myCanvas.yview)

                scrollFrame=Frame(myCanvas)
                scrollFrame.bind("<Configure>", lambda e:  myCanvas.configure(scrollregion=myCanvas.bbox("all")))

                myCanvas.create_window((0,0),window=scrollFrame, anchor=NW)
                myCanvas.configure(yscrollcommand=myScrollBar.set)
                

                boxLabel = Label(Mainframe, relief='solid')
                #boxLabel.place(x=0, y=0, width=1170, height=570)


                boxTitleLabel = Label(Mainframe, text ='Manage Category', font=labelFont, relief=SOLID, anchor=W)
                boxTitleLabel.place(x=0, y=0, width=1170, height=35)

                srLabel =Label(Mainframe, font=labelFont, text="Sr.No." , anchor=CENTER,relief="solid")
                srLabel.place(x=0, y=35,width=150)
                categoryNameLabel=Label(Mainframe,font=labelFont, text="Category Name", anchor=CENTER,relief="solid",width=25)
                categoryNameLabel.place(x=150, y=35,width=400)

                statusLabel=Label(Mainframe,font=labelFont, text="Category Status", anchor=CENTER,relief="solid",width=25)
                statusLabel.place(x=550, y=35, width=400)

                actionLabel=Label(Mainframe,text='Action',font=labelFont,relief=SOLID,width=14)
                actionLabel.place(x=950,y=35,width=200)

                
                sr=1
                records=Backend__Admin.records
                global pos
                yval=50
                for i in records:
                    if i[1]==1:
                        text="Active"
                    else:
                        text="Inactive"
                    print(i)
                    rowsrLabel=Label(scrollFrame, font=entryFont, text=sr, anchor=CENTER,relief=SOLID, width=14)
                    rowsrLabel.grid(row=sr,column=0)
                    

                    rowCatNameLabel=Label(scrollFrame, font=entryFont, text=(i[0]),relief=SOLID,width=39)
                    rowCatNameLabel.grid(row=sr,column=1)
                    #rowCatNameLabel.place(x=150,y=yval)


                    rowStatusLabel=Label(scrollFrame, font=entryFont, text=text,relief=SOLID,width=40)
                    rowStatusLabel.grid(row=sr,column=3)

                    rowEditButton=Button(scrollFrame, font=entryFont, text=("Edit"), anchor=CENTER ,relief=SOLID,width=9,height=0,command= lambda i=i:self.updateCategory(i[0]))
                    rowEditButton.grid(row=sr,column=4)

                    from Admin import AdminPage
                    rowDeleteButton=Button(scrollFrame, font=entryFont, text=("Delete"), anchor=CENTER ,relief=SOLID,width=9,height=0,command=lambda i=i:[Backend__Admin.deleteCategory(i[0]),recursion()])
                    rowDeleteButton.grid(row=sr,column=5)
                    sr=sr+1
                    yval=yval+30       
                Mainframe1.place(x=0,y=75)
                myCanvas.pack(side="left",fill="both",expand=True)
                myScrollBar.pack(side="right",fill="y")
                           
    def updateCategory(self,catName):
        #self.frame3.tkraise()
        for widgets in self.frame3.winfo_children():
                    widgets.destroy()
        titleFont = Font(family="Times New Roman",size=25, weight="bold")
        labelFont = Font(family="Times New Roman",size=15)
        entryFont = Font(family="Times New Roman",size=14)
        buttonFont = Font(family="Times New Roman",size=18)

        oldCatName=catName
        titleLabel = Label(self.frame3, bg='gray', text ='Update Category', font=titleFont)
        titleLabel.place(x=30, y=10)

        frame = Frame(self.frame3)
        frame.place(x=30, y=200, width=950, height=300)

        boxLabel = Label(frame, relief='solid')
        boxLabel.place(x=0, y=0, width=950, height=300)

        boxTitleLabel = Label(frame, text ='Update Category', font=labelFont, relief=SOLID, anchor=W)
        boxTitleLabel.place(x=0, y=0, width=950, height=30)

        CategoryLabel = Label(frame, text ='Category Name :', font=labelFont, anchor=E)
        CategoryLabel.place(x=30, y=50)

        CategoryEntry = Entry(frame, font=entryFont)
        CategoryEntry.insert("1",catName)
        CategoryEntry.place(x=190, y=50)

        statusLabel = Label(frame, text ='Status :', font=labelFont, anchor=E)
        statusLabel.place(x=105, y=100)

        status =tkinter.StringVar()
        status.set("Inactive")
        statusCheckButton = Checkbutton(frame,variable=status,  textvariable=status,font=entryFont, height=1,offvalue = 'Inactive',
                          onvalue = 'Active')
        statusCheckButton.place(x=190, y=100)

        updateCategoryButton = Button(frame, text ='Update Category', font=buttonFont)
        updateCategoryButton.place(x=65, y=200)
        updateCategoryButton.config(command=lambda:Backend__Admin.updateCategory(CategoryEntry.get(),status.get(),oldCatName))
        return

    def addSubCategoryButton(self):
        for widgets in self.frame3.winfo_children():
            widgets.destroy()

        conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="")
        if conn.is_connected():
            print("Database Connected")
            sql="SELECT category FROM category_subcategory"     
            Cursor=conn.cursor()
            Cursor.execute(sql)
            catList=Cursor.fetchall()
            list1=[]
            for i in catList:
                print(i[0])
                inp=i[0]
                list1.append(inp)
            catList=list1
        self.addSubCategoryButton.place_forget()
        self.manageSubCategoryButton.place_forget()
        titleFont = Font(family="Times New Roman",size=25, weight="bold")
        labelFont = Font(family="Times New Roman",size=15)
        entryFont = Font(family="Times New Roman",size=14)
        buttonFont = Font(family="Times New Roman",size=18)

        titleLabel = Label(self.frame3, bg='gray', text ='Add Sub-Category', font=titleFont)
        titleLabel.place(x=30, y=10)
        
        frame1 = Frame(self.frame3)
        frame1.place(x=30, y=200, width=950, height=300)

        boxLabel = Label(frame1, relief='solid')
        boxLabel.place(x=0, y=0, width=950, height=300)

        boxTitleLabel = Label(frame1, text ='Add Sub-Category', font=labelFont, relief=SOLID, anchor=W)
        boxTitleLabel.place(x=0, y=0, width=950, height=30)

        addCategoryLabel = Label(frame1, text ='Category Name :', font=labelFont, anchor=E)
        addCategoryLabel.place(x=47, y=50)

        default=StringVar(value='--select--')
        addCategoryComboBox = ttk.Combobox(frame1, width=50,state="readonly")
        addCategoryComboBox["values"]=catList
        addCategoryComboBox.set("Select")
        addCategoryComboBox.place(x=195, y=50)

        addSubCategoryLabel = Label(frame1, text ='Sub-Category Name :', font=labelFont, anchor=W)
        addSubCategoryLabel.place(x=10, y=100)

        addSubCategoryEntry = Entry(frame1, font=entryFont)
        addSubCategoryEntry.place(x=195, y=100)

        statusLabel = Label(frame1, text ='Status :', font=labelFont, anchor=E)
        statusLabel.place(x=122, y=150)

        status=StringVar()
        status.set("Inactive")
        statusCheckButton = Checkbutton(frame1,variable=status,  textvariable=status,font=entryFont, height=1,offvalue = 'Inactive',
                          onvalue = 'Active')
        statusCheckButton.place(x=192, y=150)

        addSubCategoryButton = Button(frame1, text ='Add Sub-Category', font=buttonFont)
        addSubCategoryButton.place(x=47, y=225)
        addSubCategoryButton.config(command=lambda:[Backend__Admin.AddSubCategory(status.get(), addCategoryComboBox.get(),addSubCategoryEntry.get()),statusCheckButton.deselect(),addCategoryComboBox.set("Select"),addSubCategoryEntry.delete(0,END)])
        return
    
    def manageSubCategoryButton(self):
        self.addSubCategoryButton.place_forget()
        self.manageSubCategoryButton.place_forget()
        Backend__Admin.manageSubCategory(self)
        return

    def manageSubCategoryButtonFront(self):
                def recursion():
                    Backend__Admin.manageSubCategory(self)
                    self.manageSubCategoryButtonFront()
                self.addCategoryButton.place_forget()
                self.manageCategoryButton.place_forget()
                for widgets in self.frame3.winfo_children():
                    widgets.destroy()
                
                titleFont = Font(family="Times New Roman",size=25, weight="bold")
                labelFont = Font(family="Times New Roman",size=20)
                entryFont = Font(family="Times New Roman",size=14)
                buttonFont = Font(family="Times New Roman",size=18)

                frame3 = Frame(self.frame3, bg='#1c748c')
                frame3.place(x=0, y=0, height = 685, width= 1240)
                
                titleLabel = Label(frame3, bg='gray', text ='Manage Category', font=titleFont)
                titleLabel.place(x=30, y=10)

                Mainframe = Frame(frame3)
                Mainframe.place(x=10, y=100, width=1170, height=570)
                Mainframe1=Frame(Mainframe)
                
                
                myCanvas=Canvas(Mainframe1,width=1150,height=450)
                myScrollBar=ttk.Scrollbar(Mainframe1,orient=VERTICAL,command=myCanvas.yview)

                scrollFrame=Frame(myCanvas)
                scrollFrame.bind("<Configure>", lambda e:  myCanvas.configure(scrollregion=myCanvas.bbox("all")))

                myCanvas.create_window((0,0),window=scrollFrame, anchor=NW)
                myCanvas.configure(yscrollcommand=myScrollBar.set)
                

                boxLabel = Label(Mainframe, relief='solid')
                #boxLabel.place(x=0, y=0, width=1170, height=570)


                boxTitleLabel = Label(Mainframe, text ='Manage Category', font=labelFont, relief=SOLID, anchor=W)
                boxTitleLabel.place(x=0, y=0, width=1170, height=35)

                srLabel =Label(Mainframe, font=labelFont, text="Sr.No." , anchor=CENTER,relief="solid")
                srLabel.place(x=0, y=35,width=100)
                categoryNameLabel=Label(Mainframe,font=labelFont, text="Category Name", anchor=CENTER,relief="solid",width=25)
                categoryNameLabel.place(x=100, y=35,width=300)

                subcategoryNameLabel=Label(Mainframe,font=labelFont, text="Sub-Category Name", anchor=CENTER,relief="solid",width=25)
                subcategoryNameLabel.place(x=400, y=35,width=300)

                statusLabel=Label(Mainframe,font=labelFont, text="Sub-Category Status", anchor=CENTER,relief="solid",width=25)
                statusLabel.place(x=700, y=35, width=300)

                actionLabel=Label(Mainframe,text='Action',font=labelFont,relief=SOLID,width=14)
                actionLabel.place(x=1000,y=35,width=150)

                
                sr=1
                global pos
                records=Backend__Admin.records
                yval=50
                for i in records:
                    if i[2]==1:
                        text="Active"
                    else: text="Inactive"
                    rowsrLabel=Label(scrollFrame, font=entryFont, text=sr, anchor=CENTER,relief=SOLID, width=9)
                    rowsrLabel.grid(row=sr,column=0)
                    

                    rowCatNameLabel=Label(scrollFrame, font=entryFont, text=(i[1]),relief=SOLID,width=29)
                    rowCatNameLabel.grid(row=sr,column=1)
                    #rowCatNameLabel.place(x=150,y=yval)

                    rowsubCatNameLabel=Label(scrollFrame, font=entryFont, text=(i[0]),relief=SOLID,width=30)
                    rowsubCatNameLabel.grid(row=sr,column=2)

                    rowStatusLabel=Label(scrollFrame, font=entryFont, text=text,relief=SOLID,width=29)
                    rowStatusLabel.grid(row=sr,column=3)

                    rowEditButton=Button(scrollFrame, font=entryFont, text=("Edit"), anchor=CENTER ,relief=SOLID,width=7,height=0,command=lambda i=i: self.updateSubCategory(i[0],i[1]))
                    rowEditButton.grid(row=sr,column=4)

                    rowDeleteButton=Button(scrollFrame, font=entryFont, text=("Delete"), anchor=CENTER ,relief=SOLID,width=7,height=0,command=lambda i=i:[ Backend__Admin.deleteSubCategory(i[0]),recursion()])
                    rowDeleteButton.grid(row=sr,column=5)
                    sr=sr+1
                    yval=yval+30       
                Mainframe1.place(x=0,y=75)
                myCanvas.pack(side="left",fill="both",expand=True)
                myScrollBar.pack(side="right",fill="y")
 
    def updateSubCategory(self, subCatName,catName):
        for widgets in self.frame3.winfo_children():
            widgets.destroy()
        def recursion():
            Backend__Admin.manageSubCategory()
            self.manageSubCategoryButtonFront()
        conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="")
        if conn.is_connected():
            print("Database Connected")
            global catList
            sql="SELECT category FROM category_subcategory  "     
            Cursor=conn.cursor()
            Cursor.execute(sql)
            catList=Cursor.fetchall()
            list1=[]
            for i in catList:
                print(i[0])
                inp=i[0]
                list1.append(inp)
            catList=list1
        subCatOld=subCatName
        titleFont = Font(family="Times New Roman",size=25, weight="bold")
        labelFont = Font(family="Times New Roman",size=15)
        entryFont = Font(family="Times New Roman",size=14)
        buttonFont = Font(family="Times New Roman",size=18)

        
        titleLabel = Label(self.frame3, bg='gray', text ='Update Sub-Category', font=titleFont)
        titleLabel.place(x=30, y=10)

        frame1 = Frame(self.frame3)
        frame1.place(x=30, y=200, width=950, height=300)

        boxLabel = Label(frame1, relief='solid')
        boxLabel.place(x=0, y=0, width=950, height=300)

        boxTitleLabel = Label(frame1, text ='Update Sub-Category', font=labelFont, relief=SOLID, anchor=W)
        boxTitleLabel.place(x=0, y=0, width=950, height=30)

        addCategoryLabel = Label(frame1, text ='Category Name :', font=labelFont, anchor=E)
        addCategoryLabel.place(x=47, y=50)

        addCategoryComboBox = ttk.Combobox(frame1, width=50,state="readonly")
        addCategoryComboBox["values"]=catList
        addCategoryComboBox.set(catName)
        addCategoryComboBox.place(x=195, y=50)

        SubCategoryLabel = Label(frame1, text ='Sub-Category Name :', font=labelFont, anchor=E)
        SubCategoryLabel.place(x=10, y=100)

        SubCategoryEntry = Entry(frame1, font=entryFont)
        SubCategoryEntry.insert("1", subCatName)
        SubCategoryEntry.place(x=195, y=100)

        statusLabel = Label(frame1, text ='Status :', font=labelFont, anchor=E)
        statusLabel.place(x=122, y=150)

        status =tkinter.StringVar()
        status.set("Inactive")
        statusCheckButton = Checkbutton(frame1,variable=status,  textvariable=status,font=entryFont, height=1,offvalue = 'Inactive',
                          onvalue = 'Active')
        statusCheckButton.place(x=192, y=150)

        updateSubCategoryButton = Button(frame1, text ='Update Sub-Category', font=buttonFont, command=lambda:[Backend__Admin.updateSubCategory(SubCategoryEntry.get(),addCategoryComboBox.get(),status.get(),subCatOld),recursion()])
        updateSubCategoryButton.place(x=47, y=225)
        return


    def addbrandButton(self):
        for widgets in self.frame3.winfo_children():
            widgets.destroy()
        self.addbrandButton.place_forget()
        self.managebrandButton.place_forget()
        conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="")
        if conn.is_connected():
            print("Database Connected")
            global catList
            sql="SELECT category FROM category_subcategory"     
            Cursor=conn.cursor()
            Cursor.execute(sql)
            catList=Cursor.fetchall()
            list1=[]
            for i in catList:
                print(i[0])
                inp=i[0]
                list1.append(inp)
            catList=list1
            sql="SELECT subCatName FROM subcategory"
            Cursor.execute(sql)
            subcatList=Cursor.fetchall()
            list2=[]
            for i in subcatList:
                print(i[0])
                inp=i[0]
                list2.append(inp)
            subcatList=list2
        titleFont = Font(family="Times New Roman",size=25, weight="bold")
        labelFont = Font(family="Times New Roman",size=15)
        entryFont = Font(family="Times New Roman",size=14)
        buttonFont = Font(family="Times New Roman",size=18)

        
        titleLabel = Label(self.frame3, bg='gray', text ='Add Brand', font=titleFont)
        titleLabel.place(x=30, y=10)

        frame = Frame(self.frame3)
        frame.place(x=30, y=200, width=950, height=300)

        boxLabel = Label(frame, relief='solid')
        boxLabel.place(x=0, y=0, width=950, height=300)

        boxTitleLabel = Label(frame, text ='Add Brand', font=labelFont, relief=SOLID, anchor=W)
        boxTitleLabel.place(x=0, y=0, width=950, height=30)

        addCategoryLabel = Label(frame, text ='Category Name :', font=labelFont, anchor=E)
        addCategoryLabel.place(x=47, y=50)

        default=StringVar(value='--Select--')
        addCategoryComboBox = ttk.Combobox(frame, width=50,state="readonly")
        addCategoryComboBox["values"]=catList
        addCategoryComboBox.set("Select")
        addCategoryComboBox.place(x=195, y=50)

        SubCategoryLabel = Label(frame, text ='Sub-Category Name :', font=labelFont, anchor=E)
        SubCategoryLabel.place(x=10, y=100)

        default=StringVar(value='--Select--')
        SubCategoryEntry = ttk.Combobox(frame, width=50,state="readonly")
        SubCategoryEntry["values"]=subcatList
        SubCategoryEntry.set("Select")
        SubCategoryEntry.place(x=195, y=100)

        statusLabel = Label(frame, text ='Status :', font=labelFont, anchor=E)
        statusLabel.place(x=122, y=200)

        status =tkinter.StringVar()
        status.set("Inactive")
        statusCheckButton = Checkbutton(frame,variable=status,  textvariable=status,font=entryFont, height=1,offvalue = 'Inactive',
                          onvalue = 'Active')
        statusCheckButton.place(x=192, y=200)


        addBrandLabel = Label(frame, text ='Brand Name :', font=labelFont, anchor=E)
        addBrandLabel.place(x=71, y=150)

        addBrandEntry = Entry(frame, font=entryFont)
        addBrandEntry.place(x=195, y=150)

        

        addBrandButton = Button(frame, text ='Add Brand', font=buttonFont,command=lambda: [Backend__Admin.addBrand(status.get(), addCategoryComboBox.get(),SubCategoryEntry.get(),addBrandEntry.get()),statusCheckButton.deselect(),addCategoryComboBox.set("Select"),SubCategoryEntry.set("Select"),addBrandEntry.delete(0,END)])
        addBrandButton.place(x=65, y=235)
        return

    def managebrandButton(self):
        self.addSubCategoryButton.place_forget()
        self.manageSubCategoryButton.place_forget()
        Backend__Admin.manageBrand(self)
        return
    
    def manageBrandButtonFront(self):
                def recursion():
                    Backend__Admin.manageBrand(self)
                    self.manageBrandButtonFront()
                self.addbrandButton.place_forget()
                self.managebrandButton.place_forget()
                for widgets in self.frame3.winfo_children():
                    widgets.destroy()
                
                titleFont = Font(family="Times New Roman",size=25, weight="bold")
                labelFont = Font(family="Times New Roman",size=20)
                entryFont = Font(family="Times New Roman",size=14)
                buttonFont = Font(family="Times New Roman",size=18)

                frame3 = Frame(self.frame3, bg='#1c748c')
                frame3.place(x=0, y=0, height = 685, width= 1240)
                
                titleLabel = Label(frame3, bg='gray', text ='Manage Brand', font=titleFont)
                titleLabel.place(x=30, y=10)

                Mainframe = Frame(frame3)
                Mainframe.place(x=10, y=100, width=1170, height=570)
                Mainframe1=Frame(Mainframe)
                
                
                myCanvas=Canvas(Mainframe1,width=1150,height=450)
                myScrollBar=ttk.Scrollbar(Mainframe1,orient=VERTICAL,command=myCanvas.yview)

                scrollFrame=Frame(myCanvas)
                scrollFrame.bind("<Configure>", lambda e:  myCanvas.configure(scrollregion=myCanvas.bbox("all")))

                myCanvas.create_window((0,0),window=scrollFrame, anchor=NW)
                myCanvas.configure(yscrollcommand=myScrollBar.set)
                

                boxLabel = Label(Mainframe, relief='solid')
                #boxLabel.place(x=0, y=0, width=1170, height=570)


                boxTitleLabel = Label(Mainframe, text ='Manage Brand', font=labelFont, relief=SOLID, anchor=W)
                boxTitleLabel.place(x=0, y=0, width=1170, height=35)

                srLabel =Label(Mainframe, font=labelFont, text="Sr.No." , anchor=CENTER,relief="solid")
                srLabel.place(x=0, y=35,width=100)
                categoryNameLabel=Label(Mainframe,font=labelFont, text="Category Name", anchor=CENTER,relief="solid",width=25)
                categoryNameLabel.place(x=100, y=35,width=225)

                subcategoryNameLabel=Label(Mainframe,font=labelFont, text="Sub-Category Name", anchor=CENTER,relief="solid",width=25)
                subcategoryNameLabel.place(x=325, y=35,width=225)

                brandLabel=Label(Mainframe,font=labelFont, text="Brand Name", anchor=CENTER,relief="solid",width=25)
                brandLabel.place(x=550, y=35,width=225)

                statusLabel=Label(Mainframe,font=labelFont, text="Brand Status", anchor=CENTER,relief="solid",width=25)
                statusLabel.place(x=775, y=35, width=225)
                

                actionLabel=Label(Mainframe,text='Action',font=labelFont,relief=SOLID,width=14)
                actionLabel.place(x=1000,y=35,width=150)

                
                sr=1
                global pos
                records=Backend__Admin.records
                yval=50
                for i in records:
                    if i[3]==1:
                        text="Active"
                    else: 
                        text="Inactive"
                    print(text)
                    rowsrLabel=Label(scrollFrame, font=entryFont, text=sr, anchor=CENTER,relief=SOLID, width=9)
                    rowsrLabel.grid(row=sr,column=0)                 

                    rowCatNameLabel=Label(scrollFrame, font=entryFont, text=(i[2]),relief=SOLID,width=22)
                    rowCatNameLabel.grid(row=sr,column=1)
                    #rowCatNameLabel.place(x=150,y=yval)

                    rowsubCatNameLabel=Label(scrollFrame, font=entryFont, text=(i[1]),relief=SOLID,width=22)
                    rowsubCatNameLabel.grid(row=sr,column=2)

                    rowBrandNameLabel=Label(scrollFrame, font=entryFont, text=(i[0]),relief=SOLID,width=22)
                    rowBrandNameLabel.grid(row=sr,column=3)

                    rowStatusLabel=Label(scrollFrame, font=entryFont, text=text,relief=SOLID,width=22)
                    rowStatusLabel.grid(row=sr,column=4)

                    rowEditButton=Button(scrollFrame, font=entryFont, text=("Edit"), anchor=CENTER ,relief=SOLID,width=7,height=0,command=lambda i=i: self.updateBrandButton(i[0],i[1],i[2],i[3]))
                    rowEditButton.grid(row=sr,column=5)

                    rowDeleteButton=Button(scrollFrame, font=entryFont, text=("Delete"), anchor=CENTER ,relief=SOLID,width=6,height=0,command=lambda i=i:[ Backend__Admin.deleteBrand(i[0]),recursion()])
                    rowDeleteButton.grid(row=sr,column=6)
                    sr=sr+1
                    yval=yval+30       
                Mainframe1.place(x=0,y=75)
                myCanvas.pack(side="left",fill="both",expand=True)
                myScrollBar.pack(side="right",fill="y")      
        
    def updateBrandButton(self,brandName,subCatName,catName,status):
        for widgets in self.frame3.winfo_children():
            widgets.destroy()
        def recursion():
            Backend__Admin.manageSubCategory()
            self.manageSubCategoryButtonFront()
        conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="")
        if conn.is_connected():
            print("Database Connected")
            global catList
            sql="SELECT category FROM category_subcategory  "     
            Cursor=conn.cursor()
            Cursor.execute(sql)
            catList=Cursor.fetchall()
            list1=[]
            for i in catList:
                print(i[0])
                inp=i[0]
                list1.append(inp)
            catList=list1
            

            sql="SELECT subCatName FROM subcategory  "
            Cursor.execute(sql)
            subCatList=Cursor.fetchall() 
            list2=[]
            for i in subCatList:
                print(i[0])
                inp=i[0]
                list2.append(inp)
            subCatList=list2

        brandOld=brandName
        titleFont = Font(family="Times New Roman",size=25, weight="bold")
        labelFont = Font(family="Times New Roman",size=15)
        entryFont = Font(family="Times New Roman",size=14)
        buttonFont = Font(family="Times New Roman",size=18)

        
        titleLabel = Label(self.frame3, bg='gray', text ='Update Brand', font=titleFont)
        titleLabel.place(x=30, y=10)

        frame1 = Frame(self.frame3)
        frame1.place(x=30, y=200, width=950, height=300)

        boxLabel = Label(frame1, relief='solid')
        boxLabel.place(x=0, y=0, width=950, height=300)

        boxTitleLabel = Label(frame1, text ='Update Brand', font=labelFont, relief=SOLID, anchor=W)
        boxTitleLabel.place(x=0, y=0, width=950, height=30)

        addCategoryLabel = Label(frame1, text ='Category Name :', font=labelFont, anchor=E)
        addCategoryLabel.place(x=47, y=50)

        addCategoryComboBox = ttk.Combobox(frame1, width=50,state="readonly")
        addCategoryComboBox["values"]=catList
        addCategoryComboBox.set(catName)
        addCategoryComboBox.place(x=195, y=50)

        
        SubCategoryLabel = Label(frame1, text ='Sub-Category Name :', font=labelFont, anchor=E)
        SubCategoryLabel.place(x=10, y=100)

        SubCategoryComboBox = ttk.Combobox(frame1, width=50,state="readonly")
        SubCategoryComboBox["values"]=subCatList
        SubCategoryComboBox.set(subCatName)
        SubCategoryComboBox.place(x=195, y=100)

        brandLabel = Label(frame1, text ='Brand Name :', font=labelFont, anchor=E)
        brandLabel.place(x=67, y=150)

        brandNameEntry = Entry(frame1, font=entryFont)
        brandNameEntry.insert("1", brandName)
        brandNameEntry.place(x=195, y=150)

        statusLabel = Label(frame1, text ='Status :', font=labelFont, anchor=E)
        statusLabel.place(x=122, y=200)

        status =tkinter.StringVar()
        status.set("Inactive")
        statusCheckButton = Checkbutton(frame1,variable=status,  textvariable=status,font=entryFont, height=1,offvalue = 'Inactive',
                          onvalue = 'Active')
        statusCheckButton.place(x=192, y=200)

        updateBrandButton = Button(frame1, text ='Update Brand', font=buttonFont, command=lambda:Backend__Admin.updateBrand(brandNameEntry.get(),SubCategoryComboBox.get(),addCategoryComboBox.get(),status.get(),brandOld))
        updateBrandButton.place(x=47, y=235)
        return



    def addproductButton(self):
        for widgets in self.frame3.winfo_children():
            widgets.destroy()
        self.addproductButton.place_forget()
        self.manageproductButton.place_forget()
        conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="")
        if conn.is_connected():
            print("Database Connected")
            global catList
            sql="SELECT category FROM category_subcategory"     
            Cursor=conn.cursor()
            Cursor.execute(sql)
            catList=Cursor.fetchall()
            list1=[]
            for i in catList:
                print(i[0])
                inp=i[0]
                list1.append(inp)
            catList=list1
            
            sql="SELECT subCatName FROM subcategory"
            Cursor.execute(sql)
            subcatList=Cursor.fetchall()
            list2=[]
            for i in subcatList:
                print(i[0])
                inp=i[0]
                list2.append(inp)
            subcatList=list2
            sql="SELECT BrandName FROM brand"
            Cursor.execute(sql)
            brandList=Cursor.fetchall()
            list3=[]
            for i in brandList:
                print(i[0])
                inp=i[0]
                list3.append(inp)
            brandList=list3
        titleFont = Font(family="Times New Roman",size=25, weight="bold")
        labelFont = Font(family="Times New Roman",size=15)
        entryFont = Font(family="Times New Roman",size=14)
        buttonFont = Font(family="Times New Roman",size=18)

        
        titleLabel = Label(self.frame3, bg='gray', text ='Add Product', font=titleFont)
        titleLabel.place(x=30, y=10)

        frame = Frame(self.frame3,bg='yellow')
        frame.place(x=30, y=75, width=950, height=500)

        boxLabel = Label(frame, relief='solid')
        boxLabel.place(x=0, y=0, width=950, height=500)

        boxTitleLabel = Label(frame, text ='Add Product', font=labelFont, relief=SOLID, anchor=W)
        boxTitleLabel.place(x=0, y=0, width=950, height=30)

        ProductLabel = Label(frame, text ='Product Name :', font=labelFont, anchor=E)
        ProductLabel.place(x=70, y=50)
        ProductEntry = Entry(frame, font=entryFont)
        ProductEntry.place(x=250, y=50)

        categoryLabel = Label(frame, text ='Category Name :', font=labelFont, anchor=W)
        categoryLabel.place(x=60, y=100)
        categoryCombobox = ttk.Combobox(frame, font=entryFont, height=1,state="readonly")
        categoryCombobox["values"]=catList
        categoryCombobox.set("Select")
        categoryCombobox.place(x=250, y=100,width=200)

        subCategoryLabel = Label(frame, text ='Sub-Category Name :', font=labelFont, anchor=W)
        subCategoryLabel.place(x=24, y=150)
        subCategoryComboBox = ttk.Combobox(frame, font=entryFont, height=1,state="readonly")
        subCategoryComboBox["values"]=subcatList
        subCategoryComboBox.set("Select")
        subCategoryComboBox.place(x=250, y=150)

        brandLabel = Label(frame, text ='Brand Name :', font=labelFont, anchor=W)
        brandLabel.place(x=84, y=200)
        brandComboBox = ttk.Combobox(frame, font=entryFont, height=1,state="readonly")
        brandComboBox["values"]=brandList
        brandComboBox.set("Select")
        brandComboBox.place(x=250, y=200)

        stockLabel = Label(frame, text ='Stocks Quantity :', font=labelFont, anchor=E)
        stockLabel.place(x=75, y=250)
        stockEntry = Entry(frame, font=entryFont)
        stockEntry.place(x=250, y=250)

        thresholdLabel = Label(frame, text ='Threshold :', font=labelFont, anchor=E)
        thresholdLabel.place(x=110, y=300)
        thresholdEntry = Entry(frame, font=entryFont)
        thresholdEntry.place(x=250, y=300)

        priceLabel = Label(frame, text ='Price :', font=labelFont, anchor=E)
        priceLabel.place(x=142, y=350)
        priceEntry = Entry(frame, font=entryFont)
        priceEntry.place(x=250, y=350)

        statusLabel = Label(frame, text ='Status :', font=labelFont, anchor=E)
        statusLabel.place(x=137, y=400)
        status =tkinter.StringVar()
        status.set("Inactive")
        statusCheckButton = Checkbutton(frame,variable=status,  textvariable=status,font=entryFont, height=1,offvalue = 'Inactive',
                          onvalue = 'Active')
        statusCheckButton.place(x=260, y=400)

        addProductButton = Button(frame, text ='Add Product', font=buttonFont, command= lambda: [Backend__Admin.addProduct(ProductEntry.get(),categoryCombobox.get(),subCategoryComboBox.get(),brandComboBox.get(),priceEntry.get(),thresholdEntry.get(),stockEntry.get(),status.get()),ProductEntry.delete(0,END),categoryCombobox.set("Select"),subCategoryComboBox.set("Select"),brandComboBox.set("Select"),priceEntry.delete(0,END),thresholdEntry.delete(0,END),stockEntry.delete(0,END),statusCheckButton.deselect(),status.set("Inactive")])
        addProductButton.place(x=65, y=450)
        return
        
    def manageproductButton(self):
        self.addproductButton.place_forget()
        self.manageproductButton.place_forget()
        Backend__Admin.manageProduct(self)
        return

    def manageProductButtonFront(self):
                def recursion():
                    Backend__Admin.manageProduct(self)
                    self.manageProductButtonFront()
                self.addbrandButton.place_forget()
                self.managebrandButton.place_forget()
                for widgets in self.frame3.winfo_children():
                    widgets.destroy()
                
                titleFont = Font(family="Times New Roman",size=25, weight="bold")
                labelFont = Font(family="Times New Roman",size=15)
                entryFont = Font(family="Times New Roman",size=10)
                buttonFont = Font(family="Times New Roman",size=18)

                frame3 = Frame(self.frame3, bg='#1c748c')
                frame3.place(x=0, y=0, height = 685, width= 1240)
                
                titleLabel = Label(frame3, bg='gray', text ='Manage Product', font=titleFont)
                titleLabel.place(x=30, y=10)

                Mainframe = Frame(frame3)
                Mainframe.place(x=10, y=100, width=1170, height=570)
                Mainframe1=Frame(Mainframe)
                
                
                myCanvas=Canvas(Mainframe1,width=1150,height=450)
                myScrollBar=ttk.Scrollbar(Mainframe1,orient=VERTICAL,command=myCanvas.yview)

                scrollFrame=Frame(myCanvas)
                scrollFrame.bind("<Configure>", lambda e:  myCanvas.configure(scrollregion=myCanvas.bbox("all")))

                myCanvas.create_window((0,0),window=scrollFrame, anchor=NW)
                myCanvas.configure(yscrollcommand=myScrollBar.set)
                

                boxLabel = Label(Mainframe, relief='solid')
                #boxLabel.place(x=0, y=0, width=1170, height=570)


                boxTitleLabel = Label(Mainframe, text ='Manage Product', font=labelFont, relief=SOLID, anchor=W)
                boxTitleLabel.place(x=0, y=0, width=1170, height=35)

                srLabel =Label(Mainframe, font=labelFont, text="Sr.No." , anchor=CENTER,relief="solid")
                srLabel.place(x=0, y=35,width=57)

                productIDLabel =Label(Mainframe, font=labelFont, text="ID" , anchor=CENTER,relief="solid")
                #productIDLabel.place(x=50, y=35,width=165)

                ProductNameLabel =Label(Mainframe, font=labelFont, text="Name" , anchor=CENTER,relief="solid")
                ProductNameLabel.place(x=57 , y=35,width=125)             

                categoryNameLabel=Label(Mainframe,font=labelFont, text="Category", anchor=CENTER,relief="solid",width=25)
                categoryNameLabel.place(x=182, y=35,width=170)

                subcategoryNameLabel=Label(Mainframe,font=labelFont, text="Sub-Category", anchor=CENTER,relief="solid",width=25)
                subcategoryNameLabel.place(x=352, y=35,width=132)

                brandLabel=Label(Mainframe,font=labelFont, text="Brand", anchor=CENTER,relief="solid",width=25)
                brandLabel.place(x=484, y=35,width=110)
 
                priceLabel=Label(Mainframe,font=labelFont, text="Price", anchor=CENTER,relief="solid",width=25)
                priceLabel.place(x=594, y=35,width=110)

                thresholdLabel=Label(Mainframe,font=labelFont, text="Threshold", anchor=CENTER,relief="solid",width=25)
                thresholdLabel.place(x=704, y=35,width=110)

                quantityLabel=Label(Mainframe,font=labelFont, text="Quantity", anchor=CENTER,relief="solid",width=25)
                quantityLabel.place(x=814, y=35,width=110)


                statusLabel=Label(Mainframe,font=labelFont, text="Status", anchor=CENTER,relief="solid",width=25)
                statusLabel.place(x=924, y=35, width=100)
                

                actionLabel=Label(Mainframe,text='Action',font=labelFont,relief=SOLID,width=14)
                actionLabel.place(x=1024,y=35,width=126)

                
                sr=1
                global pos
                records=Backend__Admin.records
                yval=50
                for i in records:
                    print(i[7])
                    if i[8]==1:
                        text="Active"
                    else: 
                        text="tive"
                    print(text)
                    rowsrLabel=Label(scrollFrame, font=entryFont, text=sr, anchor=CENTER,relief=SOLID, width=7)
                    rowsrLabel.grid(row=sr,column=0)   

                    rowproductIDLabel=Label(scrollFrame, font=entryFont, text=i[0],anchor=W, relief=SOLID, width=22)
                    #rowproductIDLabel.grid(row=sr,column=1)              

                    rowProductNameLabel=Label(scrollFrame, font=entryFont, text=(i[1]),relief=SOLID,width=16)
                    rowProductNameLabel.grid(row=sr,column=2)
                    #rowCatNameLabel.place(x=150,y=yval)

                    rowCatNameLabel=Label(scrollFrame, font=entryFont, text=(i[2]),relief=SOLID,width=25)
                    rowCatNameLabel.grid(row=sr,column=3)

                    rowsubCatNameLabel=Label(scrollFrame, font=entryFont, text=(i[3]),relief=SOLID,width=18)
                    rowsubCatNameLabel.grid(row=sr,column=4)

                    rowBrandNameLabel=Label(scrollFrame, font=entryFont, text=i[4],relief=SOLID,width=15)
                    rowBrandNameLabel.grid(row=sr,column=5)

                    rowPriceLabel=Label(scrollFrame, font=entryFont, text=i[5],relief=SOLID,width=15)
                    rowPriceLabel.grid(row=sr,column=6)

                    rowThresholdLabel=Label(scrollFrame, font=entryFont, text=i[6],relief=SOLID,width=15)
                    rowThresholdLabel.grid(row=sr,column=7)

                    rowQuantityLabel=Label(scrollFrame, font=entryFont, text=i[7],relief=SOLID,width=15)
                    rowQuantityLabel.grid(row=sr,column=8)

                    rowStatusLabel=Label(scrollFrame, font=entryFont, text=text,relief=SOLID,width=13)
                    rowStatusLabel.grid(row=sr,column=9)

                    rowEditButton=Button(scrollFrame, font=entryFont, text=("Edit"), anchor=CENTER ,relief=SOLID,width=8,height=0,command=lambda i=i: self.updateProductButton(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]))
                    rowEditButton.grid(row=sr,column=10)

                    rowDeleteButton=Button(scrollFrame, font=entryFont, text=("Delete"), anchor=CENTER ,relief=SOLID,width=7,height=0,command=lambda i=i:[ Backend__Admin.deleteProduct(i[0]),recursion()])
                    rowDeleteButton.grid(row=sr,column=11)
                    sr=sr+1
                    yval=yval+30       
                Mainframe1.place(x=0,y=75)
                myCanvas.pack(side="left",fill="both",expand=True)
                myScrollBar.pack(side="right",fill="y")      

    def updateProductButton(self,prodID,prodName,prodCat,prodSubCat, prodBrand,prodPrice,prodThreshold,prodQuantity,prodStatus):
        for widgets in self.frame3.winfo_children():
            widgets.destroy()
        self.addproductButton.place_forget()
        self.manageproductButton.place_forget()
        conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="")
        if conn.is_connected():
            print("Database Connected")
            global catList
            sql="SELECT category FROM category_subcategory"     
            Cursor=conn.cursor()
            Cursor.execute(sql)
            catList=Cursor.fetchall()
            list1=[]
            for i in catList:
                print(i[0])
                inp=i[0]
                list1.append(inp)
            catList=list1

            sql="SELECT subCatName FROM subcategory"
            Cursor.execute(sql)
            subcatList=Cursor.fetchall()
            list2=[]
            for i in subcatList:
                print(i[0])
                inp=i[0]
                list2.append(inp)
            subcatList=list2

            sql="SELECT BrandName FROM brand"
            Cursor.execute(sql)
            brandList=Cursor.fetchall()
            list3=[]
            for i in brandList:
                print(i[0])
                inp=i[0]
                list3.append(inp)
        titleFont = Font(family="Times New Roman",size=25, weight="bold")
        labelFont = Font(family="Times New Roman",size=15)
        entryFont = Font(family="Times New Roman",size=14)
        buttonFont = Font(family="Times New Roman",size=18)

        
        titleLabel = Label(self.frame3, bg='gray', text ='Update Product', font=titleFont)
        titleLabel.place(x=30, y=10)

        frame = Frame(self.frame3,bg='yellow')
        frame.place(x=30, y=75, width=950, height=500)

        boxLabel = Label(frame, relief='solid')
        boxLabel.place(x=0, y=0, width=950, height=500)

        boxTitleLabel = Label(frame, text ='Update Product', font=labelFont, relief=SOLID, anchor=W)
        boxTitleLabel.place(x=0, y=0, width=950, height=30)

        productIDLabel = Label(frame, text=prodID,font=entryFont)
        #productIDLabel.place(x=450, y=50)

        ProductLabel = Label(frame, text ='Product Name :', font=labelFont, anchor=E)
        ProductLabel.place(x=70, y=50)
        ProductEntry = Entry(frame, font=entryFont)
        ProductEntry.insert(1,prodName)
        ProductEntry.place(x=250, y=50)

        categoryLabel = Label(frame, text ='Category Name :', font=labelFont, anchor=W)
        categoryLabel.place(x=60, y=100)
        categoryCombobox = ttk.Combobox(frame, font=entryFont, height=1,state="readonly")
        categoryCombobox["values"]=catList
        categoryCombobox.set(prodCat)
        categoryCombobox.place(x=250, y=100,width=200)

        subCategoryLabel = Label(frame, text ='Sub-Category Name :', font=labelFont, anchor=W)
        subCategoryLabel.place(x=24, y=150)
        subCategoryComboBox = ttk.Combobox(frame, font=entryFont,state="readonly")
        subCategoryComboBox["values"]=subcatList
        subCategoryComboBox.set(prodSubCat)
        subCategoryComboBox.place(x=250, y=150)

        brandLabel = Label(frame, text ='Brand Name :', font=labelFont, anchor=W)
        brandLabel.place(x=84, y=200)
        brandComboBox = ttk.Combobox(frame, font=entryFont, height=1,state="readonly")
        brandComboBox["values"]=brandList
        brandComboBox.set(prodBrand)
        brandComboBox.place(x=250, y=200)

        stockLabel = Label(frame, text ='Stocks Quantity :', font=labelFont, anchor=E)
        stockLabel.place(x=75, y=250)
        stockEntry = Entry(frame, font=entryFont)
        stockEntry.insert(1,prodQuantity)
        stockEntry.place(x=250, y=250)

        thresholdLabel = Label(frame, text ='Threshold :', font=labelFont, anchor=E)
        thresholdLabel.place(x=110, y=300)
        thresholdEntry = Entry(frame, font=entryFont)
        thresholdEntry.insert(1,prodThreshold)
        thresholdEntry.place(x=250, y=300)

        priceLabel = Label(frame, text ='Price :', font=labelFont, anchor=E)
        priceLabel.place(x=142, y=350)
        priceEntry = Entry(frame, font=entryFont)
        priceEntry.insert(1,prodPrice)
        priceEntry.place(x=250, y=350)

        statusLabel = Label(frame, text ='Status :', font=labelFont, anchor=E)
        statusLabel.place(x=137, y=400)
        status =tkinter.StringVar()
        status.set("Inactive")
        statusCheckButton = Checkbutton(frame,variable=status,  textvariable=status,font=entryFont, height=1,offvalue = 'Inactive',
                          onvalue = 'Active')
        statusCheckButton.place(x=260, y=400)
        
        oldProdID=prodID

        updateProductButton = Button(frame, text ='Update Product', font=buttonFont, command= lambda: Backend__Admin.updateProduct(ProductEntry.get(),categoryCombobox.get(),subCategoryComboBox.get(),brandComboBox.get(),priceEntry.get(),thresholdEntry.get(),stockEntry.get(),status.get(),oldProdID))
        updateProductButton.place(x=65, y=450)
    

    def inventory(self):
        for widgets in self.frame3.winfo_children():
                    widgets.destroy()
                
        titleFont = Font(family="Times New Roman",size=25, weight="bold")
        labelFont = Font(family="Times New Roman",size=15)
        entryFont = Font(family="Times New Roman",size=10)
        buttonFont = Font(family="Times New Roman",size=18)
        frame3 = Frame(self.frame3, bg='#1c748c')
        frame3.place(x=0, y=0, height = 685, width= 1240)
                
        titleLabel = Label(frame3, bg='gray', text ='Inventory', font=titleFont)
        titleLabel.place(x=30, y=10)

        Mainframe = Frame(frame3)
        Mainframe.place(x=10, y=100, width=1170, height=570)
        Mainframe1=Frame(Mainframe)
        myCanvas=Canvas(Mainframe1,width=1150,height=450)
        myScrollBar=ttk.Scrollbar(Mainframe1,orient=VERTICAL,command=myCanvas.yview)

        scrollFrame=Frame(myCanvas)
        scrollFrame.bind("<Configure>", lambda e:  myCanvas.configure(scrollregion=myCanvas.bbox("all")))

        myCanvas.create_window((0,0),window=scrollFrame, anchor=NW)
        myCanvas.configure(yscrollcommand=myScrollBar.set)
                

        boxLabel = Label(Mainframe, relief='solid')
        
        boxTitleLabel = Label(Mainframe, text ='Inventory', font=labelFont, relief=SOLID, anchor=W)
        boxTitleLabel.place(x=0, y=0, width=1170, height=35)

        srLabel =Label(Mainframe, font=labelFont, text="Sr.No." , anchor=CENTER,relief="solid")
        srLabel.place(x=0, y=35,width=57)

        productPicLabel =Label(Mainframe, font=labelFont, text="Picture" , anchor=CENTER,relief="solid")
        productPicLabel.place(x=57, y=35,width=246)

        ProductNameLabel =Label(Mainframe, font=labelFont, text="Name" , anchor=CENTER,relief="solid")
        ProductNameLabel.place(x=303 , y=35,width=125)             

        categoryNameLabel=Label(Mainframe,font=labelFont, text="Category", anchor=CENTER,relief="solid")
        categoryNameLabel.place(x=428, y=35,width=170)

        subcategoryNameLabel=Label(Mainframe,font=labelFont, text="Sub-Category", anchor=CENTER,relief="solid")
        subcategoryNameLabel.place(x=598, y=35,width=132)

        brandLabel=Label(Mainframe,font=labelFont, text="Brand", anchor=CENTER,relief="solid")
        brandLabel.place(x=730, y=35,width=110)
 
        priceLabel=Label(Mainframe,font=labelFont, text="Price", anchor=CENTER,relief="solid")
        priceLabel.place(x=840, y=35,width=110)

        thresholdLabel=Label(Mainframe,font=labelFont, text="Threshold", anchor=CENTER,relief="solid")
        thresholdLabel.place(x=950, y=35,width=110)

        quantityLabel=Label(Mainframe,font=labelFont, text="Quantity", anchor=CENTER,relief="solid")
        quantityLabel.place(x=1060, y=35,width=110)

        records=Backend__Admin.records
        sr=1
        yval=50
        for i in records:
            if i[8]==1:
                text="Active"
            else:
                text="Inactive"
    
            rowsrLabel=Button(scrollFrame, font=entryFont, text=sr, anchor=CENTER,relief=SOLID, width=7,command=lambda i=i: Backend__Admin.addCart(i[0],i[1],i[2],i[3],i[4],i[5],i[7]))
            rowsrLabel.grid(row=sr,column=0)   

            rowproductPicLabel=Label(scrollFrame, font=entryFont, text=i[0],anchor=W, relief=SOLID, width=34)
            rowproductPicLabel.grid(row=sr,column=1)              

            rowProductNameLabel=Label(scrollFrame, font=entryFont, text=(i[1]),relief=SOLID,width=17,anchor=W)
            rowProductNameLabel.grid(row=sr,column=2)
            #rowCatNameLabel.place(x=150,y=yval)

            rowCatNameLabel=Label(scrollFrame, font=entryFont, text=(i[2]),relief=SOLID,width=25)
            rowCatNameLabel.grid(row=sr,column=3)

            rowsubCatNameLabel=Label(scrollFrame, font=entryFont, text=(i[3]),relief=SOLID,width=17)
            rowsubCatNameLabel.grid(row=sr,column=4)

            rowBrandNameLabel=Label(scrollFrame, font=entryFont, text=i[4],relief=SOLID,width=15)
            rowBrandNameLabel.grid(row=sr,column=5)

            rowPriceLabel=Label(scrollFrame, font=entryFont, text=i[5],relief=SOLID,width=15)
            rowPriceLabel.grid(row=sr,column=6)

            rowThresholdLabel=Label(scrollFrame, font=entryFont, text=i[6],relief=SOLID,width=15)
            rowThresholdLabel.grid(row=sr,column=7)

            rowQuantityLabel=Label(scrollFrame, font=entryFont, text=i[7],relief=SOLID,width=15)
            rowQuantityLabel.grid(row=sr,column=8)

            rowStatusLabel=Label(scrollFrame, font=entryFont, text=text,relief=SOLID,width=13)
            rowStatusLabel.grid(row=sr,column=9)

            rowEditButton=Button(scrollFrame, font=entryFont, text=("Edit"), anchor=CENTER ,relief=SOLID,width=8,height=0,command=lambda i=i: self.updateProductButton(i[0]))
            rowEditButton.grid(row=sr,column=10)

            rowDeleteButton=Button(scrollFrame, font=entryFont, text=("Delete"), anchor=CENTER ,relief=SOLID,width=7,height=0,command=lambda i=i:[ Backend__Admin.deleteProduct(i[0])])
            rowDeleteButton.grid(row=sr,column=11)
            sr=sr+1
            yval=yval+30




        
                

        Mainframe1.place(x=0,y=75)
        myCanvas.pack(side="left",fill="both",expand=True)
        myScrollBar.pack(side="right",fill="y")

        return


    def search(self):
        
        titleFont = Font(family="Times New Roman",size=25, weight="bold")
        labelFont = Font(family="Times New Roman",size=15)
        entryFont = Font(family="Times New Roman",size=10)
        buttonFont = Font(family="Times New Roman",size=18)
        frame3 = Frame(self.frame3, bg='#1c748c')
        frame3.place(x=10, y=150, height = 520, width= 1170)

        titleLabel = Label(self.frame3, bg='gray', text ='Search', font=titleFont)
        titleLabel.place(x=30, y=10)

        Mainframe = Frame(frame3)
        Mainframe.place(x=0, y=0, width=1170, height=520)
        Mainframe1=Frame(Mainframe)
        myCanvas=Canvas(Mainframe1,width=1150,height=450)
        myScrollBar=ttk.Scrollbar(Mainframe1,orient=VERTICAL,command=myCanvas.yview)

        scrollFrame=Frame(myCanvas)
        scrollFrame.bind("<Configure>",lambda e : myCanvas.configure(scrollregion=myCanvas.bbox("all")))

        myCanvas.create_window((0,0),window=scrollFrame, anchor=NW)
        myCanvas.configure(yscrollcommand=myScrollBar.set)

        boxTitleLabel = Label(Mainframe, text ='Search Results', font=labelFont, relief=SOLID, anchor=W)
        boxTitleLabel.place(x=0, y=0, width=1170, height=35)

        srLabel =Label(Mainframe, font=labelFont, text="Sr.No." , anchor=CENTER,relief="solid")
        srLabel.place(x=0, y=35,width=57)

        productPicLabel =Label(Mainframe, font=labelFont, text="Picture" , anchor=CENTER,relief="solid")
        productPicLabel.place(x=57, y=35,width=246)

        ProductNameLabel =Label(Mainframe, font=labelFont, text="Name" , anchor=CENTER,relief="solid")
        ProductNameLabel.place(x=303 , y=35,width=125)             

        categoryNameLabel=Label(Mainframe,font=labelFont, text="Category", anchor=CENTER,relief="solid")
        categoryNameLabel.place(x=428, y=35,width=170)

        subcategoryNameLabel=Label(Mainframe,font=labelFont, text="Sub-Category", anchor=CENTER,relief="solid")
        subcategoryNameLabel.place(x=598, y=35,width=132)

        brandLabel=Label(Mainframe,font=labelFont, text="Brand", anchor=CENTER,relief="solid")
        brandLabel.place(x=730, y=35,width=110)
 
        priceLabel=Label(Mainframe,font=labelFont, text="Price", anchor=CENTER,relief="solid")
        priceLabel.place(x=840, y=35,width=110)

        thresholdLabel=Label(Mainframe,font=labelFont, text="Threshold", anchor=CENTER,relief="solid")
        thresholdLabel.place(x=950, y=35,width=110)

        quantityLabel=Label(Mainframe,font=labelFont, text="Quantity", anchor=CENTER,relief="solid")
        quantityLabel.place(x=1060, y=35,width=110)

        records=Backend__Admin.records
        sr=1
        yval=50
        for i in records:
            if i[8]==1:
                text="Active"
            else:
                text="Inactive"

            rowsrLabel=Label(scrollFrame, font=entryFont, text=sr, anchor=CENTER,relief=SOLID, width=7)
            rowsrLabel.grid(row=sr,column=0)   

            rowproductPicLabel=Label(scrollFrame, font=entryFont, text=i[0],anchor=W, relief=SOLID, width=34)
            rowproductPicLabel.grid(row=sr,column=1)              

            rowProductNameLabel=Label(scrollFrame, font=entryFont, text=(i[1]),relief=SOLID,width=17)
            rowProductNameLabel.grid(row=sr,column=2)
            #rowCatNameLabel.place(x=150,y=yval)

            rowCatNameLabel=Label(scrollFrame, font=entryFont, text=(i[2]),relief=SOLID,width=25)
            rowCatNameLabel.grid(row=sr,column=3)

            rowsubCatNameLabel=Label(scrollFrame, font=entryFont, text=(i[3]),relief=SOLID,width=17)
            rowsubCatNameLabel.grid(row=sr,column=4)

            rowBrandNameLabel=Label(scrollFrame, font=entryFont, text=i[4],relief=SOLID,width=15)
            rowBrandNameLabel.grid(row=sr,column=5)

            rowPriceLabel=Label(scrollFrame, font=entryFont, text=i[7],relief=SOLID,width=15)
            rowPriceLabel.grid(row=sr,column=6)

            rowThresholdLabel=Label(scrollFrame, font=entryFont, text=i[5],relief=SOLID,width=15)
            rowThresholdLabel.grid(row=sr,column=7)

            rowQuantityLabel=Label(scrollFrame, font=entryFont, text=i[6],relief=SOLID,width=15)
            rowQuantityLabel.grid(row=sr,column=8)

            rowStatusLabel=Label(scrollFrame, font=entryFont, text=text,relief=SOLID,width=13)
            rowStatusLabel.grid(row=sr,column=9)

            rowEditButton=Button(scrollFrame, font=entryFont, text=("Edit"), anchor=CENTER ,relief=SOLID,width=8,height=0,command=lambda i=i: self.updateProductButton(i[0]))
            rowEditButton.grid(row=sr,column=10)

            rowDeleteButton=Button(scrollFrame, font=entryFont, text=("Delete"), anchor=CENTER ,relief=SOLID,width=7,height=0,command=lambda i=i:[ Backend__Admin.deleteProduct(i[0])])
            rowDeleteButton.grid(row=sr,column=11)
            sr=sr+1
            yval=yval+30




        
                

        Mainframe1.place(x=0,y=75)
        myCanvas.pack(side="left",fill="both",expand=True)
        myScrollBar.pack(side="right",fill="y")
        
        return


    def cart(self,records):
        for widgets in self.frame3.winfo_children():
            widgets.destroy()
        titleFont = Font(family="Times New Roman",size=25, weight="bold")
        labelFont = Font(family="Times New Roman",size=15)
        entryFont = Font(family="Times New Roman",size=14)
        buttonFont = Font(family="Times New Roman",size=18)

        titleLabel = Label(self.frame3, bg='gray', text ='Product Cart', font=titleFont)
        titleLabel.place(x=30, y=10)   

        custNameLabel = Label(self.frame3,text="Customer Name", font=labelFont)         
        custNameLabel.place(x=50,y=100)

        custNameEntry = Entry(self.frame3, font=labelFont)         
        custNameEntry.place(x=200,y=100)

        custContactLabel = Label(self.frame3,text="Customer Contact", font=labelFont)         
        custContactLabel.place(x=35,y=150)

        custContactEntry = Entry(self.frame3, font=labelFont)         
        custContactEntry.place(x=200,y=150)

        var1=IntVar()
        paymentModeLabel=Label(self.frame3,font=labelFont, text="Payment Mode:")
        paymentModeLabel.place(x=35,y=200)
        paymentMode1=Radiobutton(self.frame3,text="Cash",variable=var1,value=1)
        paymentMode1.place(x=200,y=200)
        paymentMode2=Radiobutton(self.frame3,text="Card",variable=var1,value=2)
        paymentMode2.place(x=250,y=200)
        paymentMode1.deselect()
        paymentMode2.deselect()

        srLabel =Label(self.frame3, font=labelFont, text="Sr.No." , anchor=CENTER,relief="solid")
        srLabel.place(x=50, y=250,width=57)

        ProductNameLabel =Label(self.frame3, font=labelFont, text="Name" , anchor=CENTER,relief="solid")
        ProductNameLabel.place(x=107 , y=250,width=150)             

        categoryNameLabel=Label(self.frame3,font=labelFont, text="Category", anchor=CENTER,relief="solid")
        categoryNameLabel.place(x=257, y=250,width=170)

        subcategoryNameLabel=Label(self.frame3,font=labelFont, text="Sub-Category", anchor=CENTER,relief="solid")
        subcategoryNameLabel.place(x=427, y=250,width=132)

        brandLabel=Label(self.frame3,font=labelFont, text="Brand", anchor=CENTER,relief="solid")
        brandLabel.place(x=559, y=250,width=110)
 
        priceLabel=Label(self.frame3,font=labelFont, text="Price", anchor=CENTER,relief="solid")
        priceLabel.place(x=669, y=250,width=110)

        quantityLabel=Label(self.frame3,font=labelFont, text="Quantity", anchor=CENTER,relief="solid")
        quantityLabel.place(x=779, y=250,width=110)

        totalLabel=Label(self.frame3,font=labelFont, text="Total", anchor=CENTER,relief="solid")
        totalLabel.place(x=889, y=250,width=110)

        ActionLabel=Label(self.frame3,font=labelFont, text="Delete", anchor=CENTER,relief="solid")
        ActionLabel.place(x=999, y=250,width=110)



        frame3 = Frame(self.frame3, bg='#1c748c')
        frame3.place(x=0, y=278, height = 200, width= 1170)

        Mainframe = Frame(frame3,bg="yellow")
        Mainframe.place(x=50, y=0, width=1058, height=200)
        Mainframe1=Frame(Mainframe)
        myCanvas=Canvas(Mainframe1,width=1038,height=200)
        myScrollBar=ttk.Scrollbar(Mainframe1,orient=VERTICAL,command=myCanvas.yview)

        scrollFrame=Frame(myCanvas)
        scrollFrame.bind("<Configure>",lambda e : myCanvas.configure(scrollregion=myCanvas.bbox("all")))

        myCanvas.create_window((0,0),window=scrollFrame, anchor=NW)
        myCanvas.configure(yscrollcommand=myScrollBar.set)
        sr=1
        yval=50
        for i in records:
            srLabel =Label(scrollFrame, font=labelFont, text=sr , anchor=CENTER,relief="solid",width=4)
            srLabel.grid(row=sr,column=0)

            ProductNameLabel =Label(scrollFrame, font=labelFont, text=i[2] , anchor=CENTER,relief="solid",width=13)
            ProductNameLabel.grid(row=sr,column=1)

            categoryNameLabel=Label(scrollFrame,font=labelFont, text=i[3], anchor=CENTER,relief="solid",width=16)
            categoryNameLabel.grid(row=sr,column=2)

            subcategoryNameLabel=Label(scrollFrame,font=labelFont, text=i[4], anchor=W,relief="solid",width=11)
            subcategoryNameLabel.grid(row=sr,column=4)

            brandLabel=Label(scrollFrame,font=labelFont, text=i[5], anchor=CENTER,relief="solid",width=9)
            brandLabel.grid(row=sr,column=5)
    
            priceLabel=Label(scrollFrame,font=labelFont, text=i[6], anchor=CENTER,relief="solid",width=10)
            priceLabel.grid(row=sr,column=6)

            quantityLabel=ttk.Combobox(scrollFrame,font=labelFont,width=9)
            quantityLabel.grid(row=sr,column=7)

            totalLabel=Label(scrollFrame,font=labelFont, text="Total", anchor=CENTER,relief="solid",width=9)
            totalLabel.grid(row=sr,column=8)

            deleteButton=Button(scrollFrame,font=labelFont, text="Delete", anchor=CENTER,relief="solid",width=9,command=lambda i=i:[Backend__Admin.deleteCart(i[0]),self.cartButton()])
            deleteButton.grid(row=sr,column=9)
            sr=sr+1
            yval=yval+30
        

        Mainframe1.place(x=0,y=0)
        myCanvas.pack(side="left",fill="both",expand=True)
        myScrollBar.pack(side="right",fill="y")

        checkoutButton=Button(self.frame3,font=labelFont,text="Checkout",anchor=CENTER,relief=SOLID,command=lambda: Backend__Admin.addTransact(custNameEntry.get(),custContactEntry.get(),var1.get(),records))
        checkoutButton.place(x=50,y=500)

    
    def transactionButton(self,records):
        for widgets in self.frame3.winfo_children():
            widgets.destroy()
        titleFont = Font(family="Times New Roman",size=25, weight="bold")
        labelFont = Font(family="Times New Roman",size=15)
        entryFont = Font(family="Times New Roman",size=14)
        buttonFont = Font(family="Times New Roman",size=18)

        titleLabel = Label(self.frame3, bg='gray', text ='Sales', font=titleFont)
        titleLabel.place(x=30, y=10)   

        srLabel =Label(self.frame3, font=labelFont, text="Sr.No." , anchor=CENTER,relief="solid")
        srLabel.place(x=50, y=250,width=57)

        ProductNameLabel =Label(self.frame3, font=labelFont, text="TransactionID" , anchor=CENTER,relief="solid")
        ProductNameLabel.place(x=107 , y=250,width=150)             

        categoryNameLabel=Label(self.frame3,font=labelFont, text="Customer Name", anchor=CENTER,relief="solid")
        categoryNameLabel.place(x=257, y=250,width=170)

        subcategoryNameLabel=Label(self.frame3,font=labelFont, text="Customer Contact", anchor=CENTER,relief="solid")
        subcategoryNameLabel.place(x=427, y=250,width=132)

        brandLabel=Label(self.frame3,font=labelFont, text="Payment Mode", anchor=CENTER,relief="solid")
        brandLabel.place(x=559, y=250,width=110)
 
        priceLabel=Label(self.frame3,font=labelFont, text="Product ID", anchor=CENTER,relief="solid")
        priceLabel.place(x=669, y=250,width=110)


        frame3 = Frame(self.frame3, bg='#1c748c')
        frame3.place(x=0, y=278, height = 400, width= 1170)

        Mainframe = Frame(frame3,bg="yellow")
        Mainframe.place(x=50, y=0, width=1058, height=400)
        Mainframe1=Frame(Mainframe)
        myCanvas=Canvas(Mainframe1,width=1038,height=400)
        myScrollBar=ttk.Scrollbar(Mainframe1,orient=VERTICAL,command=myCanvas.yview)

        scrollFrame=Frame(myCanvas)
        scrollFrame.bind("<Configure>",lambda e : myCanvas.configure(scrollregion=myCanvas.bbox("all")))

        myCanvas.create_window((0,0),window=scrollFrame, anchor=NW)
        myCanvas.configure(yscrollcommand=myScrollBar.set)
        sr=1
        yval=50
        for i in records:
            srLabel =Label(scrollFrame, font=labelFont, text=sr , anchor=CENTER,relief="solid",width=4)
            srLabel.grid(row=sr,column=0)

            transactIDLabel =Label(scrollFrame, font=labelFont, text=i[0] , anchor=CENTER,relief="solid",width=13)
            transactIDLabel.grid(row=sr,column=1)

            custNameLabel=Label(scrollFrame,font=labelFont, text=i[1], anchor=CENTER,relief="solid",width=16)
            custNameLabel.grid(row=sr,column=2)

            custContactLabel=Label(scrollFrame,font=labelFont, text=i[2], anchor=W,relief="solid",width=17)
            custContactLabel.grid(row=sr,column=4)

            paymentLabel=Label(scrollFrame,font=labelFont, text=i[3], anchor=CENTER,relief="solid",width=13)
            paymentLabel.grid(row=sr,column=5)
    
            prodIDLabel=Label(scrollFrame,font=labelFont, text=i[4], anchor=CENTER,relief="solid",width=12)
            prodIDLabel.grid(row=sr,column=6)

            
            sr=sr+1
            yval=yval+30
        

        Mainframe1.place(x=0,y=0)
        myCanvas.pack(side="left",fill="both",expand=True)
        myScrollBar.pack(side="right",fill="y")
        return



    def welcomeAdminButton(self):
            # Welcome Label
            for widgets in self.frame3.winfo_children():
                widgets.destroy()
            conn=None
            try:
                conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="")
                if conn.is_connected():
                    print("Connected")
                    sql="Select * from admindetails"
                    Cursor=conn.cursor()
                    Cursor.execute(sql)
                    result=Cursor.fetchall()
                    print(result)
            
            except Error as e:
                print(e)
            
            finally:
                if conn is not None and conn.is_connected():
                    conn.close()
            list1=[]
            for i in result:
                for j in range (0,5):
                    list1.append(i[j])
            adminList=list1
            print(adminList)
            welcomeLabel = Label(self.frame3, text='Welcome Admin', fg = "black", bg='#dedcda', font=("Frankin Gothic Medium", 18, 'bold'))
            welcomeLabel.place(x=57, y=66)

            profileSubWindowLabel = Label(self.frame3, bg='#F5F5F5',relief='solid')
            profileSubWindowLabel.place(x=80,y=200, width=1050, height=400)

            profileSubWindowNameLabel = Label(self.frame3, text ='       Profile',anchor='w', font=("Frankin Gothic Medium", 14),relief='solid')
            profileSubWindowNameLabel.place(x=80,y=200, width=1050)

            # Admin Details Labels

            adminnameLabel=Label(self.frame3, text ='Admin Name :',anchor='e', bg='#F5F5F5', font=("Frankin Gothic Medium", 14),relief='flat')
            adminnameLabel.place(x=130,y=260, width=150)

            adminusernameLabel=Label(self.frame3, text ='Username :', bg='#F5F5F5',anchor='e', font=("Frankin Gothic Medium", 14),relief='flat')
            adminusernameLabel.place(x=130,y=320, width=150)

            contactLabel=Label(self.frame3, text ='Contact :',anchor='e', bg='#F5F5F5', font=("Frankin Gothic Medium", 14),relief='flat')
            contactLabel.place(x=130,y=380, width=150)

            emailLabel=Label(self.frame3, text ='E-mail :',anchor='e', bg='#F5F5F5', font=("Frankin Gothic Medium", 14),relief='flat')
            emailLabel.place(x=130,y=440, width=150)

            #Admin Details Entries

            adminnameEntry = Entry(self.frame3, bg='#F5F5F5', fg='black',font=("Franklin Gothic Medium",15),text='Name',relief='solid')
            adminnameEntry.delete(0,END)
            adminnameEntry.insert(1,adminList[1])
            adminnameEntry.place(x=325, y=260, width=500)
            

            adminusernameEntry = Entry(self.frame3, bg='#F5F5F5', fg='black',font=("Franklin Gothic Medium",15),relief='solid')
            adminusernameEntry.delete(0,END)
            adminusernameEntry.insert(1,adminList[0])
            oldUsername=adminList[0]
            adminusernameEntry.place(x=325, y=320, width=500)

            contactEntry = Entry(self.frame3, bg='#F5F5F5', fg='black',font=("Franklin Gothic Medium",15),relief='solid')
            contactEntry.delete(0,END)
            contactEntry.insert(1,adminList[3])
            contactEntry.place(x=325, y=380, width=500)

            emailEntry = Entry(self.frame3, bg='#F5F5F5', fg='black',font=("Franklin Gothic Medium",15),relief='solid')
            emailEntry.delete(0,END)
            emailEntry.insert(1,adminList[4])
            emailEntry.place(x=325, y=440, width=500)

            # Update Button
            updateButton = Button(self.frame3, text = 'Update', bg='#464b53', fg='#F5F5F5', font=("Frankin Gothic Medium", 14), borderwidth=2,relief='flat', command=lambda: Backend__Admin.adminDetails(adminnameEntry.get(),adminusernameEntry.get(),contactEntry.get(),emailEntry.get(),oldUsername))
            updateButton.place(x=110, y=500)        
        
    def changepasswordbutton(self):
            # Change Password Label
            changepasswordLabel = Label(self.frame3, text='Update Password', fg = "black", bg='#dedcda', font=("Frankin Gothic Medium", 18, 'bold'))
            changepasswordLabel.place(x=57, y=66)

            changepasswordSubWindowLabel = Label(self.frame3, bg='#F5F5F5',relief='solid')
            changepasswordSubWindowLabel.place(x=80,y=200, width=1050, height=400)

            changepasswordSubWindowNameLabel = Label(self.frame3, text ='       Change Password',anchor='w', font=("Frankin Gothic Medium", 14),relief='solid')
            changepasswordSubWindowNameLabel.place(x=80,y=200, width=1050)

            # Change Password Labels

            currentpasswordLabel=Label(self.frame3, text ='Current password :',anchor='e', bg='#F5F5F5', font=("Frankin Gothic Medium", 14),relief='flat')
            currentpasswordLabel.place(x=130,y=260, width=205)

            newpassword1Label=Label(self.frame3, text ='New password :', bg='#F5F5F5',anchor='e', font=("Frankin Gothic Medium", 14),relief='flat')
            newpassword1Label.place(x=130,y=320, width=205)

            newpassword2Label=Label(self.frame3, text ='Re-type new password :',anchor='e', bg='#F5F5F5', font=("Frankin Gothic Medium", 14),relief='flat')
            newpassword2Label.place(x=130,y=380, width=205)


            #Admin Details Entries

            currentpasswordEntry = Entry(self.frame3, bg='#F5F5F5', fg='black',show='*',font=("Franklin Gothic Medium",15),text='Name',relief='solid')
            currentpasswordEntry.place(x=375, y=260, width=500)
            

            newpassword1Entry = Entry(self.frame3, bg='#F5F5F5', fg='black',show='*',font=("Franklin Gothic Medium",15),relief='solid')
            newpassword1Entry.place(x=375, y=320, width=500)

            newpassword2Entry = Entry(self.frame3, bg='#F5F5F5', fg='black',show='*',font=("Franklin Gothic Medium",15),relief='solid')
            newpassword2Entry.place(x=375, y=380, width=500)

            # Update Button
            updateButton = Button(self.frame3, text = 'Update Password', bg='#464b53', fg='#F5F5F5', font=("Frankin Gothic Medium", 14), borderwidth=2,relief='flat', command=lambda: [Backend__Admin.changePassword(currentpasswordEntry.get(),newpassword1Entry.get(),newpassword2Entry.get()), newpassword1Entry.delete(0,END),currentpasswordEntry.delete(0,END),newpassword2Entry.delete(0,END)])
            updateButton.place(x=210, y=500)
    
    def logoutButton(self,root):
        quest=messagebox.askokcancel("Logout?","Are you sure?", icon="warning")
        print(quest)
        if quest == True:
            from login import LoginPage
            login =LoginPage(root)
            root.mainloop()
            self.root.destroy()

    def thresholdButton(self):
        Backend__Admin.threshold(self)
        return
    def thresholdButton1(self):
                def recursion():
                    Backend__Admin.threshold(self)
                    return

                for widgets in self.frame3.winfo_children():
                    widgets.destroy()
                
                titleFont = Font(family="Times New Roman",size=25, weight="bold")
                labelFont = Font(family="Times New Roman",size=15)
                entryFont = Font(family="Times New Roman",size=10)
                buttonFont = Font(family="Times New Roman",size=18)

                frame3 = Frame(self.frame3, bg='#1c748c')
                frame3.place(x=0, y=0, height = 685, width= 1240)
                
                titleLabel = Label(frame3, bg='gray', text ='Manage Product', font=titleFont)
                titleLabel.place(x=30, y=10)

                Mainframe = Frame(frame3)
                Mainframe.place(x=10, y=100, width=1170, height=570)
                Mainframe1=Frame(Mainframe)
                
                
                myCanvas=Canvas(Mainframe1,width=1150,height=450)
                myScrollBar=ttk.Scrollbar(Mainframe1,orient=VERTICAL,command=myCanvas.yview)

                scrollFrame=Frame(myCanvas)
                scrollFrame.bind("<Configure>", lambda e:  myCanvas.configure(scrollregion=myCanvas.bbox("all")))

                myCanvas.create_window((0,0),window=scrollFrame, anchor=NW)
                myCanvas.configure(yscrollcommand=myScrollBar.set)
                

                boxLabel = Label(Mainframe, relief='solid')
                #boxLabel.place(x=0, y=0, width=1170, height=570)


                boxTitleLabel = Label(Mainframe, text =' Threshold', font=labelFont, relief=SOLID, anchor=W)
                boxTitleLabel.place(x=0, y=0, width=1170, height=35)

                srLabel =Label(Mainframe, font=labelFont, text="Sr.No." , anchor=CENTER,relief="solid")
                srLabel.place(x=0, y=35,width=57)

                productIDLabel =Label(Mainframe, font=labelFont, text="ID" , anchor=CENTER,relief="solid")
                #productIDLabel.place(x=50, y=35,width=165)

                ProductNameLabel =Label(Mainframe, font=labelFont, text="Name" , anchor=CENTER,relief="solid")
                ProductNameLabel.place(x=57 , y=35,width=125)             

                categoryNameLabel=Label(Mainframe,font=labelFont, text="Category", anchor=CENTER,relief="solid",width=25)
                categoryNameLabel.place(x=182, y=35,width=170)

                subcategoryNameLabel=Label(Mainframe,font=labelFont, text="Sub-Category", anchor=CENTER,relief="solid",width=25)
                subcategoryNameLabel.place(x=352, y=35,width=132)

                brandLabel=Label(Mainframe,font=labelFont, text="Brand", anchor=CENTER,relief="solid",width=25)
                brandLabel.place(x=484, y=35,width=110)
 
                priceLabel=Label(Mainframe,font=labelFont, text="Price", anchor=CENTER,relief="solid",width=25)
                priceLabel.place(x=594, y=35,width=110)

                thresholdLabel=Label(Mainframe,font=labelFont, text="Threshold", anchor=CENTER,relief="solid",width=25)
                thresholdLabel.place(x=704, y=35,width=110)

                quantityLabel=Label(Mainframe,font=labelFont, text="Quantity", anchor=CENTER,relief="solid",width=25)
                quantityLabel.place(x=814, y=35,width=110)


                statusLabel=Label(Mainframe,font=labelFont, text="Status", anchor=CENTER,relief="solid",width=25)
                statusLabel.place(x=924, y=35, width=100)
                

                actionLabel=Label(Mainframe,text='Action',font=labelFont,relief=SOLID,width=14)
                actionLabel.place(x=1024,y=35,width=126)

                
                sr=1
                global pos
                records=Backend__Admin.records
                yval=50
                for i in records:
                    print(i[7])
                    if i[8]==1:
                        text="Active"
                    else: 
                        text="tive"
                    print(text)
                    rowsrLabel=Label(scrollFrame, font=entryFont, text=sr, anchor=CENTER,relief=SOLID, width=7)
                    rowsrLabel.grid(row=sr,column=0)   

                    rowproductIDLabel=Label(scrollFrame, font=entryFont, text=i[0],anchor=W, relief=SOLID, width=22)
                    #rowproductIDLabel.grid(row=sr,column=1)              

                    rowProductNameLabel=Label(scrollFrame, font=entryFont, text=(i[1]),relief=SOLID,width=16)
                    rowProductNameLabel.grid(row=sr,column=2)
                    #rowCatNameLabel.place(x=150,y=yval)

                    rowCatNameLabel=Label(scrollFrame, font=entryFont, text=(i[2]),relief=SOLID,width=25)
                    rowCatNameLabel.grid(row=sr,column=3)

                    rowsubCatNameLabel=Label(scrollFrame, font=entryFont, text=(i[3]),relief=SOLID,width=18)
                    rowsubCatNameLabel.grid(row=sr,column=4)

                    rowBrandNameLabel=Label(scrollFrame, font=entryFont, text=i[4],relief=SOLID,width=15)
                    rowBrandNameLabel.grid(row=sr,column=5)

                    rowPriceLabel=Label(scrollFrame, font=entryFont, text=i[5],relief=SOLID,width=15)
                    rowPriceLabel.grid(row=sr,column=6)

                    rowThresholdLabel=Label(scrollFrame, font=entryFont, text=i[6],relief=SOLID,width=15)
                    rowThresholdLabel.grid(row=sr,column=7)

                    rowQuantityLabel=Label(scrollFrame, font=entryFont, text=i[7],relief=SOLID,width=15)
                    rowQuantityLabel.grid(row=sr,column=8)

                    rowStatusLabel=Label(scrollFrame, font=entryFont, text=text,relief=SOLID,width=13)
                    rowStatusLabel.grid(row=sr,column=9)

                    rowEditButton=Button(scrollFrame, font=entryFont, text=("Edit"), anchor=CENTER ,relief=SOLID,width=8,height=0,command=lambda i=i: self.updateProductButton(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]))
                    rowEditButton.grid(row=sr,column=10)

                    rowDeleteButton=Button(scrollFrame, font=entryFont, text=("Delete"), anchor=CENTER ,relief=SOLID,width=7,height=0,command=lambda i=i:[ Backend__Admin.deleteProduct(i[0]),recursion()])
                    rowDeleteButton.grid(row=sr,column=11)
                    sr=sr+1
                    yval=yval+30       
                Mainframe1.place(x=0,y=75)
                myCanvas.pack(side="left",fill="both",expand=True)
                myScrollBar.pack(side="right",fill="y")
        
                return
        

    def connection(self):
        conn=None
        try:
            conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="")
            if conn.is_connected():
                print("Connected")
        
        except Error as e:
            print(e)
        
        finally:
            if conn is not None and conn.is_connected():
                conn.close()


        return
















    def __init__(self,root):
        
        self.root = root
        self.root.title("IMS---Login")
        self.root.geometry("1340x690+0+0")
        self.root.resizable(False,False)
        
        self.frame1 = Frame(self.root, bg='black')
        self.frame1.place(x=0, y=70, height = 690, width= 157)
        
        self.frame2 = Frame(self.root, bg='black')
        self.frame2.place(x=157, y=0, height = 33, width= 1200)

        self.frame3 = Frame(self.root, bg='#1c748c')
        self.frame3.place(x=157, y=33, height = 685, width= 1200)

        ### ### Login Logo ### ###
        # logoImage = Image.open(r'C:\Users\Austin\Desktop\pythonProject\Images\logo1.png')
        # logoImage = logoImage.resize((157,70),Image.ANTIALIAS)
        # self.logoImage = ImageTk.PhotoImage(logoImage)

        # logoImageLabel  = Label(self.root,image = self.logoImage, bd =4, relief = 'flat')
        # logoImageLabel.place(x=0,y=0, width=157, height= 70)

        self.dashboard()


if __name__=='__main__':
    root = Tk()
    admin = AdminPage(root)
    root.mainloop() 