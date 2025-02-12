import tkinter as tk
import tkinter.ttk as ttk

class PersonalInformation(tk.Frame):
    def __init__(self, connection, parent, controller, UserInfo=None):
        self.connection = connection
        # the parent is MainPage
        # the controller is PageController
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.UserInfo = UserInfo

        '''
        改這裡的val_
        '''
        self.val_name = ""
        self.val_username = ""
        self.val_password = ""
        self.val_email = ""

        self.personalInformationName = tk.Label(self, text='Name: '+self.val_name, font=('Arial', 15))
        self.personalInformationName.pack(anchor='w')
        self.personalInformationUsername = tk.Label(self, text='Username: '+self.val_username, font=('Arial', 15))
        self.personalInformationUsername.pack(anchor='w')
        self.personalInformationPassword = tk.Label(self, text='Password: '+self.val_password, font=('Arial', 15))
        self.personalInformationPassword.pack(anchor='w')
        self.personalInformationEmail = tk.Label(self, text='Email: '+self.val_email, font=('Arial', 15))
        self.personalInformationEmail.pack(anchor='w')

         # Schedule the update function to run every 0.1 seconds
        self.after(100, self.update_state)

    def update_state(self):        
        self.val_name = self.UserInfo.info.get("name", "")
        self.personalInformationName.config(text='Name: '+self.val_name)
        self.val_username = self.UserInfo.info.get("username", "")
        self.personalInformationUsername.config(text='Username: '+self.val_username)
        self.val_password = self.UserInfo.info.get("password", "")
        self.personalInformationPassword.config(text='Password: '+self.val_password)
        self.val_email = self.UserInfo.info.get("email_address", "")
        self.personalInformationEmail.config(text='Email: '+self.val_email)

        # Schedule the update function to run every 0.1 seconds
        self.after(100, self.update_state)

