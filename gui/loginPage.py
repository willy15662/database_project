import tkinter as tk
import tkinter.ttk as ttk
from db import login

class LoginPage(tk.Frame):
    def __init__(self, connection, parent, controller, UserInfo=None):
        self.connection = connection
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.loginPageFrame = tk.Frame(self)
        self.UserInfo = UserInfo  # self.userInfo is a UserInfo object shared by all pages

        # Tittle
        self.loginPageTitle = tk.Label(self, text='Dine Finder', font=('Arial', 18))
        self.loginPageTitle.pack()

        # Combobox for comsumer or owner
        self.loginPageCombobox = ttk.Combobox(self)
        self.loginPageCombobox['values'] = ['Customer', 'Owner']
        self.loginPageCombobox.pack(pady=10)
        self.loginPageCombobox.current(0)

        self.loginPageFrame.pack()

        # Username and password entry
        self.loginPageUsernameText = tk.Label(self.loginPageFrame, text='Username:', font=('Arial', 12))
        self.loginPageUsernameText.grid(row=0, column=0)
        self.loginPageUsernameEntry = tk.Entry(self.loginPageFrame)
        self.loginPageUsernameEntry.grid(row=0, column=1)

        self.loginPagePasswordText = tk.Label(self.loginPageFrame, text='Password:', font=('Arial', 12))
        self.loginPagePasswordText.grid(row=1, column=0)
        self.loginPagePasswordEntry = tk.Entry(self.loginPageFrame, show='*')
        self.loginPagePasswordEntry.grid(row=1, column=1)

        self.loginPageButton = tk.Button(self, text='Login', command=lambda: self.login_to_Main_Page())
        self.loginPageButton.pack()
    

    '''
    更改此function,self.loginPageUsernameEntry和self.loginPagePasswordEntry為兩個entry bar,
    使用self.controller.show_frame("MainPage")可以切換到主畫面,
    需要更改if的條件
    '''
    def login_to_Main_Page(self):
        #獲得帳號密碼和身分(Customer/Owner)
        username = self.loginPageUsernameEntry.get()
        password = self.loginPagePasswordEntry.get()
        identity = self.loginPageCombobox.get()
        if identity == 'Customer':
            # userInfo is a dictionary with keys: username, password, email, name
            userInfo = login(username, password, "customers_account", self.connection) 
            if userInfo:
                # demo account: username: 123, password: 123
                self.UserInfo.info = userInfo
                self.controller.show_frame("MainPage")
        else:
            userInfo = login(username, password, "owner_account", self.connection)
            if userInfo:
                # demo account: username: 1234, password: 1234
                self.UserInfo.info = userInfo
                self.controller.show_frame("OwnerMain")
