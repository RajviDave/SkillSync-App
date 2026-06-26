from flask import Flask,jsonify, render_template,send_from_directory
import psycopg2
from psycopg2.extras import RealDictCursor
import os

app = Flask(__name__)

db_config = {
    "dbname": "skill_sync",
    "user": "postgres",
    "password": "Aqws@434",
    "host": "localhost",
    "port": "5432"
}

def get_db_connection():
    # RealDictCursor returns rows as Python dictionaries instead of tuples
    conn = psycopg2.connect(**db_config, cursor_factory=RealDictCursor)
    return conn

@app.route('/')
def index():
    return render_template('index.html') 

# API Endpoint to fetch data from the database
@app.route('/api/data', methods=['GET'])
def get_data():
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Execute your SQL query (replace 'users' with your actual table)
        cursor.execute("SELECT username,email FROM users;")
        rows = cursor.fetchall()
        
        cursor.close()
        return jsonify(rows) # Sends rows to frontend as a JSON array
        
    except Exception as e:
        print(f"Database Error: {e}")
        return jsonify({"error": "Internal Server Error"}), 500
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    # Create the public directory if it does not exist
    if not os.path.exists('public'):
        os.makedirs('public')
    app.run(debug=True, port=5000)