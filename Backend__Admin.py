from tkinter import *
from tkinter import messagebox,ttk
import tkinter
from tkinter.font import Font
from PIL import Image, ImageTk
import mysql.connector
from mysql.connector import Error
global records




def adminDetails(name,username,contact,email,oldUsername):
        
        
        conn=None
        try:
                conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="")
                if conn.is_connected():
                    print("Connected")
                    sql="UPDATE `admindetails` SET `username` = %s, `name` = %s, `phone` = %s, `email` = %s WHERE `admindetails`.`username` = %s"
                    Cursor=conn.cursor()
                    records=(username,name,contact,email,oldUsername)
                    Cursor.execute(sql,records)
                    print(sql,records)
                    conn.commit()
                    print("Admin details updated")
                    messagebox.showinfo("Success","Admin Details updated successfully")
            
        except Error as e:
                print(e)
            
        finally:
                if conn is not None and conn.is_connected():
                    conn.close()         

def changePassword(oldPass, newPassword1,newPassword2):   
        try:
            conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="") 
            if conn.is_connected():
                    print("Connected")
                    sql="Select password from admindetails"
                    Cursor=conn.cursor()
                    Cursor.execute(sql)
                    currentPass = Cursor.fetchall()
                    print(currentPass)
                    for i in currentPass:
                        curPass = i
                    print(curPass)
                    print(curPass[0])
                    conn.commit()
            
        except Error as e:
                print(e)
            
        finally:
                if conn is not None and conn.is_connected():
                    conn.close()         

        if  newPassword1 == newPassword2 and curPass[0] == oldPass:
            conn=None
            try:
                conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="") 
                if conn.is_connected():
                        print("Connected")
                        sql="UPDATE `admindetails` SET `password` = %s WHERE `admindetails`.`password` = %s"
                        Cursor=conn.cursor()
                        records=(newPassword1,oldPass)
                        Cursor.execute(sql,records)
                        print(sql,records)
                        conn.commit()
                        print("Password updated")
                        messagebox.showinfo("Success","Password updated successfully")
                
            except Error as e:
                    print(e)
                
            finally:
                    if conn is not None and conn.is_connected():
                        conn.close()         
        else:
            messagebox.showwarning("Warning", "Incorrect Password!!!")
        

def AddCategory(status, categoryName):
    import Admin
    conn=None
    if categoryName.replace(" ","")=="":
        messagebox.showerror('Error',"Category name required")
    else:
        try:
            conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="")
            if conn.is_connected():
                if status=="Active":
                    status=1
                else:
                    status=0
                print("Connected")
                print("Status is ",status,"\nCategory Name is ",categoryName)
                sql="""insert into ims.category_subcategory  (Category,Status) values (%s,%s)"""
                record=(categoryName,status)
                print(sql)
                Cursor=conn.cursor()
                print(sql)
                Cursor.execute(sql,record)
                print(sql)
                messagebox.showinfo('Success','Category Added Successfully')
                Cursor.close()
            
        except Error as e:
            messagebox.showerror("Error","Category Name already exixts!!")
            print(e)
            
        finally:
            if conn is not None and conn.is_connected():
                conn.close()
                print("Database closed")
    return

def manageCategory(self):
    from Admin import AdminPage
    conn=None
    try:
        conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="")
        if conn.is_connected():
            print("Database Connected")
            Cursor=conn.cursor()
            global records
            sql="SELECT category,status FROM category_subcategory ORDER BY `category_subcategory`.`Category` ASC"     
            Cursor.execute(sql)
            records=Cursor.fetchall() 
            print("Backend manage category successful!!")
            Cursor.close()
            AdminPage.manageCategoryButtonFront(self)
    except Error as e:
        print(e)
        
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print("Database closed")
    return


