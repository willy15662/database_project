import tkinter as tk
import tkinter.ttk as ttk
from search import Search
from history import History
from shortcut import Shortcut
from comment import Comment
from recommand import Recommand
from personalInformation import PersonalInformation

class MainPage(tk.Frame):
    def __init__(self, connection, parent, controller, UserInfo=None):        
        self.connection = connection
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.UserInfo = UserInfo

        #上面6個按鈕選擇功能
        self.mainPageFrameChanger = tk.Frame(self)
        self.mainPageButtonSearch = tk.Button(self.mainPageFrameChanger, text="Search", relief="solid", command=lambda: self.show_frame("Search"))
        self.mainPageButtonSearch.grid(row=0, column=0, padx=10)
        self.mainPageButtonHistory = tk.Button(self.mainPageFrameChanger, text="History", relief="solid", command=lambda: self.show_frame("History"))
        self.mainPageButtonHistory.grid(row=0, column=1, padx=10)
        self.mainPageButtonShortcut = tk.Button(self.mainPageFrameChanger, text="Shortcut", relief="solid", command=lambda: self.show_frame("Shortcut"))
        self.mainPageButtonShortcut.grid(row=0, column=2, padx=10)
        self.mainPageButtonComment = tk.Button(self.mainPageFrameChanger, text="comment", relief="solid", command=lambda: self.show_frame("Comment"))
        self.mainPageButtonComment.grid(row=1, column=0, padx=10, pady=10)
        self.mainPageButtonRecommand = tk.Button(self.mainPageFrameChanger, text="Recommend", relief="solid", command=lambda: self.show_frame("Recommand"))
        self.mainPageButtonRecommand.grid(row=1, column=1, padx=10, pady=10)
        self.mainPageButtonPersonalInformation = tk.Button(self.mainPageFrameChanger, text="Personal Information", relief="solid", command=lambda: self.show_frame("PersonalInformation"))
        self.mainPageButtonPersonalInformation.grid(row=1, column=2, padx=10, pady=10)
        # self.mainPageButtonTest = tk.Button(self.mainPageFrameChanger, text="test", relief="solid", command=lambda: print(self.UserInfo.info))
        # self.mainPageButtonTest.grid(row=2, column=0, padx=10, pady=10)
        self.mainPageFrameChanger.pack()

        #分隔線
        self.mainPageSeparateLine = ttk.Separator(self, orient='horizontal')
        self.mainPageSeparateLine.pack(fill='x')

        #下面function
        self.mainPageFrameFunction = tk.Frame(self)
        self.mainPageFrameFunction.pack(side="top", fill="both", expand=True)
        self.mainPageFrameFunction.grid_rowconfigure(0, weight=1)
        self.mainPageFrameFunction.grid_columnconfigure(0, weight=1)
        self.pages = {}
        
        for F in (Shortcut, Search, History, Comment, Recommand, PersonalInformation):
            if F.__name__ == "Recommand" or F.__name__ == "Search": frame = F(self.connection, parent=self.mainPageFrameFunction, controller=self, UserInfo=UserInfo, Shortcut=self.pages["Shortcut"])
            else: frame = F(self.connection, parent=self.mainPageFrameFunction, controller=self, UserInfo=UserInfo)
            self.pages[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("Search")

    def show_frame(self, page_name):        
        frame = self.pages[page_name]
        cursor = self.connection.cursor()
        if (page_name == "Comment"): 
            query = "SELECT * FROM comments WHERE customer_id=%s"
            id = self.UserInfo.info.get("customer_id", "")
            cursor.execute(query, (id,))
            result = cursor.fetchall()
            frame.customer_comment_list(result)
        elif (page_name == "Shortcut"): 
            cursor = self.connection.cursor()
            query = "SELECT DISTINCT keyword FROM shortcuts"
            cursor.execute(query)
            result = cursor.fetchall()
            keyword_list = []
            for i in range(len(result)):
                keyword = result[i].get('keyword', '')
                keyword_list.append(keyword)
            frame.shortcutFrameCombobox['values'] = keyword_list
                  
            # if frame.categories == {}:
            query = "SELECT * FROM shortcuts WHERE customer_id=%s"
            id = self.UserInfo.info.get("customer_id", "")
            cursor.execute(query, (id,))
            result = cursor.fetchall()
            for i in range(len(result)):
                keyword = result[i].get('keyword', '')
                restaurant_id = result[i].get('restaurant_id', '')
                if keyword not in frame.categories:
                    frame.categories[keyword] = []                        
                if restaurant_id not in frame.categories[keyword]:
                    frame.categories[keyword].append(restaurant_id)
            frame.show_shortcut('favorite') # default page            
                
        elif (page_name == "History"): 
            query = "SELECT * FROM history WHERE customer_id=%s"
            id = self.UserInfo.info.get("customer_id", "")
            cursor.execute(query, (id,))
            result = cursor.fetchall()
            frame.restuaurant_history_list(result)

        cursor.close()
        frame.tkraise()
        