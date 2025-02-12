# execute this page
import tkinter as tk
from loginPage import LoginPage
from mainPage import MainPage
from ownerMain import OwnerMain
import ctypes
from db import connect_to_db

class UserInfo():    
    # UserInfo is a object shared by all pages
    def __init__(self):
        # key: customer_id/owner_id, username, password, email, name
        self.info = {}

class PageController(tk.Tk):    

    def __init__(self):
        self.connection = connect_to_db() 
        
        # ... 其餘的初始化代碼 ...
        tk.Tk.__init__(self)

        self.UserInfo = UserInfo() # self.userInfo is a UserInfo object shared by all pages

        #下面三行解決解析度問題
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
        ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
        self.tk.call('tk', 'scaling', ScaleFactor/75)

        self.title('Dine Finder')
        self.geometry('2000x1050')
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.pages = {}
        for F in (LoginPage, MainPage, OwnerMain):  # 添加其他頁面類
            frame = F(self.connection, parent=self.container, controller=self, UserInfo=self.UserInfo)
            self.pages[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # self.shared_data = {}  # 用於頁面間共享數據
        self.show_frame("LoginPage")
        

    def show_frame(self, page_name):
        frame = self.pages[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = PageController()
    app.mainloop()

app.connection.close() # *** 記得關閉連線 *** #