def updateCategory(catName,Status,oldCatName):
    import Admin
    print("New Category Name:", catName)
    print("New Status: ",Status)
    conn=None
    try:
         conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="")
         if conn.is_connected():
             print("Connected")
             if Status=="Active":
                 Status=1
             else:
                Status=0
             sql="""UPDATE `category_subcategory` SET `Category` = %s, `Status` = %s WHERE `category_subcategory`.`Category` = %s"""
             records=(catName,Status,oldCatName)
             print(sql)
             Cursor=conn.cursor()
             Cursor.execute(sql,records)

             sql="""UPDATE subcategory SET `catName` = %s WHERE `subcategory`.`catName` = %s"""
             records=(catName,oldCatName)
             Cursor=conn.cursor()
             Cursor.execute(sql,records)
             conn.commit()

             sql="""UPDATE brand SET `catName` = %s WHERE `brand`.`catName` = %s"""
             records=(catName,oldCatName)
             Cursor=conn.cursor()
             Cursor.execute(sql,records)
             conn.commit()

             sql="""UPDATE product SET `Product Category` = %s WHERE `Product Category` = %s"""
             records=(catName,oldCatName)
             Cursor=conn.cursor()
             Cursor.execute(sql,records)
             conn.commit()

             messagebox.showinfo('Success','Category Updated Successfully')
       
    except Error as e:
         print(e)
        
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print("closed")
    print("Hello")
    return

def deleteCategory(catName):
    import Admin
    quest=messagebox.askyesno("Warning!!","This may cause deletion of other sub-elements as well. Are you sure? ")
    if quest==True:
        print("Removing Category Name:", catName)
        conn=None
        try:
            conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="")
            if conn.is_connected():
                print("Connected")
                
                sql="DELETE FROM category_subcategory WHERE Category = '%s'" % (catName)
                Cursor=conn.cursor()
                Cursor.execute(sql)
                conn.commit()
                
                sql="DELETE FROM subcategory WHERE catName = '%s'" % (catName)
                Cursor.execute(sql)
                conn.commit()
                
                sql="DELETE FROM brand WHERE catName = '%s'" % (catName)
                Cursor.execute(sql)
                conn.commit()

                sql="DELETE FROM product WHERE `Product Category` = '%s'" % (catName)
                Cursor.execute(sql)
                conn.commit()
                
                messagebox.showinfo('Success','Category Deleted Successfully')
                from Admin import AdminPage
                #AdminPage.manageCategoryButton(self)
                
        
        except Error as e:
            print(e)
            messagebox.showerror('error',e)
            
        finally:
            if conn is not None and conn.is_connected():
                conn.close()
                print("closed")
        print("Hello")
        return
    else:
        return

def AddSubCategory(status, categoryName, subCategoryName):

    import Admin
    conn=None
    

    if categoryName=="Select":
        messagebox.showerror('Error', 'Category Name required!!')
        
    elif subCategoryName.replace(" ","")=="":
        messagebox.showerror('Error', 'Sub-Category Name reqiured!!')
        
    
    else:        
        try:
            conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="")
            if conn.is_connected():
                print("Database Connected")
                if status=="Active":
                    status=1
                else:
                    status=0
                sql="""insert into ims.subcategory  (subCatName,catName,Status) values (%s,%s,%s)"""
                record=(subCategoryName,categoryName,status)
                print(sql)
                Cursor=conn.cursor()
                Cursor.execute(sql,record)
                messagebox.showinfo('Success','Sub-Category Added Successfully')
                Cursor.close()
            
        except Error as e:
            messagebox.showerror("Error","Sub-Category Name already exixts!!")
            
        finally:
            if conn is not None and conn.is_connected():
                conn.close()
                print("Database connection closed")
    return

def manageSubCategory(self):
    from Admin import AdminPage
    conn=None
    try:
        conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="")
        if conn.is_connected():
            print("Database Connected")
            Cursor=conn.cursor()
            global records 
            sql="SELECT subCatName,catName, Status FROM subcategory ORDER BY `subcategory`.`subCatName` ASC"     
            Cursor.execute(sql)
            records=Cursor.fetchall() 
            print("Backend manage Sub-category successfull!!")
            Cursor.close()
            AdminPage.manageSubCategoryButtonFront(self)
    except Error as e:
        print(e)
        
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print("Database closed")
    return

