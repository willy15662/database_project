# 餐廳搜尋與管理系統

## 目錄
- [專案介紹](#專案介紹)
- [系統架構](#系統架構)
- [環境需求](#環境需求)
- [安裝與執行](#安裝與執行)
- [檔案結構](#檔案結構)
- [功能說明](#功能說明)
- [Tkinter 基礎](#tkinter-基礎)

## 專案介紹
本專案為一個使用 Tkinter 建立的餐廳搜尋與管理系統，包含顧客與店主的登入功能、餐廳搜尋、歷史紀錄、快捷選單、評論與推薦功能。

## 系統架構
- 透過 `pageController.py` 控制頁面切換
- 使用 `UserInfo` 類別來管理使用者資訊
- 提供多種顧客與店主相關功能，包括搜尋、評論、推薦、菜單管理等

## 檔案結構
```
restaurant-management/
│── pageController.py       # 負責頁面切換 (無須修改)
│── loginPage.py            # 登入頁面 (需修改 login_to_Main_Page())
│── mainPage.py             # 控制顧客功能 (無須修改)
│── search.py               # 搜尋與餐廳功能 (多個函數需修改)
│── history.py              # 瀏覽紀錄 (多個函數需修改)
│── shortcut.py             # 快捷功能 (多個函數需修改)
│── comment.py              # 評論管理 (需修改 customer_comment_list())
│── recommend.py            # 餐廳推薦 (多個函數需修改)
│── personalInformation.py  # 個人資訊管理 (可修改個人資料)
│── ownerMain.py            # 店主管理 (多個函數需修改)
└── README.md               # 專案說明文件
```
![image](https://github.com/user-attachments/assets/27fb33dd-9657-4fa4-9da7-ebd8ed4d295d)

## 功能說明
### 1. 登入 (`loginPage.py`)
- `login_to_Main_Page()`: 根據身份驗證帳號密碼後登入

### 2. 搜尋 (`search.py`)
- `search_the_restuarant()`: 搜尋餐廳並顯示列表
- `to_the_restuarant()`: 更新餐廳資訊
- `restuaurant_comment_list()`: 更新餐廳評論
- `restuaurant_menu_list()`: 更新餐廳菜單
- `add_to_shortcut()`: 新增快捷方式
- `add_to_comment()`: 新增評論

### 3. 瀏覽紀錄 (`history.py`)
- 修改 `for` 迴圈以添加瀏覽紀錄
- `to_the_restuarant()`, `restuaurant_comment_list()`, `add_to_shortcut()`, `add_to_comment()`: 需修改

### 4. 快捷 (`shortcut.py`)
- 修改 `for` 迴圈以添加快捷餐廳
- `to_the_restuarant()`, `restuaurant_comment_list()`, `restuaurant_menu_list()`, `add_to_shortcut()`, `add_to_comment()`: 需修改
- `combobox_selected()`: 依不同快捷選項更新餐廳列表

### 5. 評論 (`comment.py`)
- `customer_comment_list()`: 顯示顧客評論

### 6. 推薦 (`recommend.py`)
- `recommand_the_restuaurant()`: 顯示推薦餐廳 (需修改)
- 其他與 `search.py` 相同的函數需修改

### 7. 個人資訊 (`personalInformation.py`)
- 可修改個人資訊

### 8. 店主管理 (`ownerMain.py`)
- `add_the_restuaurant()`: 顯示店主擁有的餐廳 (僅顯示一間)
- `to_the_restuarant()`, `restuaurant_comment_list()`, `restuaurant_menu_list()`: 需修改
- `send_the_response()`: 發送評論回覆
- `change_the_menu()`: 更改菜單
- `change_restuarant_inforamtion()`: 更新餐廳資訊

## Tkinter 基礎
### 1. 元件
- **Label**: 文字標籤
- **Button**: 按鈕 (`command=lambda: function()`) 可觸發事件
- **Entry**: 輸入框 (`.get()` 取得內容)
- **Combobox**: 下拉選單 (`.get()` 取得選擇內容)

### 2. 元件定位
- `pack()`: 依序排列元件
- `grid(column, row)`: 使用網格擺放元件

