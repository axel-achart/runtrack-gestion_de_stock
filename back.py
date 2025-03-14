import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

class AddProductWindow:
    def __init__(self, parent, manager):
        self.manager = manager
        self.add_win = tk.Toplevel(parent)
        self.add_win.title("Ajouter un produit")
        
        self.fields = ["Nom", "Description", "Prix", "Quantité", "ID Catégorie"]
        self.entries = {}
        
        for i, field in enumerate(self.fields):
            tk.Label(self.add_win, text=field).grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(self.add_win)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries[field] = entry
        
        tk.Button(self.add_win, text="Ajouter", command=self.add_product).grid(row=len(self.fields), columnspan=2, pady=10)
    
    def add_product(self):
        values = {key: entry.get() for key, entry in self.entries.items()}
        
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="@testsql", database="store")
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO product (name, description, price, quantity, id_category)
                VALUES (%s, %s, %s, %s, %s)
            """, (values["Nom"], values["Description"], values["Prix"], values["Quantité"], values["ID Catégorie"]))
            conn.commit()
            conn.close()
            self.manager.refresh_table()
            self.add_win.destroy()
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

class RemoveProductWindow:
    def __init__(self, parent, manager):
        self.manager = manager
        self.remove_win = tk.Toplevel(parent)
        self.remove_win.title("Supprimer un produit")
        
        tk.Label(self.remove_win, text="ID du produit").grid(row=0, column=0, padx=10, pady=5)
        self.entry_id = tk.Entry(self.remove_win)
        self.entry_id.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Button(self.remove_win, text="Supprimer", command=self.remove_product).grid(row=1, columnspan=2, pady=10)
    
    def remove_product(self):
        product_id = self.entry_id.get()
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="@testsql", database="store")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM product WHERE id = %s", (product_id,))
            conn.commit()
            conn.close()
            self.manager.refresh_table()
            self.remove_win.destroy()
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

class EditProductWindow:
    def __init__(self, parent, manager):
        self.manager = manager
        self.edit_win = tk.Toplevel(parent)
        self.edit_win.title("Modifier un produit")
        
        tk.Label(self.edit_win, text="ID du produit").grid(row=0, column=0, padx=10, pady=5)
        self.entry_id = tk.Entry(self.edit_win)
        self.entry_id.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(self.edit_win, text="Champ à modifier").grid(row=1, column=0, padx=10, pady=5)
        self.field_var = tk.StringVar()
        self.field_dropdown = ttk.Combobox(self.edit_win, textvariable=self.field_var, values=["name", "description", "price", "quantity", "id_category"])
        self.field_dropdown.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(self.edit_win, text="Nouvelle valeur").grid(row=2, column=0, padx=10, pady=5)
        self.entry_value = tk.Entry(self.edit_win)
        self.entry_value.grid(row=2, column=1, padx=10, pady=5)
        
        tk.Button(self.edit_win, text="Modifier", command=self.edit_product).grid(row=3, columnspan=2, pady=10)
    
    def edit_product(self):
        product_id = self.entry_id.get()
        field = self.field_var.get()
        new_value = self.entry_value.get()
        
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="@testsql", database="store")
            cursor = conn.cursor()
            query = f"UPDATE product SET {field} = %s WHERE id = %s"
            cursor.execute(query, (new_value, product_id))
            conn.commit()
            conn.close()
            self.manager.refresh_table()
            self.edit_win.destroy()
        except Exception as e:
            messagebox.showerror("Erreur", str(e))
