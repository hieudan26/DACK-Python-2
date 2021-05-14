from os import environ
import matplotlib as mpl 
import matplotlib.pyplot as plt
from SQLBill import *
from matplotlib import colors as mcolors

class ShowSTatic():
    def __init__(self):
        self.crud = SQLBILL()
        self.suppress_qt_warnings()
        
    def display(self):
        DS = self.LayCacMonGiongNhau()
        self.DrawStatic(DS)

    def suppress_qt_warnings(self):# dùng để thiết lập môi trường để vẽ
        environ["QT_DEVICE_PIXEL_RATIO"] = "0"
        environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
        environ["QT_SCREEN_SCALE_FACTORS"] = "1"
        environ["QT_SCALE_FACTOR"] = "1"

    def LayCacMonGiongNhau(self):
        DS = self.crud.SoLuongMonTrongNgay()
        Listtemp = self.crud.LaytenMonAn() #List tên các món ăn ban đầu gồm list các tuple
        ListName = [] #List tên các món ăn đã được xử lý khoảng trông và tách ra khỏi tuple
        DSBD =[] #List chứa list ngày trong khaonr từ 1 -> 31(ngày bán được sản phẩm),  sản phảm, và  list số lượng sản phẩm tương ứng ngày 
        ResultArr= [] #List kết quả sau cùng ta có được gồm list chứa các list(thời gian chỉ có ngày,tên món,số lượng) bằng số ngày

        for item in Listtemp:
            ListName.append(item[0].strip())# xử lý lấy tên các món ăn ra

        for item in ListName:
            TempArrDate = []
            TempArrSL = []
            for item2 in DS:
                if(item == item2[1].strip()) :
                    TempArrDate.append(int(item2[0][0])*10 +int(item2[0][1]))#Lấy ra số ngày
                    TempArrSL.append(item2[2])#Lấy ra số lượng món ăn
            TempArr =[TempArrDate,TempArrSL,item]# gom lại thành danh sách
            DSBD.append(TempArr)

        for item in DSBD:
            TempArrDate = []
            TempArrSL = []
            for i in range(31):
                TempArrDate.append(i+1)#tạo danh sách ngày 1 -> 31
                TempArrSL.append(0)#tạo danh sách SL thức sản phẩm ban đầu là 0
            for j in range(len(item[0])):
                TempArrSL[item[0][j]] = item[1][j]#tạo thêm SL sản phẩm vào những ngày có sản phẩm đó được bán ra
            TempArr =[TempArrDate,TempArrSL,item[2]]#[ngày 1->31,SL sản phẩm, tên sản phẩm giống nhau]
            ResultArr.append(TempArr)#thêm vào list cuối cùng
        return ResultArr



    def DrawStatic(self,DS):
        self.fig, ax = plt.subplots()# khỏi tạo vẽ đường cong
        lines = []
        ax.set_title('Biểu đồ số lượng các món đã bán trong tháng của quán')#đặt tên
        for item in DS:
            line, = ax.plot(item[0], item[1], lw=2, label=item[2]) # vẽ đường thẳng với thông số đã cho trước với x là ngày và y số lượng label alf tên sản phẩm
            lines.append(line)# line,=  list = line = list[0]
        leg = ax.legend(fancybox=True, shadow=True)#hiển thị chú thích cho đồ thị
        self.lined = {}  
        for legline, origline in zip(leg.get_lines(), lines):#chuyển thành các tuple(các dòng chú thích cho từng đường cong,đường cong đồ thị )
            legline.set_picker(True) # khởi động chế độ cho phếm click
            self.lined[legline] = origline# tạo dictionary gồm các cặp dòng chú thích : đường biểu đồ
        self.fig.canvas.mpl_connect('pick_event', self.on_pick) #kết nối sự kiện click vào sẽ chạy vào hàm onpick
        plt.show()#hiển thị

    def on_pick(self,event):
        legline = event.artist # event vẽ
        origline = self.lined[legline]# lấy ra đường biểu đồ tương ứng
        visible = not origline.get_visible()# ẩn nếu chưa ẩn và hiện nếu đang ẩn
        origline.set_visible(visible)# set gia trị ẩn hiện cho đường biểu đồ
        legline.set_alpha(1.0 if visible else 0.2)# set gia trị ẩn hiện cho đường biểu đồ
        self.fig.canvas.draw()# vẽ lại
