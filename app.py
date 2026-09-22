from flask import Flask, render_template
import sqlite3
from sqlite3 import Error
app = Flask(__name__)
DATABASE = "data"


def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
    return None

@app.route('/')
def hello_world():  # put application's code here
    query ="SELECT name, sail_number, wooden_boat, place, gold_fleet FROM data_table"
    con = create_connection(DATABASE)
    cur = con.cursor()
    cur.execute(query)
    data_list = cur.fetchall()
    con.close()
    print(data_list)

    return render_template("index.html", data_set = data_list)


if __name__ == '__main__':
    app.run()