def updateSubCategory(subCat,catName,Status,subCatOld):
    conn=None
    if Status=="Active":
        Status=1
    else:
        Status=0
    try:
        conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="")
        if conn.is_connected():
            print("Connected")
            sql="UPDATE `subcategory` SET `subCatName` = %s, `catName` = %s, `Status` = %s WHERE `subcategory`.`subCatName` = %s" 
            records=(subCat, catName,Status,subCatOld)
            Cursor=conn.cursor()
            Cursor.execute(sql,records)

            sql="UPDATE `brand` SET `subCatName` = %s WHERE `subCatName` = %s" 
            records=(subCat,subCatOld)
            Cursor=conn.cursor()
            Cursor.execute(sql,records)

            sql="UPDATE `product` SET `Product SubCategory` = %s WHERE `Poduct SubCategory` = %s" 
            records=(subCat,subCatOld)
            Cursor=conn.cursor()
            Cursor.execute(sql,records)


        messagebox.showinfo('Success','SubCategory Updated Successfully')
        
    except Error as e:
        print(e)
        
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print("closed")
    print("Hello")
    return

def deleteSubCategory(subCatName):
    import Admin
    quest=messagebox.askyesno("Warning!!","This may cause deletion of other sub-elements as well. Are you sure? ")
    if quest==True:
        print("Removing Sub-Category Name:", subCatName)
        conn=None
        try:
            conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="")
            if conn.is_connected():
                print("Connected")

                sql="DELETE FROM subcategory WHERE subCatName = '%s'" % (subCatName)
                Cursor=conn.cursor()
                Cursor.execute(sql)
                conn.commit()

                sql="DELETE FROM brand WHERE subCatName = '%s'" % (subCatName)
                Cursor=conn.cursor()
                Cursor.execute(sql)
                conn.commit()

                sql="DELETE FROM product WHERE `Product SubCategory` = '%s'" % (subCatName)
                Cursor=conn.cursor()
                Cursor.execute(sql)
                conn.commit()
                messagebox.showinfo('Success','Sub-Category Deleted Successfully')          
                    
        except Error as e:
            print(e)
            messagebox.showerror('error',e)
            
        finally:
            if conn is not None and conn.is_connected():
                conn.close()
                print("closed")
        return
    else:
        return


def addBrand(Status, catName,subCatName,brandName):
    print("Brand Name:", catName)
    print("Status: ",Status)
    conn=None
    try:
         conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="")
         if conn.is_connected():
             print("Connected")
             if Status=="Active":
                 Status=1
             else:
                Status=0
             sql="""insert into ims.brand (BrandName, catName, subCatName, Status) values (%s,%s,%s,%s)"""
             records=(brandName,catName,subCatName,Status)
             print(sql,records)
             Cursor=conn.cursor()
             Cursor.execute(sql,records)
             conn.commit()
             messagebox.showinfo('Success','Brand Added Successfully')
       
    except Error as e:
         print(e)
         messagebox.showerror("Error",e)
        
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print("closed")
    print("Hello")
    
    return

def manageBrand(self):
    from Admin import AdminPage
    conn=None
    try:
        conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="")
        if conn.is_connected():
            print("Database Connected")
            Cursor=conn.cursor()
            global records 
            sql="SELECT BrandName,subCatName,catName, Status FROM brand Order by BrandName ASC"     
            Cursor.execute(sql)
            records=Cursor.fetchall() 
            print("Backend manage Manage successfull!!")
            Cursor.close()
            AdminPage.manageBrandButtonFront(self)
    except Error as e:
        print(e)
        
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print("Database closed")

