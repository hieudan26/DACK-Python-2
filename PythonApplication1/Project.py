import os
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from tkinter import *
import random
import time
import datetime
from SQLBill import *
from SQLChiTietBill import *



class ManageMenu(object):


	def display(self):
		self.root=tk.Tk()
		self.root.geometry("1550x850")
		self.root.title("Coffee Management System")
		self.root.configure(background='#7BED9F')
		# ========================================================================================================
		#                                FRAMES
		#========================================================================================================
		self.Tops = tk.Frame(self.root, width=1550, height=80, bd = 2, relief="raise", bg = '#7BED9F')
		self.Tops.pack(side = TOP)
		self.lblTitle = tk.Label(self.Tops, font=("arial", 50, 'bold'), text="             Quản lý quán cà phê         ", bg = '#7BED9F')
		self.lblTitle.grid(row=0, column=0)


		#==================================DATE TIME======================================================
		self.localtime=time.asctime(time.localtime(time.time()))
		self.lblInfo=tk.Label(self.Tops,font=('arial',20,'bold'),text=self.localtime,anchor='w', bg = '#7BED9F')
		self.lblInfo.grid(row=1,column=0)
		#===================================================================================================


		self.BottomMainFrame = tk.Frame(self.root, width=1550, height=770, bd = 2, relief="raise", bg = '#7BED9F')
		self.BottomMainFrame.pack(side=BOTTOM)

		self.f1 = tk.Frame(self.BottomMainFrame, width=500, height=770, bd = 2, relief=SUNKEN, bg = '#7BED9F')
		self.f1.pack(side=LEFT)

		self.f1top = tk.Frame(self.f1, width=500, height=570, bd = 2, relief="raise", bg = '#7BED9F')
		self.f1top.pack(side=TOP)
		#f1bottom = Frame(f1, width=500, height=200, bd=12, relief="raise", bg = "#0066FF")
		#f1bottom.pack(side=BOTTOM)


		self.f2 = tk.Frame(self.BottomMainFrame, width=400, height=770,relief=SUNKEN, bg = '#7BED9F', bd = 2)
		self.f2.pack(side=LEFT)
		self.f2Top = tk.Frame(self.f2, width=400, height=350, relief="raise", bg = '#7BED9F')
		self.f2Top.pack(side=TOP)
		#f2Bottom = Frame(f2, width=400, height=450,bd=4, relief="raise")
		#f2Bottom.pack(side=RIGHT)

		self.f4 = tk.Frame(self.BottomMainFrame, width=400, height=770, bd=2, relief=SUNKEN, bg = '#7BED9F')
		self.f4.pack(side=RIGHT)

		self.f3 = tk.Frame(self.BottomMainFrame, width=400, height=1000, bd=2, relief=SUNKEN, bg = '#7BED9F')
		self.f3.pack(side=LEFT)
		self.f3left = tk.Frame(self.f3, width=500, height=1000, bd=2, relief="raise", bg = '#7BED9F')
		self.f3left.pack(side = LEFT)
		self.f3right = tk.Frame(self.f3, width=500, height=1000, bd=2, relief="raise", bg = '#7BED9F')
		self.f3right.pack(side = RIGHT)

		# ========================================================================================================
		#                                VARIABLES
		#========================================================================================================
		self.Receipt_Ref = tk.StringVar()
		self.DateofOrder = tk.StringVar()
		self.DateofOrder.set(time.strftime("%d/%m/%y"))


		self.cPlan = tk.IntVar()
		self.cTranChauDen = tk.IntVar()
		self.cTranChauTrang = tk.IntVar()
		self.cTranChauHoangKim = tk.IntVar()
		self.cThachRauCau = tk.IntVar()
		self.cThachThuyTinh = tk.IntVar()
		self.cTraChan = tk.IntVar()
		self.cNuocDua = tk.IntVar()
		self.cCaPheDa = tk.IntVar()
		self.cNuocCam = tk.IntVar()
		self.cNuocSuoi = tk.IntVar()
		self.cChocolateDaXay = tk.IntVar()
		self.cTraSuaSocola = tk.IntVar()
		self.cTraSuaThai = tk.IntVar()
		self.cCaPheSua = IntVar()
		self.cNuocNgot = tk.IntVar()



		self.cPlan.set(0)
		self.cTranChauDen.set(0)
		self.cTranChauTrang.set(0)
		self.cTranChauHoangKim.set(0)
		self.cThachRauCau.set(0)
		self.cThachThuyTinh.set(0)
		self.cTraChan.set(0)
		self.cNuocDua.set(0)
		self.cCaPheDa.set(0)
		self.cNuocCam.set(0)
		self.cNuocSuoi.set(0)
		self.cChocolateDaXay.set(0)
		self.cTraSuaSocola.set(0)
		self.cTraSuaThai.set(0)
		self.cCaPheSua.set(0)
		self.cNuocNgot.set(0)


		#====================================BOTTOM FRAME : FRAME 2 TOP FRAME VARIABLES==================================================
		self.varPlan = tk.StringVar()
		self.varTranChauDen = tk.StringVar()
		self.varTranChauTrang = tk.StringVar()
		self.varTranChauHoangKim = tk.StringVar()
		self.varThachRauCau = tk.StringVar()
		self.varThachThuyTinh = tk.StringVar()

		self.varPlan.set(0)
		self.varTranChauDen.set(0)
		self.varTranChauTrang.set(0)
		self.varTranChauHoangKim.set(0)
		self.varThachRauCau.set(0)
		self.varThachThuyTinh.set(0)

		#====================================BOTTOM FRAME : FRAME 2 BOTTOM FRAME VARIABLES==================================================
		self.varTotal = tk.StringVar()
		self.varVAT = tk.StringVar()
		self.varPay = tk.StringVar()
		self.varPM = tk.StringVar()
		self.varTotal.set(0)
		self.varVAT.set(0)
		self.varPay.set(0)

		#====================================BOTTOM FRAME : FRAME 3 VARIABLES==================================================
		self.varTraChan = tk.StringVar()
		self.varNuocDua = tk.StringVar()
		self.varCaPheDa = tk.StringVar()
		self.varNuocCam = tk.StringVar()
		self.varNuocSuoi= tk.StringVar()
		self.varChocolateDaXay = tk.StringVar()
		self.varTraSuaSocola = tk.StringVar()
		self.varTraSuaThai = tk.StringVar()
		self.varCaPheSua = tk.StringVar()
		self.varNuocNgot = tk.StringVar()

		self.varTraChan.set(0)
		self.varNuocDua.set(0)
		self.varCaPheDa.set(0)
		self.varNuocCam.set(0)
		self.varNuocSuoi.set(0)
		self.varChocolateDaXay.set(0)
		self.varTraSuaSocola.set(0)
		self.varTraSuaThai.set(0)
		self.varCaPheSua.set(0)
		self.varNuocNgot.set(0)      

		self.bill = SQLBILL()
		self.CTbill = SQLChiTietBill()

				#                       FRAME 1
		# ================================================================================

		self.lblinfo = tk.Label(self.f3left, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5, bg = '#7BED9F')
		self.lblinfo.grid(row = 0, column = 0)
		self.lblinfo = tk.Label(self.f3left, font=('aria', 15, 'bold'), text="_____________", fg="#7BED9F", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row=2, column=0)
		self.lblinfo = tk.Label(self.f3right, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row = 3, column = 0)
		self.lblinfo = tk.Label(self.f3right, font=('aria', 15, 'bold'), text="______", fg="#7BED9F", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row=4, column=0)

		self.lblinfo = tk.Label(self.f3left, font=('aria', 15, 'bold'), text="Trà chanh", fg="steel blue", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row = 3, column = 0)
		self.lblinfo = tk.Label(self.f3right, font=('aria', 15, 'bold'), text="20.000", fg="steel blue", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row = 5, column = 0)
		self.lblinfo = tk.Label(self.f3left, font=('aria', 15, 'bold'), text="Cà phê đá", fg="steel blue", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row = 4, column = 0)
		self.lblinfo = tk.Label(self.f3right, font=('aria', 15, 'bold'), text="20.000", fg="steel blue", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row = 6, column = 0)
		self.lblinfo = tk.Label(self.f3left, font=('aria', 15, 'bold'), text="Cà phê sữa", fg="steel blue", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row = 5, column = 0)
		self.lblinfo = tk.Label(self.f3right, font=('aria', 15, 'bold'), text="25.000", fg="steel blue", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row = 7, column = 0)

		self.lblinfo = tk.Label(self.f3left, font=('aria', 15, 'bold'), text="Nước dừa", fg="steel blue", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row = 6, column = 0)
		self.lblinfo = tk.Label(self.f3right, font=('aria', 15, 'bold'), text="25.000", fg="steel blue", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row = 8, column = 0)
		self.lblinfo = tk.Label(self.f3left, font=('aria', 15, 'bold'), text="Nước cam", fg="steel blue", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row = 7, column = 0)
		self.lblinfo = tk.Label(self.f3right, font=('aria', 15, 'bold'), text="25.000", fg="steel blue", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row = 9, column = 0)
		self.lblinfo = tk.Label(self.f3left, font=('aria', 15, 'bold'), text="Nước suối", fg="steel blue", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row = 8, column = 0)
		self.lblinfo = tk.Label(self.f3right, font=('aria', 15, 'bold'), text="10.000", fg="steel blue", anchor=W ,bg = '#7BED9F')
		self.lblinfo.grid(row = 10, column = 0)
		self.lblinfo = tk.Label(self.f3left, font=('aria', 15, 'bold'), text="Chocolate đá xay", fg="steel blue", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row = 9, column = 0)
		self.lblinfo = tk.Label(self.f3right, font=('aria', 15, 'bold'), text="30.000", fg="steel blue", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row = 11, column = 0)

		self.lblinfo = tk.Label(self.f3left, font=('aria', 15, 'bold'), text="Trà sữa sô-cô-la", fg="steel blue", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row = 10, column = 0)
		self.lblinfo = tk.Label(self.f3right, font=('aria', 15, 'bold'), text="30.000", fg="steel blue", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row = 12, column = 0)
		self.lblinfo = tk.Label(self.f3left, font=('aria', 15, 'bold'), text="Trà sữa thái xanh", fg="steel blue", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row = 11, column = 0)
		self.lblinfo = tk.Label(self.f3right, font=('aria', 15, 'bold'), text="30.000", fg="steel blue", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row = 13, column = 0)
		self.lblinfo = tk.Label(self.f3left, font=('aria', 15, 'bold'), text="Nuoc ngọt", fg="steel blue", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row = 12, column = 0)
		self.lblinfo = tk.Label(self.f3right, font=('aria', 15, 'bold'), text="15.000", fg="steel blue", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row = 14, column = 0)

		self.lblinfo = tk.Label(self.f3left, font=('aria', 15, 'bold'), text="Plan", fg="steel blue", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row = 13, column = 0)
		self.lblinfo = tk.Label(self.f3right, font=('aria', 15, 'bold'), text="5.000", fg="steel blue", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row = 15, column = 0)
		self.lblinfo = tk.Label(self.f3left, font=('aria', 15, 'bold'), text="Trân châu đen", fg="steel blue", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row = 14, column = 0)
		self.lblinfo = tk.Label(self.f3right, font=('aria', 15, 'bold'), text="5.000", fg="steel blue", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row = 16, column = 0)
		self.lblinfo = tk.Label(self.f3left, font=('aria', 15, 'bold'), text="Trân châu trắng", fg="steel blue", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row = 15, column = 0)
		self.lblinfo = tk.Label(self.f3right, font=('aria', 15, 'bold'), text="5.000", fg="steel blue", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row = 17, column = 0)
		self.lblinfo = tk.Label(self.f3left, font=('aria', 15, 'bold'), text="Trân châu hoàng kim", fg="steel blue", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row = 16, column = 0)
		self.lblinfo = tk.Label(self.f3right, font=('aria', 15, 'bold'), text="5.000", fg="steel blue", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row = 18, column = 0)
		self.lblinfo = tk.Label(self.f3left, font=('aria', 15, 'bold'), text="Thạch rau câu", fg="steel blue", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row = 17, column = 0)
		self.lblinfo = tk.Label(self.f3right, font=('aria', 15, 'bold'), text="5.000", fg="steel blue", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row = 19, column = 0)
		self.lblinfo = tk.Label(self.f3left, font=('aria', 15, 'bold'), text="Thạch thủy tinh", fg="steel blue", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row = 18, column = 0)
		self.lblinfo = tk.Label(self.f3right, font=('aria', 15, 'bold'), text="5.000", fg="steel blue", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row = 20, column = 0)


		#================================================================================
		#                       FRAME 2 Top
		# ================================================================================


		    
		self.lblMeal = tk.Label(self.f2Top,font=("arial",25,'bold'), text="TOPPING", bg = '#7BED9F')
		self.lblMeal.grid(row=0, column=0)

		self.lblinfo = tk.Label(self.f2Top, font=('aria', 15, 'bold'), text="\n_____________", fg="#7BED9F", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row=1, column=0)

		self.Plan = tk.Checkbutton(self.f2Top, text="Plan", variable=self.cPlan, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command= self.Plan_CB, bg = '#7BED9F')
		self.Plan.grid(row=2, column=0, sticky = W)
		self.txtPlan = tk.Entry(self.f2Top, font=("arial", 18, 'bold'), textvariable = self.varPlan, width=4, justify="right",state=DISABLED, bg = '#7BED9F')
		self.txtPlan.grid(row=2, column=1)

		self.TranChauDen = tk.Checkbutton(self.f2Top, text="Trân châu đen ", variable=self.cTranChauDen, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=self.TranChauDen_CB, bg = '#7BED9F')
		self.TranChauDen.grid(row=3, column=0, sticky = W)
		self.txtTranChauDen = tk.Entry(self.f2Top, font=("arial", 18, 'bold'), textvariable = self.varTranChauDen, width=4, justify="right",state=DISABLED, bg = '#7BED9F')
		self.txtTranChauDen.grid(row=3, column=1)

		self.TranChauTrang = tk.Checkbutton(self.f2Top, text="Trân châu trắng", variable=self.cTranChauTrang, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=self.TranChauTrang_CB, bg = '#7BED9F')
		self.TranChauTrang.grid(row=4, column=0, sticky = W)
		self.txtTranChauTrang = tk.Entry(self.f2Top, font=("arial", 18, 'bold'), textvariable = self.varTranChauTrang, width=4, justify="right",state=DISABLED, bg = '#7BED9F')
		self.txtTranChauTrang.grid(row=4, column=1)

		self.TranChauHoangKim = tk.Checkbutton(self.f2Top, text="Trân châu hoàng kim", variable=self.cTranChauHoangKim, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=self.TranChauHoangKim_CB, bg = '#7BED9F')
		self.TranChauHoangKim.grid(row=5, column=0, sticky = W)
		self.txtTranChauHoangKim = tk.Entry(self.f2Top, font=("arial", 18, 'bold'), textvariable = self.varTranChauHoangKim, width=4, justify="right",state=DISABLED, bg = '#7BED9F')
		self.txtTranChauHoangKim.grid(row=5, column=1)

		self.ThachRauCau = tk.Checkbutton(self.f2Top, text="Thạch rau câu ", variable=self.cThachRauCau, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=self.ThanhRauCau_CB, bg = '#7BED9F')
		self.ThachRauCau.grid(row=6, column=0, sticky = W)
		self.txtThachRauCau = tk.Entry(self.f2Top, font=("arial", 18, 'bold'), textvariable = self.varThachRauCau, width=4, justify="right",state=DISABLED, bg = '#7BED9F')
		self.txtThachRauCau.grid(row=6, column=1)

		self.ThachThuyTinh = tk.Checkbutton(self.f2Top, text="Thạch thủy tinh", variable=self.cThachThuyTinh, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=self.ThachThuyTinh_CB, bg = '#7BED9F')
		self.ThachThuyTinh.grid(row=7, column=0, sticky = W)
		self.txtThachThuyTinh = tk.Entry(self.f2Top, font=("arial", 18, 'bold'),  textvariable = self.varThachThuyTinh, width=4, justify="right",state=DISABLED, bg = '#7BED9F')
		self.txtThachThuyTinh.grid(row=7, column=1)

		self.lbn = tk.Label(self.f2Top, font =("arial", 18, 'bold'), text = "\n\n\n\n\n",  width=4, anchor='w', bg = '#7BED9F')
		self.lbn.grid(row = 8, column = 1)


		#================================================================================
		#                       FRAME 2 BOTTOM
		# ================================================================================



		self.lblPaymentMethod = tk.Label(self.f4, font=("arial", 18, 'bold'), text = "Payment Method", width=15, anchor='w', bg = '#7BED9F')
		self.lblPaymentMethod.grid(row=0,column=0)

		self.cmbPaymentMethod = ttk.Combobox(self.f4, textvariable=self.varPM, state="readonly", font=("arial", 10, 'bold'), width=10)
		self.cmbPaymentMethod['value']=('Cash','Paytm','Master Card','Visa Card','Debit Card')
		self.cmbPaymentMethod.current(0)
		self.cmbPaymentMethod.grid(row=0, column=1)

		self.lblTotal = tk.Label(self.f4, font=("arial", 18, 'bold'), text = "Total", width=8, anchor='e', bg = '#7BED9F')
		self.lblTotal.grid(row=2,column=0)
		self.txtTotal = tk.Entry(self.f4, font=("arial", 18, 'bold'), textvariable = self.varTotal, width=8, justify="right",state=DISABLED, bg = '#7BED9F')
		self.txtTotal.grid(row=2, column=1)

		self.lblVAT = tk.Label(self.f4, font=("arial", 18, 'bold'), text = "VAT @10%", width=8, anchor='e', bg = '#7BED9F')
		self.lblVAT.grid(row=3,column=0)
		self.txtVAT = tk.Entry(self.f4, font=("arial", 18, 'bold'),  textvariable = self.varVAT, width=8, justify="right",state=DISABLED, bg = '#7BED9F')
		self.txtVAT.grid(row = 3, column = 1)

		self.lblpay = tk.Label(self.f4, font=("arial", 18, 'bold'), text = "Total Payable\nAmount",width=15, anchor='e', bg = '#7BED9F')
		self.lblpay.grid(row=4, column=0)
		self.txtpay = tk.Entry(self.f4, font=("arial", 18, 'bold'),  textvariable = self.varPay, width=8, justify="right",state=DISABLED, bg = '#7BED9F')
		self.txtpay.grid(row=4, column=1)
		self.lbn = tk.Label(self.f4, font =("arial", 18, 'bold'), text = "\n\n\n\n",  width=4, anchor='w', bg = '#7BED9F')
		self.lbn.grid(row = 11, column = 1)

		#======================================================================================================================
		#                                     BUTTONS
		#======================================================================================================================
		#btnprice=Button(f2Bottom,padx=20,pady=1, bd=14 ,fg="black",font=('arial' ,16,'bold'),width=5, text="PRICE LIST", command = price_list)
		#btnprice.grid(row=2, column=0)

		self.btnTotal = tk.Button(self.f4, padx=20, pady=1, fg="black", font=("arial", 16, 'bold'), width=4,
							text="TOTAL", command = self.TotalCost, bg = '#7BED9F').grid(row=6, column=1)

		self.btnReset=tk.Button(self.f4,padx=20,pady=1,fg="black",font=('arial',16,'bold'),width=4,text="RESET", command=self.Reset, bg = '#7BED9F')
		self.btnReset.grid(row=7,column=1)

		self.btnReceipt = tk.Button(self.f4,padx=20,pady=1,fg="black",font=('arial',16,'bold'),width=4,text="RECEIPT", command=self.Receipt, bg = '#7BED9F')
		self.btnReceipt.grid(row = 8, column = 1)

		self.btnExit=tk.Button(self.f4,padx=20,pady=1,fg="black",font=('arial',16,'bold'),width=4,text="EXIT", command = self.iExit, bg = '#7BED9F')
		self.btnExit.grid(row=9,column=1)

		self.lbn =tk.Label(self.f4, font =("arial", 18, 'bold'), text = "\n",  width=4, anchor='w', bg = '#7BED9F')
		self.lbn.grid(row = 10, column = 1)



		#================================================================================
		#                       FRAME 3
		# ================================================================================

		self.lblDrinks = tk.Label(self.f1top,font=("arial",25,'bold'), text="DRINKS", bg = '#7BED9F')
		self.lblDrinks.grid(row=0, column=0)

		self.lblinfo = tk.Label(self.f1top, font=('aria', 15, 'bold'), text="\n_____________", fg="#7BED9F", anchor=W, bg = '#7BED9F')
		self.lblinfo.grid(row=1, column=0)

		self.TraChanh = tk.Checkbutton(self.f1top, text="Trà Chanh", variable=self.cTraChan, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command= self.TraChan_CB, bg = '#7BED9F')
		self.TraChanh.grid(row=2, column=0, sticky = W)
		self.txtTraChanh = tk.Entry(self.f1top, font=("arial", 18, 'bold'), textvariable = self.varTraChan, width=4, justify="right",state=DISABLED, bg = '#7BED9F')
		self.txtTraChanh.grid(row=2, column=1)

		self.NuocDua = tk.Checkbutton(self.f1top, text="Nước dừa", variable=self.cNuocDua, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=self.NuocDua_CB, bg = '#7BED9F')
		self.NuocDua.grid(row=3, column=0, sticky = W)
		self.txtNuocDua = tk.Entry(self.f1top, font=("arial", 18, 'bold'), textvariable = self.varNuocDua, width=4, justify="right",state=DISABLED, bg = '#7BED9F')
		self.txtNuocDua.grid(row=3, column=1)

		self.CaPheDa = tk.Checkbutton(self.f1top, text="Cà phê đá", variable=self.cCaPheDa, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=self.CaPheDa_CB, bg = '#7BED9F')
		self.CaPheDa.grid(row=4, column=0, sticky = W)
		self.txtCaPheDa = tk.Entry(self.f1top, font=("arial", 18, 'bold'), textvariable = self.varCaPheDa, width=4, justify="right",state=DISABLED, bg = '#7BED9F')
		self.txtCaPheDa.grid(row=4, column=1)

		self.CaPheSua = tk.Checkbutton(self.f1top, text="Cà phê sữa", variable=self.cCaPheSua, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=self.CaPheSua_CB, bg = '#7BED9F')
		self.CaPheSua.grid(row=5, column=0, sticky = W)
		self.txtCaPheSua = tk.Entry(self.f1top, font=("arial", 18, 'bold'),textvariable = self.varCaPheSua, width=4, justify="right",state=DISABLED, bg = '#7BED9F')
		self.txtCaPheSua.grid(row=5, column=1)

		self.NuocCam = tk.Checkbutton(self.f1top, text="Nước cam", variable=self.cNuocCam, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=self.NuocCam_CB, bg = '#7BED9F')
		self.NuocCam.grid(row=6, column=0, sticky = W)
		self.txtNuocCam = tk.Entry(self.f1top, font=("arial", 18, 'bold'),  textvariable = self.varNuocCam, width=4, justify="right",state=DISABLED, bg = '#7BED9F')
		self.txtNuocCam.grid(row=6, column=1)

		self.NuocSuoi = tk.Checkbutton(self.f1top, text="Nước Suối", variable=self.cNuocSuoi, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=self.NuocSuoi_CB, bg = '#7BED9F')
		self.NuocSuoi.grid(row=7, column=0, sticky = W)
		self.txtNuocSuoi = tk.Entry(self.f1top, font=("arial", 18, 'bold'),  textvariable = self.varNuocSuoi, width=4, justify="right",state=DISABLED, bg = '#7BED9F')
		self.txtNuocSuoi.grid(row=7, column=1)


		self.ChocolateDaXay = tk.Checkbutton(self.f1top, text="Chocolate đá xay", variable=self.cChocolateDaXay, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=self.ChocolaDaXay_CB, bg = '#7BED9F')
		self.ChocolateDaXay.grid(row=8, column=0, sticky = W)
		self.txtChocolateDaXay = tk.Entry(self.f1top, font=("arial", 18, 'bold'), textvariable = self.varChocolateDaXay, width=4, justify="right",state=DISABLED, bg = '#7BED9F')
		self.txtChocolateDaXay.grid(row=8, column=1)

		self.TraSuaSocola = tk.Checkbutton(self.f1top, text="Trà sữa sô-cô-la", variable=self.cTraSuaSocola, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=self.TraSuaSocola_CB, bg = '#7BED9F')
		self.TraSuaSocola.grid(row=9, column=0, sticky = W)
		self.txtTraSuaSocola = tk.Entry(self.f1top, font=("arial", 18, 'bold'),  textvariable = self.varTraSuaSocola, width=4, justify="right",state=DISABLED, bg = '#7BED9F')
		self.txtTraSuaSocola.grid(row=9, column=1)

		self.TraSuaThai = tk.Checkbutton(self.f1top, text="Trà sữa thái xanh", variable=self.cTraSuaThai, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=self.TraSuaThai_CB, bg = '#7BED9F')
		self.TraSuaThai.grid(row=10, column=0, sticky = W)
		self.txtTraSuaThai = tk.Entry(self.f1top, font=("arial", 18, 'bold'),  textvariable = self.varTraSuaThai, width=4, justify="right",state=DISABLED, bg = '#7BED9F')
		self.txtTraSuaThai.grid(row=10, column=1)

		self.NuocNgot = tk.Checkbutton(self.f1top, text="Nước ngọt các loại", variable=self.cNuocNgot, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=self.NuocNgot_CB, bg = '#7BED9F')
		self.NuocNgot.grid(row=11, column=0, sticky = W)
		self.txtNuocNgot = tk.Entry(self.f1top, font=("arial", 18, 'bold'), textvariable = self.varNuocNgot, width=4, justify="right",state=DISABLED, bg = '#7BED9F')
		self.txtNuocNgot.grid(row=11, column=1)
		self.root.mainloop()

		#lblSpace = Label(f3top,text="\n\n\n\n\n")
		#lblSpace.grid(row=11, column=0)
        #==============================================================================


    #================================================================================
	#                       BUTTON FUNCTIONS
	# ================================================================================

	#========================EXIT FUNCTION======================================
	def iExit(self):
		qExit = messagebox.askyesno("Restraunt Management","Do you want to quit ?")
		if qExit > 0:
			self.root.destroy()
			return 


	#========================RESET FUNCTION======================================

	def Reset(self):
		self.varTotal.set(0)
		self.varVAT.set(0)
		self.varPay.set(0)
		self.varTraChan.set(0)
		self.varNuocDua.set(0)
		self.varCaPheDa.set(0)
		self.varNuocCam.set(0)
		self.varNuocSuoi.set(0)
		self.varChocolateDaXay.set(0)
		self.varTraSuaSocola.set(0)
		self.varTraSuaThai.set(0)
		self.varCaPheSua.set(0)
		self.varNuocNgot.set(0)


		self.cPlan.set(0)
		self.cTranChauDen.set(0)
		self.cTranChauTrang.set(0)
		self.cTranChauHoangKim.set(0)
		self.cThachRauCau.set(0)
		self.cThachThuyTinh.set(0)
		self.cTraChan.set(0)
		self.cNuocDua.set(0)
		self.cCaPheDa.set(0)
		self.cNuocCam.set(0)
		self.cNuocSuoi.set(0)
		self.cChocolateDaXay.set(0)
		self.cTraSuaSocola.set(0)
		self.cTraSuaThai.set(0)
		self.cCaPheSua.set(0)
		self.cNuocNgot.set(0)

		self.varPlan.set(0)
		self.varTranChauDen.set(0)
		self.varTranChauTrang.set(0)
		self.varTranChauHoangKim.set(0)
		self.varThachRauCau.set(0)
		self.varThachThuyTinh.set(0)
		
		self.txtTotal.configure(state=DISABLED)
		self.txtVAT.configure(state=DISABLED)
		self.txtpay.configure(state=DISABLED)
		self.txtTraChanh.configure(state=DISABLED)
		self.txtCaPheDa.configure(state=DISABLED)
		self.txtNuocDua.configure(state=DISABLED)
		self.txtNuocCam.configure(state=DISABLED)
		self.txtNuocSuoi.configure(state=DISABLED)
		self.txtChocolateDaXay.configure(state=DISABLED)
		self.txtTraSuaSocola.configure(state=DISABLED)
		self.txtTraSuaThai.configure(state=DISABLED)
		self.txtCaPheSua.configure(state=DISABLED)
		self.txtNuocNgot.configure(state=DISABLED)
		self.txtTranChauDen.configure(state=DISABLED)
		self.txtTranChauTrang.configure(state=DISABLED)
		self.txtTranChauHoangKim.configure(state=DISABLED)
		self.txtThachRauCau.configure(state=DISABLED)
		self.txtPlan.configure(state=DISABLED)
		self.txtThachRauCau.configure(state=DISABLED)
		self.txtThachThuyTinh.configure(state=DISABLED)	       



	# ===============================================================
	#                       RECEIPT FUMCTION
	# ================================================================	    
	def Receipt(self):
		roor = Tk()
		roor.geometry("600x700+0+0")

		f1 = tk.Frame(roor, width = 1600, height = 700, bd = 12, relief = "raise", bg = '#7BED9F')
		f1.pack()
		lblReceipt = tk.Label(f1, font=('arial', 12, 'bold'), text="Receipt", bd=2, anchor='w', bg = '#7BED9F')
		lblReceipt.grid(row=0, column=0, sticky=W)
		txtReceipt = tk.Text(f1, width=64, height=35, bg="#7BED9F", bd=8, font=('arial', 11, 'bold'))
		txtReceipt.grid(row=1, column=0)
		txtReceipt.delete("1.0", END)
		x = random.randint(1000, 500890)
		randomRef = str(x)
		self.Receipt_Ref.set("BILL" + randomRef)

		txtReceipt.insert(END, 'Receipt Ref:\t\t\t'+ self.Receipt_Ref.get() + '\t\t\t' + self.DateofOrder.get()+"\n")
		txtReceipt.insert(END, 'Items\t\t\t\t' + "No. of Items \n\n")
		txtReceipt.insert(END, 'Tra Chanh: \t\t\t\t\t' + self.varTraChan.get() + "\n")
		txtReceipt.insert(END, 'Cà Phê Đá: \t\t\t\t\t' + self.varCaPheDa.get() + "\n")
		txtReceipt.insert(END, 'Cà Phê Sữa: \t\t\t\t\t' + self.varCaPheSua.get() + "\n")
		txtReceipt.insert(END, 'Nước Dừa: \t\t\t\t\t' + self.varNuocDua.get() + "\n")
		txtReceipt.insert(END, 'Nước Cam: \t\t\t\t\t' + self.varNuocCam.get() + "\n")
		txtReceipt.insert(END, 'Nước Suối: \t\t\t\t\t' + self.varNuocSuoi.get() + "\n")
		txtReceipt.insert(END, 'Chocolate Đá Xay: \t\t\t\t\t' + self.varChocolateDaXay.get() + "\n")
		txtReceipt.insert(END, 'Trà Sữa Sô-cô-la: \t\t\t\t\t' + self.varTraSuaSocola.get() + "\n")
		txtReceipt.insert(END, 'Trà Sữa Thái Xanh: \t\t\t\t\t' + self.varTraSuaThai.get() + "\n")
		txtReceipt.insert(END, 'Plan: \t\t\t\t\t' + self.varPlan.get() + "\n")
		txtReceipt.insert(END, 'Trân châu đen: \t\t\t\t\t' + self.varTranChauDen.get() + "\n")
		txtReceipt.insert(END, 'Trân châu trắng: \t\t\t\t\t' + self.varTranChauTrang.get() + "\n")
		txtReceipt.insert(END, 'Trân châu hoàng kim: \t\t\t\t\t' + self.varTranChauHoangKim.get() + "\n")
		txtReceipt.insert(END, 'Thạch rau câu: \t\t\t\t\t' + self.varThachRauCau.get() + "\n")
		txtReceipt.insert(END, 'Thạch thủy tinh: \t\t\t\t\t' + self.varThachThuyTinh.get() + "\n")
		txtReceipt.insert(END, '\nTotal Cost of Food: \t\t' + self.varTotal.get() + "\nVAT:\t\t" + self.varVAT.get()
							+"\nTotal Payble amount:\t\t" + self.varPay.get())
		name = ''
		if (str(self.varTraChan.get()) != '0'):
			name = 'Trà chanh'
			self.CTbill.AddCTBill(self.Receipt_Ref.get(),name,self.varTraChan.get())
		if (str(self.varCaPheDa.get()) != '0'):
			name =  'Cà phê đá'
			self.CTbill.AddCTBill(self.Receipt_Ref.get(),name,self.varCaPheDa.get())
		if (str(self.varCaPheSua.get()) != '0'):
			name =  'Cà phê sữa'
			self.CTbill.AddCTBill(self.Receipt_Ref.get(),name,self.varCaPheSua.get())
		if (str(self.varNuocDua.get()) != '0'):
			name =  'Nước dừa'
			self.CTbill.AddCTBill(self.Receipt_Ref.get(),name,self.varNuocDua.get())
		if (str(self.varNuocCam.get()) != '0'):
			name =  'Nước cam'
			self.CTbill.AddCTBill(self.Receipt_Ref.get(),name,self.varNuocCam.get())
		if (str(self.varNuocSuoi.get()) != '0'):
			name =  'Nước suối'
			self.CTbill.AddCTBill(self.Receipt_Ref.get(),name,self.varNuocSuoi.get())
		if (str(self.varChocolateDaXay.get()) != '0'):
			name =  'Chocolate đá xay'
			self.CTbill.AddCTBill(self.Receipt_Ref.get(),name,self.varChocolateDaXay.get())
		if (str(self.varTraSuaSocola.get()) != '0'):
			name =  'Trà sữa sô-cô-la'
			self.CTbill.AddCTBill(self.Receipt_Ref.get(),name,self.varTraSuaSocola.get())
		if (str(self.varTraSuaThai.get()) != '0'):
			name = 'Trà sữa thái xanh'
			self.CTbill.AddCTBill(self.Receipt_Ref.get(),name,self.varTraSuaThai.get())
		if (str(self.varNuocNgot.get()) != '0'):
			name = 'Nước ngọt'
			self.CTbill.AddCTBill(self.Receipt_Ref.get(),name,self.varNuocNgot.get())
		if (str(self.varPlan.get()) != '0'):
			name =  'Plan'
			self.CTbill.AddCTBill(self.Receipt_Ref.get(),name,self.varPlan.get())
		if (str(self.varTranChauDen.get()) != '0'):
			name = 'Trân châu đen'
			self.CTbill.AddCTBill(self.Receipt_Ref.get(),name,self.varTranChauDen.get())
		if (str(self.varTranChauTrang.get()) != '0'):
			name =  'Trân châu trắng'
			self.CTbill.AddCTBill(self.Receipt_Ref.get(),name,self.varTranChauTrang.get())
		if (str(self.varTranChauHoangKim.get()) != '0'):
			name = 'Trân châu hoàng kim'
			self.CTbill.AddCTBill(self.Receipt_Ref.get(),name,self.varTranChauHoangKim.get())
		if (str(self.varThachRauCau.get()) != '0'):
			name =  'Thạch rau câu'
			self.CTbill.AddCTBill(self.Receipt_Ref.get(),name,self.varThachRauCau.get())
		if (str(self.varThachThuyTinh.get()) != '0'):
			name =  'Thạch thủy tinh'
			self.CTbill.AddCTBill(self.Receipt_Ref.get(),name,self.varThachThuyTinh.get())
		self.bill.AddBill(self.DateofOrder.get(),self.varTotal.get(),self.Receipt_Ref.get())
		roor.mainloop()


	#================================================PRICE LIST=======================================

	# ===============================TOTAL FUNCTION===============================================
	def TotalCost(self):

		costPlan = float(self.varPlan.get())
		costTranChauDen = float(self.varTranChauDen.get())
		costTranChauTrang = float(self.varTranChauTrang.get())
		costTranChauHoangKim = float(self.varTranChauHoangKim.get())
		costThachRauCau = float(self.varThachRauCau.get())
		costThachThuyTinh = float(self.varThachThuyTinh.get())

		costTraChanh = float(self.varTraChan.get())
		costNuocDua = float(self.varNuocDua.get())
		costCaPhe = float(self.varCaPheDa.get())
		costNuocCam = float(self.varNuocCam.get())
		costNuocSuoi = float(self.varNuocSuoi.get())
		costChocolaDaXay = float(self.varChocolateDaXay.get())
		costTraSuaSocola = float(self.varTraSuaSocola.get())
		costTraSuaThai = float(self.varTraSuaThai.get())
		costCaPheSua = float(self.varCaPheSua.get())
		costNuocNgot = float(self.varNuocNgot.get())

		iTotal = ((costPlan + costTranChauDen + costTranChauTrang + costTranChauHoangKim + costThachRauCau + costThachThuyTinh)*5000 + (costTraChanh + costCaPhe)*20000
					+(costNuocDua + costCaPheSua + costNuocCam)*25000 + (costTraSuaSocola + costTraSuaThai + costChocolaDaXay) * 30000 + costNuocNgot*15000 + costNuocSuoi*10000)

		striTotal = str(iTotal)
		self.varTotal.set(striTotal)

		vat = (10/100)*iTotal
		strvat = str(vat)
		self.varVAT.set(vat)

		strPay =  str('%.2f'%(iTotal+vat))
		self.varPay.set(strPay)

	#================================================================================
	#                       CHECKBOX FUNCTION
	def Plan_CB(self):
		if self.cPlan.get() == 1:
			self.txtPlan.configure(state=NORMAL)
			self.varPlan.set("1")
		elif self.cPlan.get() == 0:
			self.txtPlan.configure(state=DISABLED)
			self.varPlan.set("0")
	def TranChauDen_CB(self):
		if self.cTranChauDen.get() == 1:
			self.txtTranChauDen.configure(state=NORMAL)
			self.varTranChauDen.set("1")
		elif self.cTranChauDen.get() == 0:
			self.txtTranChauDen.configure(state=DISABLED)
			self.varTranChauDen.set("0")
	def TranChauTrang_CB(self):
		if self.cTranChauTrang.get() == 1:
			self.txtTranChauTrang.configure(state=NORMAL)
			self.varTranChauTrang.set("1")
		elif self.cTranChauTrang.get() == 0:
			self.txtTranChauTrang.configure(state=DISABLED)
			self.varTranChauTrang.set("0")
	def TranChauHoangKim_CB(self):
		if self.cTranChauHoangKim.get() == 1:
			self.txtTranChauHoangKim.configure(state=NORMAL)
			self.varTranChauHoangKim.set("1")
		elif self.cTranChauHoangKim.get() == 0:
			self.txtTranChauHoangKim.configure(state=DISABLED)
			self.varTranChauHoangKim.set("0")
	def ThanhRauCau_CB(self):
		if self.cThachRauCau.get() == 1:
			self.txtThachRauCau.configure(state=NORMAL)
			self.varThachRauCau.set("1")
		elif self.cThachRauCau.get() == 0:
			self.txtThachRauCau.configure(state=DISABLED)
			self.varThachRauCau.set("0")
	def ThachThuyTinh_CB(self):
		if self.cThachThuyTinh.get() == 1:
			self.txtThachThuyTinh.configure(state=NORMAL)
			self.varThachThuyTinh.set("1")
		elif self.cThachThuyTinh.get() == 0:
			self.txtThachThuyTinh.configure(state=DISABLED)
			self.varThachThuyTinh.set("0")
	def TraChan_CB(self):
		if self.cTraChan.get() == 1:
			self.txtTraChanh.configure(state=NORMAL)
			self.varTraChan.set("1")
		elif self.cTraChan.get() == 0:
			self.txtTraChanh.configure(state=DISABLED)
			self.varTraChan.set("0")
			
	def NuocDua_CB(self):
		if self.cNuocDua.get() == 1:
			self.txtNuocDua.configure(state=NORMAL)
			self.varNuocDua.set("1")
		elif self.cNuocDua.get() == 0:
			self.txtNuocDua.configure(state=DISABLED)
			self.varNuocDua.set("0")
			
	def CaPheDa_CB(self):
		if self.cCaPheDa.get() == 1:
			self.txtCaPheDa.configure(state=NORMAL)
			self.varCaPheDa.set("1")
		elif self.cCaPheDa.get() == 0:
			self.txtCaPheDa.configure(state=DISABLED)
			self.varCaPheDa.set("0")
			
	def NuocCam_CB(self):
		if self.cNuocCam.get() == 1:
			self.txtNuocCam.configure(state=NORMAL)
			self.varNuocCam.set("1")
		elif self.cNuocCam.get() == 0:
			self.txtNuocCam.configure(state=DISABLED)
			self.varNuocCam.set("0")
			
	def NuocSuoi_CB(self):
		if self.cNuocSuoi.get() == 1:
			self.txtNuocSuoi.configure(state=NORMAL)
			self.varNuocSuoi.set("1")
		elif self.cNuocSuoi.get() == 0:
			self.txtNuocSuoi.configure(state=DISABLED)
			self.varNuocSuoi.set("0")
			
	def ChocolaDaXay_CB(self):
		if self.cChocolateDaXay.get() == 1:
			self.txtChocolateDaXay.configure(state=NORMAL)
			self.varChocolateDaXay.set("1")
		elif self.cChocolateDaXay.get() == 0:
			self.txtChocolateDaXay.configure(state=DISABLED)
			self.varChocolateDaXay.set("0")
			
	def TraSuaSocola_CB(self):
		if self.cTraSuaSocola.get() == 1:
			self.txtTraSuaSocola.configure(state=NORMAL)
			self.varTraSuaSocola.set("1")
		elif self.cTraSuaSocola.get() == 0:
			self.txtTraSuaSocola.configure(state=DISABLED)
			self.varTraSuaSocola.set("0")
			
	def TraSuaThai_CB(self):
		if self.cTraSuaThai.get() == 1:
			self.txtTraSuaThai.configure(state=NORMAL)
			self.varTraSuaThai.set("1")
		elif self.cTraSuaThai.get() == 0:
			self.txtTraSuaThai.configure(state=DISABLED)
			self.varTraSuaThai.set("0")

	def CaPheSua_CB(self):
		if self.cCaPheSua.get() == 1:
			self.txtCaPheSua.configure(state=NORMAL)
			self.varCaPheSua.set("1")
		elif self.cCaPheSua.get() == 0:
			self.txtCaPheSua.configure(state=DISABLED)
			self.varCaPheSua.set("0")

	def NuocNgot_CB(self):
		if self.cNuocNgot.get() == 1:
			self.txtNuocNgot.configure(state=NORMAL)
			self.varNuocNgot.set("1")
		elif self.cNuocNgot.get() == 0:
			self.txtNuocNgot.configure(state=DISABLED)
			self.varNuocNgot.set("0")