import tkinter as tk
import tkinter.ttk as ttk

class OwnerMain(tk.Frame):
    def __init__(self, connection, parent, controller, UserInfo=None):
        self.connection = connection
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.UserInfo = UserInfo

        #下方餐廳列表
        self.searchRestuaurantFrame = tk.Frame(self)
        self.searchRestuaurantFrameScrollbar = tk.Scrollbar(self.searchRestuaurantFrame)
        self.searchRestuaurantFrameScrollbar.pack(side='right', fill='y')
        self.searchCanvas = tk.Canvas(self.searchRestuaurantFrame, yscrollcommand=self.searchRestuaurantFrameScrollbar.set)
        self.searchCanvas.pack(fill="y", expand=True)
        self.searchRestuaurantFrameScrollbar.config(command=self.searchCanvas.yview)
        self.searchRestuaurantButtonFrame = tk.Frame(self.searchCanvas)
        self.searchCanvas.create_window((0, 0), window=self.searchRestuaurantButtonFrame)
        self.searchRestuaurantButtonFrame.bind("<Configure>", self.onFrameConfigure)
        self.add_the_restuaurant()
        self.searchRestuaurantFrame.pack(fill='both', expand=True)

        #餐廳: 上方功能按鈕
        self.searchSpecificFrame = tk.Frame(self)
        self.searchSpecificFrameFunction = tk.Frame(self.searchSpecificFrame)
        self.searchSpecificFrameReturn = tk.Button(self.searchSpecificFrameFunction, text='Return', command=lambda:self.back_to_the_list(), relief='solid', font=('Arial', 15))
        self.searchSpecificFrameReturn.grid(row=0, column=0, padx=5, pady=3)
        self.searchSpecificFrameInformation = tk.Button(self.searchSpecificFrameFunction, text='Information', relief='solid', command=lambda:self.change_function(1), font=('Arial', 15))
        self.searchSpecificFrameInformation.grid(row=0, column=1, padx=5, pady=3)
        self.searchSpecificFrameMenu = tk.Button(self.searchSpecificFrameFunction, text='Menu', relief='solid', command=lambda:self.change_function(4), font=('Arial', 15))
        self.searchSpecificFrameMenu.grid(row=0, column=2, padx=5, pady=3)
        self.searchSpecificFrameComment = tk.Button(self.searchSpecificFrameFunction, text='Comment', relief='solid', command=lambda:self.change_function(2), font=('Arial', 15))
        self.searchSpecificFrameComment.grid(row=0, column=3, padx=5, pady=3)
        self.searchSpecificFrameFunction.pack()
        self.searchSpecificSeparateLine = ttk.Separator(self.searchSpecificFrame, orient='horizontal')
        self.searchSpecificSeparateLine.pack(fill='x', pady=5)

        #餐廳: 資訊
        self.searchSpecificFrameInformationFrame = tk.Frame(self.searchSpecificFrame)
        self.searchSpecificStoreName = tk.Label(self.searchSpecificFrameInformationFrame, font=('Arial', 15))
        self.searchSpecificStoreName.grid(row=0, column=0, sticky='w')
        self.searchSpecificStoreNameEntry = tk.Entry(self.searchSpecificFrameInformationFrame)
        self.searchSpecificStoreNameEntry.grid(row=0, column=1, sticky='w')
        self.searchSpecificRating = tk.Label(self.searchSpecificFrameInformationFrame, font=('Arial', 15))
        self.searchSpecificRating.grid(row=1, column=0, sticky='w')
        self.searchSpecificType = tk.Label(self.searchSpecificFrameInformationFrame, font=('Arial', 15))
        self.searchSpecificType.grid(row=2, column=0, sticky='w')
        self.searchSpecificTypeEntry = tk.Entry(self.searchSpecificFrameInformationFrame)
        self.searchSpecificTypeEntry.grid(row=2, column=1, sticky='w')
        self.searchSpecificPriceRange = tk.Label(self.searchSpecificFrameInformationFrame, font=('Arial', 15))
        self.searchSpecificPriceRange.grid(row=3, column=0, sticky='w')
        self.searchSpecificPriceRangeEntry = tk.Entry(self.searchSpecificFrameInformationFrame)
        self.searchSpecificPriceRangeEntry.grid(row=3, column=1, sticky='w')
        self.searchSpecificAddress = tk.Label(self.searchSpecificFrameInformationFrame, font=('Arial', 15))
        self.searchSpecificAddress.grid(row=4, column=0, sticky='w')
        self.searchSpecificAddressEntry = tk.Entry(self.searchSpecificFrameInformationFrame)
        self.searchSpecificAddressEntry.grid(row=4, column=1, sticky='w')
        self.searchSpecificPhone = tk.Label(self.searchSpecificFrameInformationFrame, font=('Arial', 15))
        self.searchSpecificPhone.grid(row=5, column=0, sticky='w')
        self.searchSpecificPhoneEntry = tk.Entry(self.searchSpecificFrameInformationFrame)
        self.searchSpecificPhoneEntry.grid(row=5, column=1, sticky='w')
        self.searchSpecificIntroduction = tk.Label(self.searchSpecificFrameInformationFrame, font=('Arial', 15))
        self.searchSpecificIntroduction.grid(row=6, column=0, sticky='w')
        self.searchSpecificIntroductionEntry = tk.Entry(self.searchSpecificFrameInformationFrame)
        self.searchSpecificIntroductionEntry.grid(row=6, column=1, sticky='w')
        self.searchSpecificWebsite = tk.Label(self.searchSpecificFrameInformationFrame, font=('Arial', 15))
        self.searchSpecificWebsite.grid(row=7, column=0, sticky='w')
        self.searchSpecificWebsiteEntry = tk.Entry(self.searchSpecificFrameInformationFrame)
        self.searchSpecificWebsiteEntry.grid(row=7, column=1, sticky='w')
        self.searchSpecificDeliveryPlatform = tk.Label(self.searchSpecificFrameInformationFrame, font=('Arial', 15))
        self.searchSpecificDeliveryPlatform.grid(row=8, column=0, sticky='w')
        self.searchSpecificDeliveryPlatformEntry = tk.Entry(self.searchSpecificFrameInformationFrame)
        self.searchSpecificDeliveryPlatformEntry.grid(row=8, column=1, sticky='w')
        self.searchSpecificSaveButton = tk.Button(self.searchSpecificFrameInformationFrame, text="Save", font=('Arial', 15), command=lambda:self.change_restuarant_inforamtion())
        self.searchSpecificSaveButton.grid(row=9, column=1, sticky='w')
        self.searchSpecificFrameInformationFrame.pack(fill='x')

        #餐廳: 菜單
        self.searchSpecificFrameMenuFrame = tk.Frame(self.searchSpecificFrame)
        self.searchSpecificFrameMenuFrameScrollbar = tk.Scrollbar(self.searchSpecificFrameMenuFrame)
        self.searchSpecificFrameMenuFrameScrollbar.pack(side='right', fill='y')
        self.searchSpecificFrameMenuFrameCanvas = tk.Canvas(self.searchSpecificFrameMenuFrame, yscrollcommand=self.searchSpecificFrameMenuFrameScrollbar.set)
        self.searchSpecificFrameMenuFrameCanvas.pack(fill="y", expand=True)
        self.searchSpecificFrameMenuFrameScrollbar.config(command=self.searchSpecificFrameMenuFrameCanvas.yview)
        self.searchSpecificFrameMenuFrameMenuFrame = tk.Frame(self.searchSpecificFrameMenuFrameCanvas)
        self.searchSpecificFrameMenuFrameCanvas.create_window((0, 0), window=self.searchSpecificFrameMenuFrameMenuFrame)
        self.searchSpecificFrameMenuFrameMenuFrame.bind("<Configure>", self.onFrameConfigureM)

        #餐廳: 評論
        self.searchSpecificFrameCommentFrame = tk.Frame(self.searchSpecificFrame)
        self.searchSpecificFrameCommentFrameAddCommentFrame = tk.Frame(self.searchSpecificFrameCommentFrame)
        self.searchSpecificFrameCommentFrameAddCommentFrame.pack(pady=10)
        self.searchSpecificFrameCommentFrameScrollbar = tk.Scrollbar(self.searchSpecificFrameCommentFrame)
        self.searchSpecificFrameCommentFrameScrollbar.pack(side='right', fill='y')
        self.searchSpecificFrameCanvas = tk.Canvas(self.searchSpecificFrameCommentFrame, yscrollcommand=self.searchSpecificFrameCommentFrameScrollbar.set)
        self.searchSpecificFrameCanvas.pack(fill="y", expand=True)
        self.searchSpecificFrameCommentFrameScrollbar.config(command=self.searchSpecificFrameCanvas.yview)
        self.searchSpecificFrameCommentFrameCommentFrame = tk.Frame(self.searchSpecificFrameCanvas)
        self.searchSpecificFrameCanvas.create_window((0, 0), window=self.searchSpecificFrameCommentFrameCommentFrame)
        self.searchSpecificFrameCommentFrameCommentFrame.bind("<Configure>", self.onFrameConfigureC)


        self.searchSpecificFrame.pack_forget()
    #不須改動
    def onFrameConfigure(self, event):
        # 更新滾動區域
        self.searchCanvas.configure(scrollregion=self.searchCanvas.bbox("all"))
    #不須改動
    def onFrameConfigureC(self, event):
        self.searchSpecificFrameCanvas.configure(scrollregion=self.searchSpecificFrameCanvas.bbox("all"))
    
    def onFrameConfigureM(self, event):
        self.searchSpecificFrameMenuFrameCanvas.configure(scrollregion=self.searchSpecificFrameMenuFrameCanvas.bbox("all"))

    '''
    用來顯示owner擁有的餐廳列表,
    更改此function,
    '''
    def add_the_restuaurant(self):
        # 添加餐廳列表
        tk.Button(self.searchRestuaurantButtonFrame, text="Add New Restuarant", relief='solid', anchor='w', width=50, height=3, command=lambda:self.to_the_restuarant()).pack(pady=5, fill='x', expand=True)
        for i in range(50):
            button_text = 'Mcdonald\'s ' + '\n$$ ' + '4.0/5.0 ' + '\nTaichung,' + 'North District' + 'Qfas Road'
            tk.Button(self.searchRestuaurantButtonFrame, text=button_text, relief='solid', anchor='w', width=50, height=3, command=lambda:self.to_the_restuarant()).pack(pady=5, fill='x', expand=True)

    '''
    顯示餐廳資訊
    更改此function,val_對應到餐廳的各種資訊
    '''
    def to_the_restuarant(self):
        self.searchRestuaurantFrame.pack_forget()
        self.searchSpecificFrame.pack(fill='both', expand=True)
        self.val_store_name = 'Mcdonald\'s'
        self.val_rating = '4.0'
        self.val_type = 'Fast Food'
        self.val_price_range = '$$'
        self.val_address = 'Taichung, North District, Qfas Road'
        self.val_phone = '0411111111'
        self.val_introduction = 'Welcome'
        self.val_website = 'http://www.mc.com'
        self.val_delivery_platform = 'ubereats'
         # 更新 Label 文本
        self.searchSpecificStoreName.config(text='Store name: '+self.val_store_name)
        self.searchSpecificRating.config(text='Score: '+self.val_rating+'/5.0')
        self.searchSpecificType.config(text='Type: '+self.val_type)
        self.searchSpecificPriceRange.config(text='Price range: '+self.val_price_range)
        self.searchSpecificAddress.config(text='Address: '+self.val_address)
        self.searchSpecificPhone.config(text='Phone: '+self.val_phone)
        self.searchSpecificIntroduction.config(text='Introduction: '+self.val_introduction)
        self.searchSpecificWebsite.config(text='Website: '+self.val_website)
        self.searchSpecificDeliveryPlatform.config(text='Delivery Platform: '+self.val_delivery_platform)

    #不須改動
    def back_to_the_list(self):
        self.change_function(1)
        self.searchRestuaurantFrame.pack(fill='both', expand=True)
        self.searchSpecificFrame.pack_forget()
    #不須改動
    def change_function(self, index):
        if index == 1:
            self.searchSpecificFrameInformationFrame.pack(fill='x')
            self.searchSpecificFrameCommentFrame.pack_forget()
            self.searchSpecificFrameMenuFrame.pack_forget()
        elif index == 2:
            self.restuaurant_comment_list()
            self.searchSpecificFrameCommentFrame.pack(fill='both', expand=True)
            self.searchSpecificFrameInformationFrame.pack_forget()
            self.searchSpecificFrameMenuFrame.pack_forget()
        elif index == 4:
            self.restuaurant_menu_list()
            self.searchSpecificFrameMenuFrame.pack()
            self.searchSpecificFrameInformationFrame.pack_forget()
            self.searchSpecificFrameCommentFrame.pack_forget()



    '''
    更改此function,對應到評論
    '''
    def restuaurant_comment_list(self):
        for i in range(30):
            comment_text = 'Johnson' #name
            rating = '4.5' #rating
            response = 'Thanks for your comment' #content
            temp = tk.LabelFrame(self.searchSpecificFrameCommentFrameCommentFrame, text=comment_text)
            tk.Label(temp, text='                                                                                                      ').pack() #寬度需要
            tk.Label(temp, text= rating + '/5.0').pack()
            tk.Label(temp, text='Good').pack()
            tk.Label(temp, text='Restuarant response: '+response).pack()
            self.x=tk.Entry(temp).pack(pady=5)
            tk.Button(temp, text="Response", relief='solid', command=lambda:self.send_the_response(self.x.get())).pack()
            temp.pack(fill='x', expand=True)
    '''
    更改此function,更新owner對comment的回覆
    '''
    def send_the_response(self, response):
        print(response)

    '''
    更改此function,對應到菜單
    '''
    def restuaurant_menu_list(self):
        for i in range(30):
            dish_name='Burger'
            price='140'
            tk.Label(self.searchSpecificFrameMenuFrameMenuFrame, text='                                                                                                      ').pack() #寬度需要
            tk.Label(self.searchSpecificFrameMenuFrameMenuFrame, text=dish_name).pack()
            tk.Label(self.searchSpecificFrameMenuFrameMenuFrame, text=price).pack()
            self.name = tk.Entry(self.searchSpecificFrameMenuFrameMenuFrame).pack()
            self.price = tk.Entry(self.searchSpecificFrameMenuFrameMenuFrame).pack()
            tk.Button(self.searchSpecificFrameMenuFrameMenuFrame, text="Save", relief='solid', command=lambda:self.send_the_response(self.name.get(), self.price.get())).pack()
            ttk.Separator(self.searchSpecificFrameMenuFrameMenuFrame, orient='horizontal').pack(fill='x')
    '''
    更改此function,用於新增菜單
    '''
    def change_the_menu(seld, name, price):
        print(name)

    '''
    需修改,此function用來更新餐廳基本資料,
    下方更新label需加入if條件因為可能沒有更改導致賦值為空
    '''
    def change_restuarant_inforamtion(self):
        self.val_store_name = self.searchSpecificStoreNameEntry.get()
        self.val_type = self.searchSpecificTypeEntry.get()
        self.val_price_range = self.searchSpecificPriceRangeEntry.get()
        self.val_address = self.searchSpecificAddressEntry.get()
        self.val_phone = self.searchSpecificPhoneEntry.get()
        self.val_introduction = self.searchSpecificIntroductionEntry.get()
        self.val_website = self.searchSpecificWebsiteEntry.get()
        self.val_delivery_platform = self.searchSpecificDeliveryPlatformEntry.get()
         # 更新 Label 文本
        self.searchSpecificStoreName.config(text='Store name: '+self.val_store_name)
        self.searchSpecificType.config(text='Type: '+self.val_type)
        self.searchSpecificPriceRange.config(text='Price range: '+self.val_price_range)
        self.searchSpecificAddress.config(text='Address: '+self.val_address)
        self.searchSpecificPhone.config(text='Phone: '+self.val_phone)
        self.searchSpecificIntroduction.config(text='Introduction: '+self.val_introduction)
        self.searchSpecificWebsite.config(text='Website: '+self.val_website)
        self.searchSpecificDeliveryPlatform.config(text='Delivery Platform: '+self.val_delivery_platform)