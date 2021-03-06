import AddForm as Addform
from EditForm import *
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import sqlite3
from SQLBill import *
from SQLChiTietBill import *

class ShowChitietBill():
    def __init__(self,IDBill):
        self.IDBill = IDBill
    def display(self):
        self.rootShow = tk.Tk()
        self.rootShow.title = 'Doanh Thu'
     
        self.crud = SQLBILL()
        w = 300
        h = 700
        ws = self.rootShow.winfo_screenwidth()
        hs = self.rootShow.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.rootShow.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.rootShow.configure(bg = '#dff9fb')
        self.labelContent()
        self.labelBill()
#===============Label====================
    def labelContent(self):
        lb_Content = tk.Label(
            self.rootShow,
            text = 'Chi tiết Bill: '+ str(self.IDBill),
            font = ('Times', 15, 'italic'),
            fg = 'Black',
            bg = '#dff9fb'
            )
        lb_Content.pack(pady=5)

    def labelBill(self):
        DSPrice ={"Trà sữa sô-cô-la": 30000,"Thạch rau câu": 5000,"Thạch thủy tinh": 5000,"Trân châu đen": 5000,"Trân châu trắng": 5000,"Trân châu hoàng kim": 5000,"Plan": 5000,"Nước ngọt" : 15000,"Trà sữa thái xanh" : 30000,"Chocolate đá xay" : 30000,"Trà chanh" : 20000,"Cà phê đá": 20000,"Cà phê sữa" : 25000,"Nước dừa" :25000, "Nước cam" : 25000, "Nước suối" : 10000}
        listfood = self.crud.FoodForBill(self.IDBill)
        tt = 0
        lb_Content = tk.Label(
            self.rootShow,
            text = 'Các món đã gọi ',
            font = ('Times', 15, 'italic'),
            fg = 'Black',
            bg = '#dff9fb'
            )
        lb_Content.pack(pady=5)
        for index,item in enumerate(listfood):
            Label(self.rootShow,text="Tên : "+ item[0] +"  SL: "+ item[1]+ "  Giá:  "+ str(DSPrice[str(item[0]).strip()] *int(item[1])) + "VNĐ").pack(anchor = "w" ,padx =10,pady=10)
            tt = tt +DSPrice[str(item[0]).strip()] *int(item[1])
        lb_Total = tk.Label(
            self.rootShow,
            text = 'Tổng tiền '+ str(tt)+ " VNĐ ",
            font = ('Times', 15, 'italic'),
            fg = 'Black',
            bg = '#dff9fb'
            )
        lb_Total.pack(pady=5)
#===============Funtion====================
    
    