import sqlite3

def init_db():
    conn = sqlite3.connect('sales.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS sales
                      (date TEXT, product TEXT, quantity INTEGER, price REAL)''')
    conn.commit()
    conn.close()

def add_sale(date, product, quantity, price):
    conn = sqlite3.connect('sales.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sales (date, product, quantity, price) VALUES (?, ?, ?, ?)", 
                   (date, product, quantity, price))
    conn.commit()
    conn.close()

def get_sales():
    conn = sqlite3.connect('sales.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sales")
    sales = cursor.fetchall()
    conn.close()
    return sales