def  updateBrand(brand,subCat,catName,Status,brandOld):
    conn=None
    print(Status)
    if Status=="Active":
        Status=1
    else:
        Status=0

    try:
        conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="")
        if conn.is_connected():
            print("Connected")
            sql="UPDATE `brand` SET `BrandName` = %s, `subCatName` = %s, `catName` = %s, `Status` = %s WHERE `brand`.`BrandName` = %s" 
            records=(brand,subCat,catName,Status,brandOld)
            Cursor=conn.cursor()
            print(sql,records)
            Cursor.execute(sql,records)

            sql="UPDATE `product` SET `Product Brand` = %s WHERE `Product Brand` = %s" 
            records=(brand,brandOld)
            Cursor=conn.cursor()
            Cursor.execute(sql,records)
            
        messagebox.showinfo('Success','Brand Updated Successfully')
        
    except Error as e:
        print(e)
        
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print("closed")
    print("Hello")
    return

def deleteBrand(brandName):
    quest=messagebox.askyesno("Warning!!","This may cause deletion of other sub-elements as well. Are you sure? ")
    if quest==True:
        print("Removing Brand Name:", brandName)
        conn=None
        try:
            conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="")
            if conn.is_connected():
                print("Connected")
                sql="DELETE FROM brand WHERE BrandName = '%s'" % (brandName)
                #sql='UPDATE category_subcategory SET Category="'+catName+'"Status=',Status,' WHERE category_subcategory.Category="'+oldCatName+'"'
                records=(brandName)
                print(sql)
                Cursor=conn.cursor()
                Cursor.execute(sql)
                conn.commit()
                print(sql,records)
                messagebox.showinfo('Success','Brand Deleted Successfully')          
                    
        except Error as e:
            print(e)
            messagebox.showerror('error',e)
            
        finally:
            if conn is not None and conn.is_connected():
                conn.close()
                print("closed")
        return
    else:
        return

