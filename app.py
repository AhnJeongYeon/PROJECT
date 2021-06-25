from flask import Flask , render_template, redirect , request
import sqlite3
import pandas as pd
conn = sqlite3.connect("lib.db", isolation_level=None)

c = conn.cursor()
app = Flask(__name__)
app.debug = True


@app.route('/', methods = ['GET', 'POST'])
def book():
    if request.method == 'POST':
        query =  "INSERT INTO `Ratings` VALUES (?,?,?);"
        book = int(request.form['book'])
        rating = int(request.form['rating'])
        member = request.form['member']
        data_list = [book, rating, member]
        c.execute(query,data_list)
        print(book, rating , member)

        return "SUCCESS"
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000)