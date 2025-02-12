import pymysql
from tkinter import messagebox
from pymysql.cursors import DictCursor

def connect_to_db():
    db_settings = {
        ### 必須的基本資料
        "user": "root", # 當初安裝mysql時設的帳密，不是customers_account或owner_account的username和password
        "password": "1234",  
        "host": "127.0.0.1",
        "database": "dinefinder",
        "port": 3306,
        "read_timeout": 5,
        "cursorclass": DictCursor, # 以 dict 型別返回查詢結果，而不是 tuple 型別
    }

    try: 
        connection = pymysql.connect(**db_settings)
        return connection

    except pymysql.Error as e:
        messagebox.showerror("Error", f"Error connecting to the database: {e}")

def login(username, password, table_name, connection):    

    cursor = connection.cursor()        
    if (table_name == "customers_account"):
        query = "SELECT * FROM customers_account WHERE username=%s AND password=%s"
    elif (table_name == "owner_account"):
        query = "SELECT * FROM owner_account WHERE username=%s AND password=%s"
    else:
        raise Exception("Error: Invalid table name.")
    cursor.execute(query, (username, password,))

    result = cursor.fetchone()
    if result:
        # messagebox.showinfo("Login", "Login Successful!")
        print("Login successful!")
        print(f"Welcome {result['username']}!")
    else:
        messagebox.showinfo("Failed", "Login Failed! Please check your username and password.")
        print("Login failed.")
    return result

def select_all_by_id(connection, id, table_name):
    cursor = connection.cursor()
    if (table_name == "comments"):
        query = "SELECT * FROM comments WHERE customer_id=%s"
    cursor.execute(query, (id,))
    result = cursor.fetchall()
    return result

def select_history_by_id(connection, id, table_name):
    cursor = connection.cursor()
    if (table_name == "history"):
        query = "SELECT * FROM history WHERE customer_id=%s"
    cursor.execute(query, (id,))
    result = cursor.fetchall()
    return result

def select_all_by_resid(connection, id, table_name):
    cursor = connection.cursor()
    if (table_name == "comments"):
        query = "SELECT * FROM comments WHERE restaurant_id=%s"
    cursor.execute(query, (id,))
    result = cursor.fetchall()
    return result

def find_one_restaurant(connection, id, table_name):
    cursor = connection.cursor()
    if (table_name == "restaurant"):
        query = "SELECT * FROM restaurant WHERE restaurant_id=%s"
    cursor.execute(query, (id,))
    result = cursor.fetchone()
    return result

def find_restaurant(type, price, address, table_name, connection): 
    cursor = connection.cursor()
    if table_name == "restaurant":

        if(address != 'None') :
            address = '%'+ address + '%'

        query = "SELECT * FROM restaurant where (tag=%s OR 'None'=%s) and (price_range=%s OR 'None'=%s) and (address LIKE %s OR 'None'=%s)"

        cursor.execute(query, (type, type, price, price, address, address))
        
    result_res = cursor.fetchall()
    return result_res

def select_menu_by_resid(connection, id, table_name):
    cursor = connection.cursor()
    if (table_name == "menus"):
        query = "SELECT * FROM menus WHERE restaurant_id=%s"
    cursor.execute(query, (id,))
    result = cursor.fetchall()
    return result