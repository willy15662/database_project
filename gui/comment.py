import tkinter as tk
import tkinter.ttk as ttk
from db import select_all_by_id

class Comment(tk.Frame):
    def __init__(self, connection, parent, controller, UserInfo=None):    
        self.connection = connection    
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.UserInfo = UserInfo

        #餐廳: 評論
        self.searchSpecificFrameCommentFrame = tk.Frame(self)

        self.searchSpecificFrameCommentFrameScrollbar = tk.Scrollbar(self.searchSpecificFrameCommentFrame)
        self.searchSpecificFrameCommentFrameScrollbar.pack(side='right', fill='y')
        self.searchSpecificFrameCanvas = tk.Canvas(self.searchSpecificFrameCommentFrame, yscrollcommand=self.searchSpecificFrameCommentFrameScrollbar.set)
        self.searchSpecificFrameCanvas.pack(fill="y", expand=True)
        self.searchSpecificFrameCommentFrameScrollbar.config(command=self.searchSpecificFrameCanvas.yview)
        self.searchSpecificFrameCommentFrameCommentFrame = tk.Frame(self.searchSpecificFrameCanvas)
        self.searchSpecificFrameCanvas.create_window((0, 0), window=self.searchSpecificFrameCommentFrameCommentFrame)
        self.searchSpecificFrameCommentFrameCommentFrame.bind("<Configure>", self.onFrameConfigureC)
        self.comments = {}
        self.searchSpecificFrameCommentFrame.pack(expand=True, fill='both')

        #不須改動
    def onFrameConfigureC(self, event):
        self.searchSpecificFrameCanvas.configure(scrollregion=self.searchSpecificFrameCanvas.bbox("all"))

    '''
    更改此function,對應到評論
    '''
    def customer_comment_list(self, result=None):
        # self.comments = result
        for widget in self.searchSpecificFrameCommentFrameCommentFrame.winfo_children():  # 每次都先清空
            widget.destroy()
        for i in range(len(result)):
            comment_text = self.UserInfo.info.get('name', '') #name
            rating =  result[i].get('rating', 0) #rating
            response = result[i].get('store_response', '') #content
            cursor = self.connection.cursor()

            query = "SELECT store_name FROM restaurant WHERE restaurant_id=%s"
            content = result[i].get('content', '')
            restaurant_id = result[i].get('restaurant_id', '')
            cursor.execute(query, (restaurant_id,))            
            restuarant = cursor.fetchone().get('store_name', '')
            temp = tk.LabelFrame(self.searchSpecificFrameCommentFrameCommentFrame, text=comment_text)
            tk.Label(temp, text='                                                                                                      ').pack() #寬度需要
            tk.Label(temp, text=restuarant).pack()
            tk.Label(temp, text= str(rating) + '/5.0').pack()
            tk.Label(temp, text=content).pack()
            tk.Label(temp, text='Restuarant response: '+response).pack()
            temp.pack(fill='x', expand=True)

    