def addProduct(productName,catName,subcat,brand,prodPrice,threshold,quantity,Status):
    print("Product Name:", productName)
    print("Status: ",Status)
    conn=None
    try:
         conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="")
         if conn.is_connected():
             print("Connected")
             if Status=="Active":
                 Status=1
             else:
                Status=0
             sql="""insert into ims.product (`Product_ID`, `Product name`, `Product Category`, `Product SubCategory`, `Product Brand`,`ProductPrice`, `Product Threshold`, `Product Quantity`, `ProductStatus`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
             productid=productName+"/"+catName+"/"+subcat+"/"+brand
             print(productid, len(productid))
             records=(productid,productName,catName,subcat,brand,prodPrice,threshold,quantity,Status)
             print(sql,records)
             Cursor=conn.cursor()
             Cursor.execute(sql,records)
             conn.commit()
             messagebox.showinfo('Success','Product Added Successfully')
       
    except Error as e:
         print(e)
         messagebox.showerror("Error",e)
        
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print("closed")    
    return

def manageProduct(self):
    from Admin import AdminPage
    conn=None
    try:
        conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="")
        if conn.is_connected():
            print("Database Connected")
            Cursor=conn.cursor()
            global records 
            sql="SELECT * FROM product ORDER BY `product`.`Product name` ASC"     
            Cursor.execute(sql)
            records=Cursor.fetchall() 
            print("Backend manage Product successfull!!")
            Cursor.close()
            AdminPage.manageProductButtonFront(self)
            print(records)
    except Error as e:
        print(e)
        
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print("Database closed")
    
    return

def updateProduct(prodName,catName,subCat,brand,prodPrice,threshold,quantity,Status,prodID):
    conn=None
    print(Status)
    if Status=="Active":
        Status=1
    else:
        Status=0

    try:
        conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="")
        if conn.is_connected():
            print("Connected")
            productid=prodName+"/"+catName+"/"+subCat+"/"+brand
            sql="UPDATE `product` SET `Product_ID`= %s,`Product name` = %s, `Product Category` = %s, `Product SubCategory` = %s, `Product Brand` = %s, `ProductPrice` = %s, `Product Threshold` = %s, `Product Quantity` = %s, `ProductStatus` = %s  WHERE `product`.`Product_ID` = %s" 
            records=(prodID,prodName,catName,subCat,brand,prodPrice,threshold,quantity,Status,prodID)
            Cursor=conn.cursor()
            print(sql,records)
            Cursor.execute(sql,records)
            conn.commit()
            
        messagebox.showinfo('Success','Product Updated Successfully')
        
    except Error as e:
        print(e)
        
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print("closed")    
    return

def deleteProduct(prodID):
    quest=messagebox.askyesno("Warning!!","This may cause deletion of other sub-elements as well. Are you sure? ")
    if quest==True:
        print("Removing Product ID:", prodID)
        
        try:
            conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="")
            if conn.is_connected():
                print("Connected")
                sql=r"DELETE FROM product WHERE Product_ID = '%s'" % (prodID)
                #sql='UPDATE category_subcategory SET Category="'+catName+'"Status=',Status,' WHERE category_subcategory.Category="'+oldCatName+'"'
                records=(prodID)
                print(sql)
                Cursor=conn.cursor()
                Cursor.execute(sql)
                conn.commit()
                print(sql,records)
                messagebox.showinfo('Success','Brand Deleted Successfully')          
                    
        except Error as e:
            print(e)
            messagebox.showerror('error',e)
            
        finally:
            if conn is not None and conn.is_connected():
                conn.close()
                print("closed")
        return
    else:
        return

def addCart(productID,productName,catName,subcat,brand,prodPrice,quantity):
    print("Product Name:", productName)
    conn=None
    try:
         conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="")
         if conn.is_connected():
             sql="""insert into ims.cart (`Product_ID`, `Product Name`, `Product Category`, `Product SubCategory`, `Product Brand`,`Product Price`,`Product Quantity`) values (%s,%s,%s,%s,%s,%s,%s)"""
             records=(productID,productName,catName,subcat,brand,prodPrice,quantity)
             print(sql,records)
             Cursor=conn.cursor()
             Cursor.execute(sql,records)
             conn.commit()
             messagebox.showinfo('Success','Product Added to Cart Successfully')
       
    except Error as e:
         print(e)
         messagebox.showerror("Error",e)
        
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print("closed")    

    return

def showCart(self):
    conn=None
    try:
         conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="")
         if conn.is_connected():
             sql="select * from ims.cart"
             print(sql)
             Cursor=conn.cursor()
             Cursor.execute(sql)
             records=Cursor.fetchall()
             print(records)
             print("Executed")
             from Admin import AdminPage
             AdminPage.cart(self,records)
       
    except Error as e:
         print(e)
         messagebox.showerror("Error",e)
        
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print("closed")    

    return

def deleteCart(sr):
    conn=None
    try:
         print(sr)
         conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="")
         if conn.is_connected():
             sql="Delete from cart where `cart`.`sr`= %s " ,(sr)
             print(sql)
             Cursor=conn.cursor()
             Cursor.execute(sql)
             print("Deleted")
       
    except Error as e:
         print(e)
         messagebox.showerror("Error",e)
        
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print("closed")    

    return

def addTransact(custName,custContact,paymentmode,records):
    conn=None
    print(records)
    String=""
    for i in records:
        print(i[1])
        String=String+",",i[1]
    if(paymentmode==1):
        paymentMode="Cash"
    else:
        paymentMode="Card"
    try:
         conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="")
         if conn.is_connected():
             sql="insert into `Product_ID` from ims.transaction values(`TransID`, `CustName`, `CustContact`, `PaymentMode`, `ProductID`) VALUES ('asda', 'sda', 'sdasdasdas', 'ssss', 'asdasdasd'))"
             print(sql)
             Cursor=conn.cursor()
             Cursor.execute(sql)
             records=Cursor.fetchall()
             print(records)
             l=[]
             for i in records:
                l.append(i[0])
             prodID=l
             import random,string
             s=10
             ran=''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase+string.digits,k=s))
             transID=str(ran)
             sql="""INSERT INTO transaction (TransID,CustName,CustContact,PaymentMode,ProductID) VALUES (%s,%s,%s,%s,%s)"""

             records=(transID,custName,custContact,paymentMode,prodID)
             Cursor.execute(sql,records)
             conn.commit()
             sql="truncate table cart"
             Cursor.execute(sql)
             conn.commit()
             print("Executed")
    except Error as e:
         print(e)
         messagebox.showerror("Error",e)
        
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print("closed")    

    return    
def showTransact(self):
    conn=None
    try:
         conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="")
         if conn.is_connected():
             sql="select * from transaction"
             print(sql)
             Cursor=conn.cursor()
             Cursor.execute(sql)
             records=Cursor.fetchall()
             print(records)
             print("Executed")
             from Admin import AdminPage
             AdminPage.transactionButton(self,records)
       
    except Error as e:
         print(e)
         messagebox.showerror("Error",e)
        
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print("closed")    

    return

def inventory(self):
    from Admin import AdminPage
    conn=None
    try:
        conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="")
        if conn.is_connected():
            print("Database Connected")
            Cursor=conn.cursor()
            global records 
            sql="SELECT * FROM product where ProductStatus=1"     
            Cursor.execute(sql)
            records=Cursor.fetchall() 
            print("Backend cartsuccessfull!!")
            Cursor.close()
            print(records)
            AdminPage.inventory(self)
    except Error as e:
        print(e)
        
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print("Database closed")        

def search(self,searchEntry, searchParameter,order):
    if searchParameter == "":
        messagebox.showerror("Error","Search by Field Required!!")
    if searchEntry=="":
        messagebox.showerror("Error","Search for Field Required!!")
    else:
        if searchParameter=="Product Name":
            searchParameter="Product name"
        elif searchParameter=="Brand":
            searchParameter="Product Brand"
        elif searchParameter=="Sub-Category":
            searchParameter="Product SubCategory"
        else:
            searchParameter="Product Name"
        if order=="Ascending":
            order="ASC"
        elif order=="Descending":
            order="DESC"
        else:
           order="ASC" 
        print(order)

        from Admin import AdminPage
        conn=None
        try:
            conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="")
            if conn.is_connected():
                print("Database Connected")
                Cursor=conn.cursor()
                global records 
                searchEntry='%'+searchEntry+'%'
                sql="SELECT * FROM product  WHERE `%s` LIKE  '%s' ORDER BY product.`%s`  %s" % (searchParameter,searchEntry,searchParameter,order)
                
                records=(searchParameter,searchEntry,searchParameter,order)
                print(sql)
                Cursor.execute(sql)
                records=Cursor.fetchall() 
                print("Backend Search successfull!!")
                Cursor.close()
                print(records)
                AdminPage.search(self)
                if records==[]:
                    messagebox.showinfo("Info","No such product found")
        except Error as e:
            print(e)
            
        finally:
            if conn is not None and conn.is_connected():
                conn.close()
                print("Database closed")
        
    return
def threshold(self):
        from Admin import AdminPage
        conn=None
        try:
            conn=mysql.connector.connect(host="localhost", database="ims",user="root",password="")
            if conn.is_connected():
                print("Database Connected")
                Cursor=conn.cursor()
                global records 
                sql="Select * from product where `Product Threshold` > `Product Quantity`"
                
                print(sql)
                Cursor.execute(sql)
                records=Cursor.fetchall() 
                print("Backend Threshold successfull!!")
                Cursor.close()
                print(records)
                AdminPage.thresholdButton1(self)
                if records==[]:
                    messagebox.showinfo("Info","No product found")
        except Error as e:
            print(e)
            
        finally:
            if conn is not None and conn.is_connected():
                conn.close()
                print("Database closed")
        
        
    

def __init__(self,root):
        self.root = root


if __name__=='__main__':
    root = Tk()
    root.mainloop() 