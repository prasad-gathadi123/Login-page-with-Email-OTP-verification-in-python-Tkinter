import random
import string
from tkinter import *
import tkinter.messagebox
from functools import partial
from tkinter import *
from PIL import Image , ImageTk
from time import sleep
import datetime as dt
from time import sleep
import datetime
import tkinter.messagebox
import mysql.connector
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase
from email import encoders

mydb = mysql.connector.connect(
                            host="localhost",      ##This information is defferent in your case 
                            user="root",		   ##correctly write the user , password and database name
                            passwd="",
                            database = "login"
                            )
mycursor = mydb.cursor()

def raise_frame(frame):
    frame.tkraise()
#root = tk.Tk()
main_win = Tk()
main_win.geometry('600x700')
main_win.title("Registration Form")

def main():
    t = datetime.datetime.now()
    time_now = t.strftime("%c")
    fourth_frame = Frame(main_win)
    fourth_frame.place(x=0, y=0, width=600, height=700)

    third_frame = Frame(main_win)
    third_frame.place(x=0, y=0, width=600, height=700)

    second_frame = Frame(main_win)
    second_frame.place(x=0, y=0, width=600, height=700)

    first_frame = Frame(main_win)
    first_frame.place(x=0, y=0, width=600, height=700)
    def next_to_verify(args):
        emailidget = args
        new_pass = StringVar()
        def update_to_database():
            ps_updated = new_pass.get()
            mycursor = mydb.cursor()
            sql_select_query = """Update register set email = %s , passwd = %s where email = %s"""
            change = (emailidget , ps_updated , emailidget)
            mycursor.execute(sql_select_query, change)
            mydb.commit()
            tkinter.messagebox.showinfo("Success!",'New Password Updated Successfully!')
            main()
            
        l1v = Label(fourth_frame , text = "Enter New  Password  :   " , width = 18 , font=("helvetica",12,"bold"))
        l1v.place(x = 110,y=380)
        e1v = Entry(fourth_frame,textvar=new_pass)
        e1v.place(x = 320 , y= 380)
        Button(fourth_frame, text='Submit',width=20,bg='brown',fg='white',command=update_to_database).place(x=210,y=430)            
        Button(fourth_frame, text="HOME",width=20,bg='white',fg='black', command=main).place(x=10,y=10)
    def frtpass():
        emailid = StringVar()
        def update():
           # tkinter.messagebox.showinfo("OTP",'Enter OTP send to Email Id. ')
            #otp_get = otp.get()
            otp = StringVar()
            emailidget = emailid.get()
            try :
                def get_otp(stringLength=8):
                    lettersAndDigits = string.ascii_letters + string.digits
                    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))
                o = get_otp(8);
                s = "Password Reset"
                c = "OTP for Password Reset  : \n"+o+"\n thank you!"
                send_email(emailidget, c , s)
                tkinter.messagebox.showinfo("OTP",'Enter OTP send to Email Id. ')
            except:
                tkinter.messagebox.showinfo("Error",'Email not send try again later! ')
                main()
            def check():
                otp_get_var = otp.get()
                if(o == otp_get_var):
                    next_to_verify(emailidget)
                else :
                    tkinter.messagebox.showinfo("Error",'You Entered Wrong OTP try again')
                    
            
            l1v = Label(fourth_frame , text = "Enter OTP   :   " , width = 18 , font=("helvetica",12,"bold"))
            l1v.place(x = 110,y=270)
            e1v = Entry(fourth_frame,textvar=otp)
            e1v.place(x = 320 , y= 270)
            Button(fourth_frame, text='Submit',width=20,bg='brown',fg='white' , command = check).place(x=210,y=320)
            #delay()

       
        l1v = Label(fourth_frame , text = "Enter Email ID      :   " , width = 18 , font=("helvetica",12,"bold"))
        l1v.place(x = 110,y=150)
        e1v = Entry(fourth_frame,textvar=emailid)
        e1v.place(x = 320 , y= 150)
        Button(fourth_frame, text='Submit',width=20,bg='brown',fg='white',command =update).place(x=210,y=200)
        Button(fourth_frame, text="HOME",width=20,bg='white',fg='black', command=main).place(x=10,y=10)
        raise_frame(fourth_frame)
        
    def next_page():
        l2m = Label(third_frame, text="login Successfully!!!!!",width=40,font=("bold", 16))
        l2m.place(x=50,y=80)
        Button(third_frame, text="HOME",width=20,bg='white',fg='black', command=main).place(x=10,y=10)       
        raise_frame(third_frame)

    def login():
        emailid = StringVar()
        psd  = StringVar()
        def check_criteria() :
            email__get = emailid.get()
            psdget = psd.get()
            try:
                mycursor = mydb.cursor()
                sql_select_query = """select * from register where email = %s"""
                mycursor.execute(sql_select_query, (email__get,))
                myresult = mycursor.fetchall()
                if(psdget == myresult[0][3]) :
                    next_page()
                else:
                    tkinter.messagebox.showinfo("Error",'Invalid Email Or Password Please Try again !')
                    login()
            except:
                tkinter.messagebox.showinfo("Error",'Invalid Email Or Password Please Try again !')
                login()
        
        l1v = Label(second_frame , text = "Enter Email ID      :   " , width = 18 , font=("helvetica",12,"bold"))
        l1v.place(x = 110,y=150)
        e1v = Entry(second_frame,textvar=emailid)
        e1v.place(x = 320 , y= 150)


        
        l1v = Label(second_frame , text = "Password      :   " , width = 18 , font=("helvetica",12,"bold"))
        l1v.place(x = 110,y=200)
        e1v = Entry(second_frame,textvar=psd)
        e1v.place(x = 320 , y= 200)
        
        
        Button(second_frame, text='Login',width=20,bg='brown',fg='white',command = check_criteria).place(x=120,y=250)
        Button(second_frame, text='Forgot Password?',width=20,bg='brown',fg='white',command = frtpass).place(x=215,y=300)
        
        Button(second_frame, text='EXIT',width=20,bg='brown',fg='white',command = ex).place(x=320,y=250) 
        l1m = Label(second_frame, text="Login",width=40,font=("bold", 16))
        l1m.place(x=50,y=50)
        Button(second_frame, text="HOME",width=20,bg='white',fg='black', command=main).place(x=10,y=10)        
        raise_frame(second_frame)

    def register():
        pwd = StringVar()
        fn = StringVar()
        ln = StringVar()
        emid = StringVar()
        def set_data():
            firstname = fn.get()
            lastname = ln.get()
            emailid = emid.get()
            passwd = pwd.get()
            
            try :
                mycursor = mydb.cursor()
                mycursor.execute('CREATE TABLE IF NOT EXISTS register (firstname varchar(55) , lastname varchar(55) , email varchar(55) ,passwd varchar(55))')
                mycursor.execute('INSERT INTO register (firstname, lastname,email,passwd) VALUES(%s,%s,%s,%s)',(firstname.upper() , lastname.upper() , emailid ,passwd))                
                mydb.commit()
                mycursor.close()
                s = 'Registration Confirmed'
                c = "Congratulation !!! "+ firstname.upper() +" "+ lastname.upper() +"\nYour Registration Completed."
                send_email(emailid,c,s)
                tkinter.messagebox.showinfo("Welcome",'User is Successfully Signed up !! \nDetails send to Your Registered Email Id. ')
                main()
            except :
                tkinter.messagebox.showinfo("Error",'Please Enter Valid Email Id ')
                

        def verify_email():
            otp = StringVar()
            emailidget = emid.get()
            try :
                def get_otp(stringLength=8):
                    lettersAndDigits = string.ascii_letters + string.digits
                    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))
                o = get_otp(8);
                s = " One Time Password "
                c = "OTP for Verify Email Id   : \n"+o+"\nThank you!"
                send_email(emailidget, c , s)
                tkinter.messagebox.showinfo("OTP",'Enter OTP send to Email Id. ')
            except :
                tkinter.messagebox.showinfo("Error",'Email not send try again later! ')
                main()
            def check():
                otp_get_var = otp.get()
                if(o == otp_get_var):
                    set_data()
                else :
                    tkinter.messagebox.showinfo("Error",'You Entered Wrong OTP try again')    

            l1v = Label(first_frame , text = "Enter OTP   :   " , width = 18 , font=("helvetica",12,"bold"))
            l1v.place(x = 110,y=450)
            e1v = Entry(first_frame,textvar=otp)
            e1v.place(x = 320 , y= 450)
            Button(first_frame, text='Register',width=20,bg='brown',fg='white' , command = check).place(x=110,y=500)


					
            #Button(first_frame, text='Register',width=20,bg='brown',fg='white',command =set_data ).place(x=110,y=450)
            
        l1n = Label(first_frame , text = "First Name      :   " , width = 18 , font=("helvetica",12,"bold"))
        l1n.place(x = 110,y=140)
        e1n = Entry(first_frame,textvar=fn)
        e1n.place(x = 320 , y= 140)

        l2n = Label(first_frame , text = "Last Name      :   " , width = 18 , font=("helvetica",12,"bold"))
        l2n.place(x = 110,y=190)
        e2n = Entry(first_frame,textvar=ln)
        e2n.place(x = 320 , y= 190)

        l3n = Label(first_frame , text = "Email Id           :   " , width = 18 , font=("helvetica",12,"bold"))
        l3n.place(x = 110,y=240)
        e3n = Entry(first_frame,textvar=emid)
        e3n.place(x = 320 , y= 240)
        
        l11n = Label(first_frame , text = "Password      :   " , width = 18 , font=("helvetica",12,"bold"))
        l11n.place(x = 110,y=290)
        e11n = Entry(first_frame,textvar=pwd)
        e11n.place(x = 320 , y= 290)
        
        Button(first_frame, text='Submit',width=20,bg='brown',fg='white',command =verify_email ).place(x=110,y=350)
        Button(first_frame, text='Exit',width=20,bg='brown',fg='white', command=ex).place(x=320,y=350)
        
        Button(first_frame, text="HOME",width=20,bg='white',fg='black', command=main).place(x=10,y=10)       
        raise_frame(first_frame)
        
    def ex():
        tkinter.messagebox.askquestion("Exit ?",'Do You Want to Exit ?')
        exit()
        
    def send_email(email_id,containt, s):
        toaddr = email_id
        me = 'Here write your own email id'
        subject= s
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = me
        msg['To'] = toaddr
        body =containt
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(user = 'Here write your own email id',password='Write password correctly')
        server.send_message(msg)
        server.quit()

    date = dt.datetime.now()
    w = Label(main_win, text=f"{dt.datetime.now():%a, %b %d %Y}", fg="white", bg="black", font=("helvetica", 10))
    w.place(x = 20, y=20)
    l1m = Label(main_win, text="Welcome To ",width=40,font=("bold", 16))
    l1m.place(x=50,y=50)
    l2m = Label(main_win, text="Registration Page ",width=40,font=("bold", 16))
    l2m.place(x=50,y=80)

    Button(main_win, text="Register",width=20,bg='brown',fg='white', command=register).place(x=230,y=200) 
    Button(main_win, text="Login",width=20,bg='brown',fg='white', command=login).place(x=230,y=250) 
    Button(main_win, text="EXIT",width=20,bg='brown',fg='white', command=ex).place(x=230,y=300) 

    main_win.mainloop()


if __name__ == "__main__":
    main()
