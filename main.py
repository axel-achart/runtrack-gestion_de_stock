# Main file


from config import *
import tkinter as tk 
import tkinter.font
from tkinter import ttk
from database import *
from display import *
from back import *


# Main Function
def main():
    # Initialisation
    screen = tk.Tk()
    screen.title("Store Dashboard")
    screen.geometry(WINDOW_SIZE)
    screen.configure(bg=BACKGROUND)

    FONT = tkinter.font.Font(family=family_font, size=size_font, weight=weight_font)
    TITLE_FONT = tkinter.font.Font(family=family_font, size=title_size_font, weight=weight_font)

    # Title in window
    title_label = tk.Label(screen, text="Dashboard", font=TITLE_FONT)
    title_label.pack(pady=10)

    main_frame = tk.Frame(screen)
    main_frame.pack(fill="both", expand=True)

    # Box of Products in stock
    left_frame = tk.Frame(main_frame, width=600, bg=SND_BACKGROUND)
    left_frame.pack(side="left", fill="y")

    stock_label = tk.Label(left_frame, text="Produits en stock", font=FONT, bg=SND_BACKGROUND)
    stock_label.pack(pady=10)

    # Treeview for visualisation in table
    columns = ("ID", "Name", "Description", "Price", "Quantity", "ID_Category")
    product_tree = ttk.Treeview(left_frame, columns=columns, show="headings")
    product_tree.pack(padx=10, pady=5)

    # Title of columns
    for col in columns:
        product_tree.heading(col, text=col)
        product_tree.column(col, width=160, anchor="center")


    products, categories = get_products()


    # Fill table with products
    for product in products:
        product = list(product)
        product[2] = wrap_text(product[2])
        product_tree.insert("", tk.END, values=product)

    adjust_row_height(product_tree, products)


    # Right Frame for Buttons
    right_frame = tk.Frame(main_frame, bg=BACKGROUND)
    right_frame.pack(side="right", fill="both", expand=True)


    # Buttons in Right Frame
    add_button = tk.Button(right_frame, text="Add", command=add, font=FONT)
    add_button.pack(pady=30)

    del_button = tk.Button(right_frame, text="Delete", command=remove, font=FONT)
    del_button.pack(pady=30)

    edit_button = tk.Button(right_frame, text="Edit", command=edit, font=FONT)
    edit_button.pack(pady=30)

    # Tkinter Loop
    screen.mainloop()




if __name__ == "__main__":
    main()