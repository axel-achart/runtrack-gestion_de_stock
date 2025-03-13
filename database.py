# Connect with database 'store'


import mysql.connector


# Function to get product and category  from db
def get_products():
    conn = mysql.connector.connect(
        host = "localhost",
        user="root",
        password="mdp",
        database="store"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product")  
    product = cursor.fetchall()
    cursor.execute("SELECT * FROM category")  
    category = cursor.fetchall()

    cursor.close()
    conn.close()

    return product, category