import sqlite3

DATABASE_FILE = 'guests.db'

def create_guests_table():
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS guests (
            id INTEGER PRIMARY KEY,
            full_name TEXT,
            email TEXT,
            company TEXT,
            mobile_number TEXT,
            checked_in INTEGER
        )
    ''')

    conn.commit()
    conn.close()

def populate_guests_data():
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()

    guestData = [
        {
            'full_name': 'John Doe',
            'email': 'john.doe@example.com',
            'company': 'ABC Company',
            'mobile_number': '1234567890',
            'checked_in': 0,
        },
        {
            'full_name': 'Jane Smith',
            'email': 'jane.smith@example.com',
            'company': 'XYZ Corporation',
            'mobile_number': '9876543210',
            'checked_in': 1,
        },
        {
            'full_name': 'Guest 1',
            'email': 'guest1@example.com',
            'company': 'Company 1',
            'mobile_number': '1111111111',
            'checked_in': 0,
        },
        {
            'full_name': 'Guest 2',
            'email': 'guest2@example.com',
            'company': 'Company 2',
            'mobile_number': '2222222222',
            'checked_in': 1,
        },
        {
            'full_name': 'Guest 3',
            'email': 'guest3@example.com',
            'company': 'Company 3',
            'mobile_number': '3333333333',
            'checked_in': 0,
        },
        {
            'full_name': 'Guest 4',
            'email': 'guest4@example.com',
            'company': 'Company 4',
            'mobile_number': '4444444444',
            'checked_in': 1,
        },
        {
            'full_name': 'Guest 5',
            'email': 'guest5@example.com',
            'company': 'Company 5',
            'mobile_number': '5555555555',
            'checked_in': 0,
        }
    ]

    for guest in guestData:
        c.execute('''
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

if __name__ == '__main__':
    create_guests_table()
    populate_guests_data()
    print("Database guests.db created and populated with sample data.")
