from flask import Flask, request, redirect, render_template
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        # 1. Connect to database
        conn = sqlite3.connect('data.db')
        c = conn.cursor()

        # 2. Insert data
        c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))

        # 3. Commit & close
        conn.commit()
        conn.close()

        return redirect('/')  # redirect to same page to avoid resubmission

    # Display data
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT name, email FROM users")
    rows = c.fetchall()
    conn.close()

    return render_template('index.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
