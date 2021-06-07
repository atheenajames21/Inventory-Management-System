from Admin import AdminPage
from Backend__Admin import *
from tkinter import *
from tkinter.font import Font
from PIL import ImageTk,Image
from ttkthemes import themed_tk as tk
import os
from tkinter import messagebox
from subprocess import call
import mysql.connector

class LoginPage:
    
    mydb = mysql.connector.connect(host = "localhost", user="root", password="", database="ims")
    print(mydb)
    print('host = "localhost", user="root", password="", database="ims"')
    mycursor = mydb.cursor()

    def __init__(self,root):
        self.root = root 
        self.root.title("IMS---Login")
        self.root.geometry("1340x690+0+0")
        self.root.resizable(False,False)

        #### """Login Background Image""" ####
        self.bgImage = Image.open(r'C:\Users\Austin\Desktop\Inventory\Images\loginBackground.jpg')
        self.bgImage = self.bgImage.resize((1340,690),Image.ANTIALIAS)
        self.logoImage = ImageTk.PhotoImage(self.bgImage)
        self.bgImage = Label(self.root, image=self.logoImage).place(x=0,y=0,width=1340,height=690)

        #### """Login Frame """ ####
        loginFrame = Frame(self.root, bg='#af9bd6')
        loginFrame.place(x=100, y=250, height = 300, width= 450)

        #### """Login Frame Components""" ####
        titleFont = Font(family="Times New Roman",size=35, weight="bold")
        labelFont = Font(family="Times New Roman",size=15)
        entryFont = Font(family="Times New Roman",size=14)
        buttonFont = Font(family="Times New Roman",size=20)

        titleLabel = Label(loginFrame, text="Admin Login", font=titleFont,bg='#af9bd6')
        titleLabel.place(x=90, y=10)

        usernameLabel =Label(loginFrame, text = "Username", font = labelFont,bg='#af9bd6')
        usernameLabel.place(x=50,y=100)

        passwordLabel = Label(loginFrame, text = 'Password', font = labelFont,bg='#af9bd6')
        passwordLabel.place(x=50,y=170)

        self.usernameEntry = Entry(loginFrame, font=entryFont)
        self.usernameEntry.place(x=50,y=125)

        self.passwordEntry = Entry(loginFrame,show='*',font=entryFont)
        self.passwordEntry.place(x=50,y=195)

        loginButton = Button(loginFrame,text='Login', font=buttonFont, relief = 'flat', command=self.loginButton)
        loginButton.place(x=50,y=235, height=40, width=80)
        return









    def loginButton(self):
        if self.usernameEntry.get()=="" or self.passwordEntry.get()=="":
            messagebox.showwarning("Error","All fields required", parent=self.root)
            print("All fields required")
        else:
            print("hello world")
            user=self.usernameEntry.get()
            passw=self.passwordEntry.get()
            print(user,passw)
            self.loginSecurity(user,passw)
    

    def loginSecurity(self,user, passw):
        user=user
        passw=passw
        print(user, passw)
        loginSQL="Select * from admindetails where username='"+user+"' AND password = '"+passw+"'"
        print(loginSQL)
        self.mycursor.execute(loginSQL)
        print("execute done")
        result = self.mycursor.fetchall()
        print("fetchall done")
        for x in result:
            print("result")
            print(x)
        print('result')
        if len(result)!=0:
            print("Deiconify")
            import Admin
            admin=AdminPage(root)
            root.mainloop()
            self.root.destroy()

            
            
        else:
            messagebox.showerror("Error","Wrong Username/Password", parent=self.root)
            



if __name__ == '__main__':
    root = Tk()
    login = LoginPage(root)
    root.mainloop()
