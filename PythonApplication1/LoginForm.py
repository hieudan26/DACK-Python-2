import Project
from mydb import *
from RegisterForm import *
from FormQuanLy import *
from Project import *
import numpy as np
import matplotlib as mpl 
import matplotlib.pyplot as plt
from AddForm import *
from ShowStaff import *
from EditForm import *
from DoanhThu import *
from Static import *
from Project import *
from class1 import *


class LoginForm():
    """description of class"""
    def __init__(self):
        self.LoginForm = Tk();
        self.frm = ManageMenu()
        pass
#=====================LOGINFORM DESIGN===============
    def setupLoginForm(self):

        self.LoginForm.title('Login')
        self.LoginForm.geometry("418x433")
        self.LoginForm.configure(bg = 'Purple')
        self.LoginForm.minsize(418,433)
        self.LoginForm.maxsize(418,433)
        self.Content()
        self.UserName_Textbox()
        self.Password_Textbox()
        self.Cancel_Button()
        self.Login_Button()
        self.Register_Button()
        
        self.LoginForm.mainloop()
        

    #set up content
    def Content(self):
        Content_Label = tk.Label(
            self.LoginForm, 
            text = "Account Login", 
            font = ("Comic Sans MS", 25, "bold", "underline"),
            fg='aqua',
            bg = "Purple")
        Content_Label.place(x = 96, y = 24)

    #set up Text Box Username
    def UserName_Textbox(self):
        userName_Label = tk.Label(
            self.LoginForm, 
            text = "Username:", 
            font = ("Yu Gothic UI", 15),
            fg='white', 
            bg = 'Purple')
        userName_Label.place(x = 28, y = 128)
        self.userName_TextBox = Entry(
            self.LoginForm,
            font =("Yu Gothic UI", 15))
        self.userName_TextBox.place(x = 142, y = 128)




    #set up Text Box Password
    def Password_Textbox(self):
        passWord_Label = tk.Label(self.LoginForm, 
                               text = "Password:", 
                               font = ("Yu Gothic UI", 15),
                               fg='white', 
                               bg = 'Purple')
        passWord_Label.place(x = 32, y = 185)
        self.passWord_TextBox = Entry(
            self.LoginForm,
            font =("Yu Gothic UI", 15), 
            show = "*")
        self.passWord_TextBox.place(x = 142, y = 185)



    #set up Button Cancel
    def Cancel_Button(self):
        self.cancel_Button = tk.Button(
            self.LoginForm, 
            text = "Cancel", 
            font = "Helvetica 15 bold",
            fg = 'white',
            bg = 'red',
            bd =  10,
            highlightthickness=4, 
            highlightcolor="#37d3ff", 
            highlightbackground="#37d3ff", 
            borderwidth=4,
            width = 11,
            command = self.cancelCommand)
        self.cancel_Button.place(x = 37, y = 249)


    #set up Button Login
    def Login_Button(self):
        self.login_Button = tk.Button(self.LoginForm, text = "Login", font = "Helvetica 15 bold",
                      fg = 'white',
                      bg = 'green3',
                      bd =  10, 
                      highlightthickness=4, 
                      highlightcolor="#37d3ff", 
                      highlightbackground="#37d3ff", 
                      borderwidth=4,
                      width = 11,
                      command = lambda : self.loginCommand())
        self.login_Button.place(x = 221, y = 249)



    #set up Button Register
    def Register_Button(self):
        self.register_Button = tk.Button(self.LoginForm, text = "Register", font = "Helvetica 15 bold",
                      fg = 'white',
                      bg = 'blue',
                      bd =  10, 
                      highlightthickness=4, 
                      highlightcolor="#37d3ff", 
                      highlightbackground="#37d3ff", 
                      borderwidth=4,
                      width = 10,
                      command = self.setupRegisterCommand)
        self.register_Button.place(x = 135, y = 318)



#==========================COMMAND============================

    def cancelCommand(self):
        self.LoginForm.destroy()


    def loginCommand(self):
        mdb = mydb()
        if self.userName_TextBox.get() == "" or self.passWord_TextBox.get() == "":
            messagebox.showerror("Login", "L???i: Username, Password kh??ng ???????c b??? tr???ng")
        else:
            username = self.userName_TextBox.get()
            password = self.passWord_TextBox.get()
            dt = mdb.getData("Select * from login where username = '"+ username + "' and password = '"+ password + "'")

            if len(dt) != 0:
                self.OpenWordForm(dt[0][0]);
            else:
                messagebox.showerror("Login", "L???i: Username, Password kh??ng ????ng")
    def OpenWordForm(self,id):
        mdb = mydb()
        dt = mdb.getData("SELECT Chucvu, tennhanvien FROM login, NhanVien  where login.id = NhanVien.IDnhanvien and id = " + str(id))
        if len(dt)!=0 and dt[0][0] == 'Qu???n L??':
            messagebox.showinfo("Login","????ng nh???p qu???n l?? th??nh c??ng")
            frmQuanLy = FormQuanLy()
            self.LoginForm.destroy()
            frmQuanLy.setupForm()
        else:
            self.setupFormNhanVien()

    def setupFormNhanVien(self):
        self.passWord_TextBox.delete(0, len(self.passWord_TextBox.get()))
        self.userName_TextBox.delete(0, len(self.userName_TextBox.get()))
        self.LoginForm.destroy()
        self.frm.display()

    def setupRegisterCommand(self):
        resForm = RegisterForm()
        resForm.setUpRegisterForm()


