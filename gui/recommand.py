import tkinter as tk
import tkinter.ttk as ttk
import db
from datetime import datetime

class Recommand(tk.Frame):
    def __init__(self, connection, parent, controller, UserInfo=None, Shortcut=None):
        self.Shortcut = Shortcut
        self.connection = connection    
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.UserInfo = UserInfo
        #初始化
        self.val_store_name = ''
        self.val_rating = ''
        self.val_type = ''
        self.val_price_range = ''
        self.val_address = ''
        self.val_phone = ''
        self.val_introduction = ''
        self.val_website = ''
        self.val_delivery_platform = ''
        self.val_restuarant_list = []

        #Search bar
        self.searchFrameSreachBar = tk.Frame(self)
        self.searchFrameSreachBarButton = tk.Button(self.searchFrameSreachBar, text="Recommand", command=lambda:self.recommand_the_restuaurant(), relief='solid')
        self.searchFrameSreachBarButton.grid(row=0, column=3, pady=5)

        self.searchFrameSreachBarType = tk.Label(self.searchFrameSreachBar, text="Type:")
        self.searchFrameSreachBarType.grid(row=1, column=0, padx=5)
        self.searchFrameSreachBarTypeCombobox = ttk.Combobox(self.searchFrameSreachBar)
        self.searchFrameSreachBarTypeCombobox['value'] = ["None","Japanese", "Steak", "Italian", "Vegetarian", "Seafood", "Chinese", "Dessert", "Fast Food", "Mexican", "Thai"]
        self.searchFrameSreachBarTypeCombobox.current(0)
        self.searchFrameSreachBarTypeCombobox.grid(row=1, column=1, padx=5)

        self.searchFrameSreachBarPrice = tk.Label(self.searchFrameSreachBar, text="Price:")
        self.searchFrameSreachBarPrice.grid(row=1, column=2, padx=5)
        self.searchFrameSreachBarPriceCombobox = ttk.Combobox(self.searchFrameSreachBar)
        self.searchFrameSreachBarPriceCombobox['value'] = ['None','$','$$','$$$','$$$$']
        self.searchFrameSreachBarPriceCombobox.current(0)
        self.searchFrameSreachBarPriceCombobox.grid(row=1, column=3, padx=5)

        self.searchFrameSreachBarAddress = tk.Label(self.searchFrameSreachBar, text="Address:")
        self.searchFrameSreachBarAddress.grid(row=1, column=4, padx=5)
        self.searchFrameSreachBarAddressCityCombobox = ttk.Combobox(self.searchFrameSreachBar)
        self.searchFrameSreachBarAddressCityCombobox['value'] = ['None','Taipei','Taichung']
        self.searchFrameSreachBarAddressCityCombobox.current(0)
        self.searchFrameSreachBarAddressCityCombobox.grid(row=1, column=5, padx=5)
        self.searchFrameSreachBarAddressDistrictCombobox = ttk.Combobox(self.searchFrameSreachBar)
        self.searchFrameSreachBarAddressDistrictCombobox['value'] = ['None','Eastern District','West District','North District','South District']
        self.searchFrameSreachBarAddressDistrictCombobox.current(0)
        self.searchFrameSreachBarAddressDistrictCombobox.grid(row=1, column=6, padx=5)
        self.searchFrameSreachBar.pack()


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
        self.searchSpecificFrameAddShortcut = tk.Button(self.searchSpecificFrameFunction, text='Shortcut', relief='solid', command=lambda:self.change_function(3), font=('Arial', 15))
        self.searchSpecificFrameAddShortcut.grid(row=0, column=4, padx=5, pady=3)
        self.searchSpecificFrameFunction.pack()
        self.searchSpecificSeparateLine = ttk.Separator(self.searchSpecificFrame, orient='horizontal')
        self.searchSpecificSeparateLine.pack(fill='x', pady=5)

        #餐廳: 資訊
        self.searchSpecificFrameInformationFrame = tk.Frame(self.searchSpecificFrame)
        self.searchSpecificStoreName = tk.Label(self.searchSpecificFrameInformationFrame, font=('Arial', 15))
        self.searchSpecificStoreName.pack(anchor='w', pady=5, padx=10)
        self.searchSpecificRating = tk.Label(self.searchSpecificFrameInformationFrame, font=('Arial', 15))
        self.searchSpecificRating.pack(anchor='w', pady=5, padx=10)
        self.searchSpecificType = tk.Label(self.searchSpecificFrameInformationFrame, font=('Arial', 15))
        self.searchSpecificType.pack(anchor='w', pady=5, padx=10)
        self.searchSpecificPriceRange = tk.Label(self.searchSpecificFrameInformationFrame, font=('Arial', 15))
        self.searchSpecificPriceRange.pack(anchor='w', pady=5, padx=10)
        self.searchSpecificAddress = tk.Label(self.searchSpecificFrameInformationFrame, font=('Arial', 15))
        self.searchSpecificAddress.pack(anchor='w', pady=5, padx=10)
        self.searchSpecificPhone = tk.Label(self.searchSpecificFrameInformationFrame, font=('Arial', 15))
        self.searchSpecificPhone.pack(anchor='w', pady=5, padx=10)
        self.searchSpecificIntroduction = tk.Label(self.searchSpecificFrameInformationFrame, font=('Arial', 15))
        self.searchSpecificIntroduction.pack(anchor='w', pady=5, padx=10)
        self.searchSpecificWebsite = tk.Label(self.searchSpecificFrameInformationFrame, font=('Arial', 15))
        self.searchSpecificWebsite.pack(anchor='w', pady=5, padx=10)
        self.searchSpecificDeliveryPlatform = tk.Label(self.searchSpecificFrameInformationFrame, font=('Arial', 15))
        self.searchSpecificDeliveryPlatform.pack(anchor='w', pady=5, padx=10)
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
        self.searchSpecificFrameCommentFrameAddCommentContentL = tk.Label(self.searchSpecificFrameCommentFrameAddCommentFrame, text='Please leave your comment: ', font=('Arial', 15))
        self.searchSpecificFrameCommentFrameAddCommentContentL.grid(row=0, column=0)
        self.searchSpecificFrameCommentFrameAddCommentContent = tk.Entry(self.searchSpecificFrameCommentFrameAddCommentFrame)
        self.searchSpecificFrameCommentFrameAddCommentContent.grid(row=0, column=1)
        self.searchSpecificFrameCommentFrameAddCommentRatingL = tk.Label(self.searchSpecificFrameCommentFrameAddCommentFrame, text='Rating(0.0~5.0): ', font=('Arial', 15))
        self.searchSpecificFrameCommentFrameAddCommentRatingL.grid(row=1, column=0)
        self.searchSpecificFrameCommentFrameAddCommentRating = ttk.Entry(self.searchSpecificFrameCommentFrameAddCommentFrame)
        self.searchSpecificFrameCommentFrameAddCommentRating.grid(row=1,column=1)
        self.searchSpecificFrameCommentFrameAddCommentButton = tk.Button(self.searchSpecificFrameCommentFrameAddCommentFrame, relief='solid', font=('Arial', 10), text='Add New Comment', command=lambda:self.add_to_comment())
        self.searchSpecificFrameCommentFrameAddCommentButton.grid(row=2, column=1)
        self.searchSpecificFrameCommentFrameAddCommentFrame.pack(pady=10)
        self.searchSpecificFrameCommentFrameScrollbar = tk.Scrollbar(self.searchSpecificFrameCommentFrame)
        self.searchSpecificFrameCommentFrameScrollbar.pack(side='right', fill='y')
        self.searchSpecificFrameCanvas = tk.Canvas(self.searchSpecificFrameCommentFrame, yscrollcommand=self.searchSpecificFrameCommentFrameScrollbar.set)
        self.searchSpecificFrameCanvas.pack(fill="y", expand=True)
        self.searchSpecificFrameCommentFrameScrollbar.config(command=self.searchSpecificFrameCanvas.yview)
        self.searchSpecificFrameCommentFrameCommentFrame = tk.Frame(self.searchSpecificFrameCanvas)
        self.searchSpecificFrameCanvas.create_window((0, 0), window=self.searchSpecificFrameCommentFrameCommentFrame)
        self.searchSpecificFrameCommentFrameCommentFrame.bind("<Configure>", self.onFrameConfigureC)

        #餐廳: 加入我的最愛
        self.searchSpecificFrameShortcutFrame = tk.Frame(self.searchSpecificFrame)
        self.searchSpecificFrameShortcutFrameKeywordL = tk.Label(self.searchSpecificFrameShortcutFrame, font=('Arial', 10), text='Keyword(Add to the same shortcut if the keywords are the same):')
        self.searchSpecificFrameShortcutFrameKeywordL.grid(row=0, column=0)
        self.searchSpecificFrameShortcutFrameKeyword = tk.Entry(self.searchSpecificFrameShortcutFrame)
        self.searchSpecificFrameShortcutFrameKeyword.grid(row=0, column=1)
        self.searchSpecificFrameShortcutFrameAddButton = tk.Button(self.searchSpecificFrameShortcutFrame, font=('Arial', 10), text='Add', command=lambda:self.add_to_shortcut())
        self.searchSpecificFrameShortcutFrameAddButton.grid(row=1, column=1)

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
    顯示餐廳資訊
    更改此function,val_對應到餐廳的各種資訊
    '''
    def to_the_restuarant(self, restaurant_id, resInfo, rating):
        self.restaurant_id = restaurant_id
        self.searchRestuaurantFrame.pack_forget()
        self.searchSpecificFrame.pack(fill='both', expand=True)
        self.val_store_name = resInfo.get("store_name", "")
        self.val_rating = rating
        self.val_type = resInfo.get("tag", "")
        self.val_price_range = resInfo.get("price_range", "")
        self.val_address = resInfo.get("address", "")
        self.val_phone = resInfo.get("phone", "")
        self.val_introduction = resInfo.get("introductione", "")
        self.val_website = resInfo.get("official_website", "")
        self.val_delivery_platform = resInfo.get("delivery_platform", "")

        query = "INSERT INTO history (customer_id, search_time, restaurant_id) VALUES (%s, %s, %s)"
        uid = self.UserInfo.info.get('customer_id', '')
        timestamp_value = datetime.now()
        cursor = self.connection.cursor()
        cursor.execute(query, (uid, timestamp_value, restaurant_id,))
        self.connection.commit()
        cursor.close()

        # 更新 Label 
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
            self.searchSpecificFrameShortcutFrame.pack_forget()
            self.searchSpecificFrameMenuFrame.pack_forget()
        elif index == 2:
            self.restuaurant_comment_list()
            self.searchSpecificFrameCommentFrame.pack(fill='both', expand=True)
            self.searchSpecificFrameInformationFrame.pack_forget()
            self.searchSpecificFrameShortcutFrame.pack_forget()
            self.searchSpecificFrameMenuFrame.pack_forget()
        elif index == 4:
            self.restuaurant_menu_list()
            self.searchSpecificFrameMenuFrame.pack()
            self.searchSpecificFrameInformationFrame.pack_forget()
            self.searchSpecificFrameCommentFrame.pack_forget()
            self.searchSpecificFrameShortcutFrame.pack_forget()
        else:
            self.searchSpecificFrameShortcutFrame.pack(side='top')
            self.searchSpecificFrameInformationFrame.pack_forget()
            self.searchSpecificFrameCommentFrame.pack_forget()
            self.searchSpecificFrameMenuFrame.pack_forget()

    '''
    更改此function,對應到評論
    '''
    def restuaurant_comment_list(self):
        cursor = self.connection.cursor()
        query = "SELECT customer_id, content, rating, store_response FROM comments WHERE restaurant_id=%s"
        cursor.execute(query, (self.restaurant_id,))
        result = cursor.fetchall()
        for widget in self.searchSpecificFrameCommentFrameCommentFrame.winfo_children(): # 每次都先清空
            widget.destroy()
        for i in range(len(result)):
            customer_id = result[i].get('customer_id', 0)
            query_cid = "SELECT name FROM customers_account WHERE customer_id=%s"
            cursor.execute(query_cid, (customer_id,))            
            comment_text =  cursor.fetchone().get('name', '')  #name
            content = result[i].get('content', '')
            rating = result[i].get('rating', 0) #rating
            response = result[i].get('store_response', '') #content
            temp = tk.LabelFrame(self.searchSpecificFrameCommentFrameCommentFrame, text=comment_text)
            tk.Label(temp, text='                                                                                                      ').pack() #寬度需要
            tk.Label(temp, text= str(rating)[:3] + '/5.0').pack()
            tk.Label(temp, text=content).pack()
            tk.Label(temp, text='Restuarant response: '+response).pack()
            temp.pack(fill='x', expand=True)
    '''
    更改次function,新增shortcuut
    '''
    def add_to_shortcut(self):
        keyword = self.searchSpecificFrameShortcutFrameKeyword.get()
        cid = self.UserInfo.info.get('customer_id', '') 
        cursor = self.connection.cursor()
        query = "INSERT INTO shortcuts (customer_id, keyword, restaurant_id) VALUES (%s, %s, %s)"
        cursor.execute(query, (cid, keyword, self.restaurant_id,))
        self.connection.commit()
        cursor.close()

        if keyword.lower() not in self.Shortcut.categories:
            self.Shortcut.categories[keyword.lower()] = []
        self.Shortcut.categories[keyword.lower()].append(self.restaurant_id)

    '''
    更改次function,新增comment
    '''
    def add_to_comment(self):
        content = self.searchSpecificFrameCommentFrameAddCommentContent.get()
        rating = self.searchSpecificFrameCommentFrameAddCommentRating.get()
        cid = self.UserInfo.info.get('customer_id', '') #name
        cursor = self.connection.cursor()
        query = "INSERT INTO comments (customer_id, restaurant_id, rating, content) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (int(cid), self.restaurant_id, float(rating), content,))
        self.restuaurant_comment_list()
        self.connection.commit()
        cursor.close()
    '''
    更改次function,對應到菜單
    '''
    def restuaurant_menu_list(self):
        cursor = self.connection.cursor()
        query = "SELECT price, dish_name FROM menus WHERE restaurant_id=%s"
        cursor.execute(query, (self.restaurant_id,))
        result = cursor.fetchall()
        for widget in self.searchSpecificFrameMenuFrameMenuFrame.winfo_children():  # 每次都先清空
            widget.destroy()
        for i in range(len(result)):
            dish_name = result[i].get('dish_name', '')
            price = str(result[i].get('price', 0)) + ' NTD'
            tk.Label(self.searchSpecificFrameMenuFrameMenuFrame, text='                                                                                                      ').pack() #寬度需要
            tk.Label(self.searchSpecificFrameMenuFrameMenuFrame, text=dish_name).pack()
            tk.Label(self.searchSpecificFrameMenuFrameMenuFrame, text=price).pack()
            ttk.Separator(self.searchSpecificFrameMenuFrameMenuFrame, orient='horizontal').pack(fill='x')
    '''
    更改此function,按下推薦時顯示隨機推薦餐廳(看要顯示幾項)
    '''
    def recommand_the_restuaurant(self):
        search_type = self.searchFrameSreachBarTypeCombobox.get()
        search_price = self.searchFrameSreachBarPriceCombobox.get()
        search_address = self.searchFrameSreachBarAddressCityCombobox.get()
        search_addressdistrict = self.searchFrameSreachBarAddressDistrictCombobox.get().split()[0]
        # 添加餐廳列表
        resInfoList = db.find_restaurant(search_type, search_price, search_address, "restaurant",self.connection) 
        for widget in self.searchRestuaurantButtonFrame.winfo_children():  # 每次都先清空
            widget.destroy()
        for resInfo in resInfoList:
            if search_addressdistrict != "None" and search_addressdistrict not in resInfo.get("address", ""):
                continue
            restaurant_id = resInfo.get("restaurant_id", "")
            commInfolist = db.select_all_by_resid(self.connection, restaurant_id, "comments")
            rating, i= 0, 0
            for commInfo in commInfolist:
                rating += float(commInfo.get("rating", ""))
                i+=1
            rating = rating / i
            rating = round(rating, 1)
            self.val_store_name = resInfo.get("store_name", "")
            self.val_price_range = resInfo.get("price_range", "")
            self.val_address = resInfo.get("address", "")
            button_text = self.val_store_name + '\n' + self.val_price_range  +'   '+ str(rating) + '/5.0 ' + '\n' + self.val_address
            tk.Button(self.searchRestuaurantButtonFrame, text=button_text, relief='solid', anchor='w', width=50, height=3, 
                      command=lambda id=restaurant_id, res = resInfo, rat=rating: self.to_the_restuarant(id, res, str(rat))).pack(pady=5, fill='x', expand=True)
        self.searchRestuaurantFrame.pack(fill='both', expand=True)