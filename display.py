# Display on home screen dashboard (alignement, wrap)


from tkinter import ttk


# Function to wrap text
def wrap_text(text, length=25):
    return '\n'.join(text[i:i+length] for i in range(0, len(text), length))

# Function to adjust line height
def adjust_row_height(tree, products):
    max_lines = 1  # Minimum lines

    for product in products:
        description = wrap_text(product[2])  # Back to the line
        lines = description.count("\n") + 1  # Necessary lines
        max_lines = max(max_lines, lines)

    style = ttk.Style()
    style.configure("Treeview", rowheight=25 * max_lines)