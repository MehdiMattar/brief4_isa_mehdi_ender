from flask import Flask, render_template
from flask import send_from_directory
import sqlite3

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("simple_page.html")

@app.route("/table/<name>")
def sql_table(name):
    print(name)
    db_path = "data.db"
    connexion = sqlite3.connect(db_path)
    cursor = connexion.cursor()
    cursor.execute(f"SELECT * FROM {name} limit 50")
    result = cursor.fetchall()
    if name == "customer":
        colonlist = ("id", "country")
    elif name == "customer_order":
        colonlist = ("id", "invoice_nb", "invoice_date", "customer_id")
    elif name == "order_detail":
        colonlist = ("id", "quantity", "order_id", "product_id")   
    elif name == "product":
        colonlist = ("id", "description", "price")   
    else:
        colonlist = []  
    return render_template("simple_page.html",name=name,result=result,colonlist=colonlist)

@app.route("/table/all") 
def sql_table2():
    print("all")
    db_path = "data.db"
    connexion = sqlite3.connect(db_path)
    cursor = connexion.cursor()
    cursor.execute("""SELECT * FROM customer as t1 
                   INNER JOIN customer_order as t2 ON t1.id = t2.customer_id
                   INNER JOIN order_detail as t3 ON t2.id = t3.order_id
                   INNER JOIN product as t4 ON t4.id = t3.product_id
                   LIMIT 50""")
    result = cursor.fetchall()
    colonlist = ("id", "country","id", "invoice_nb", "invoice_date", "customer_id","id","quantity", "order_id", "product_id","id","description", "price")
    return render_template("simple_page.html",result=result,colonlist=colonlist)