from flask import Flask, request, jsonify, after_this_request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)


def get_db_connection():
    try:
        conn = sqlite3.connect('guests.db')
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print("Database connection error:", e)


def init_db():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS guests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT,
                email TEXT,
                company TEXT,
                mobile_number TEXT,
                checked_in INTEGER
            )
        ''')
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print("Database initialization error:", e)


@app.route('/guests', methods=['GET'])
def get_guests():
    try:
        conn = get_db_connection()
        conn.row_factory = sqlite3.Row
        c = conn.cursor()

        c.execute('SELECT * FROM guests')
        rows = c.fetchall()

        guests = [dict(row) for row in rows]  # Convert rows to dictionaries

        conn.close()

        @after_this_request
        def add_cache_control_header(response):
            response.headers['Cache-Control'] = 'no-store'
            return response

        return jsonify(guests)
    except sqlite3.Error as e:
        print("Error retrieving guests:", e)
        return jsonify({'message': 'Error retrieving guests'}), 500


@app.route('/guests', methods=['POST'])
def add_guest():
    try:
        guest = request.get_json()

        conn = get_db_connection()
        cursor = conn.cursor()

        # Check if the guest with the same full_name already exists
        cursor.execute('SELECT * FROM guests WHERE full_name = ?', (guest['full_name'],))
        existing_guest = cursor.fetchone()

        if existing_guest:
            conn.close()
            return jsonify({'message': 'Guest with the same full_name already exists'}), 409

        # Insert the guest into the database
        cursor.execute('''
            INSERT INTO guests (full_name, email, company, mobile_number, checked_in)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            guest['full_name'],
            guest['email'],
            guest['company'],
            guest['mobile_number'],
            guest['checked_in']
        ))
        conn.commit()
        conn.close()

        @after_this_request
        def add_cache_control_header(response):
            response.headers['Cache-Control'] = 'no-store'
            return response

        return jsonify({'message': 'Guest added successfully'}), 201
    except sqlite3.Error as e:
        print("Error adding guest:", e)
        return jsonify({'message': 'Error adding guest'}), 500


@app.route('/guests/<email>', methods=['PUT'])
def check_in_guest(email):
    print(email)
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE guests
            SET checked_in = ?
            WHERE email = ?
        ''', (1, email))
        conn.commit()
        conn.close()

        @after_this_request
        def add_cache_control_header(response):
            response.headers['Cache-Control'] = 'no-store'
            return response

        return jsonify({'message': 'Guest check-in updated successfully'}), 200
    except sqlite3.Error as e:
        print("Error updating guest check-in:", e)
        return jsonify({'message': 'Error updating guest check-in'}), 500


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
