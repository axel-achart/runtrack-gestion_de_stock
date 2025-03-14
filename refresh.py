import tkinter as tk
import mysql.connector

class StockManager:
    def __init__(self, product_tree):
        self.product_tree = product_tree

    def refresh_table(self):
        for row in self.product_tree.get_children():
            self.product_tree.delete(row)
        
        conn = mysql.connector.connect(host="localhost", user="root", password="@testsql", database="store")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM product")
        products = cursor.fetchall()
        conn.close()
        
        for product in products:
            self.product_tree.insert("", tk.END, values=product)