from flask import Flask, render_template
import psycopg2

### Make the flask app
app = Flask(__name__)
app.static_folder = 'static'

### Functions
def debug(s):
    """Prints a message to the screen (not web browser) 
    if FLASK_DEBUG is set."""
    if app.config['DEBUG']:
        print(s)

def get_db():
    return psycopg2.connect(
    host="localhost",
    database="Pizza_flask",
    port=5433,
    user="testuser",
    password="1234"
    )

conn = get_db()
cursor = conn.cursor()

### Routes
@app.route("/pizza", methods=['get', 'post'])
@app.route("/", methods=['get', 'post'])
def pizza_page():
    cursor.execute('select image_link, dish_name, dish_description, price, ingredients, toppings from pizza')
    rowlist = cursor.fetchall()
    print(rowlist);
    return render_template('assets/index.html', data=rowlist)

@app.route("/sushi", methods=['get', 'post'])
def sushi_page():
    cursor.execute('select image_link, dish_name, dish_description, price, ingredients, toppings from sushi')
    rowlist = cursor.fetchall()
    print(rowlist);
    return render_template('assets/index.html', data=rowlist)

@app.route("/drinks", methods=['get', 'post'])
def drinks_page():
    cursor.execute('select image_link, dish_name, dish_description, price, ingredients, toppings from drink')
    rowlist = cursor.fetchall()
    print(rowlist);
    return render_template('assets/index.html', data=rowlist)

@app.route("/populate", methods=['get', 'post'])
def populate_db():
    conn = get_db()
    cur = conn.cursor()
    with app.open_resource("populate.sql") as file: # open the file
        alltext = file.read() # read all the text
        cur.execute(alltext) # execute all the SQL in the file
    conn.commit()
    print("Populated DB with sample data.")
    return render_template("create_data.html")

@app.route("/create", methods=['get', 'post'])
def init_db():
    """Clear existing data and create new tables."""
    conn = get_db()
    cur = conn.cursor()
    with app.open_resource("schema.sql") as file: # open the file
        alltext = file.read() # read all the text
        cur.execute(alltext) # execute all the SQL in the file
    conn.commit()
    print("Initialized the database.")
    return render_template("con_db.html")

### Start flask
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
