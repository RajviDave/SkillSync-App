from flask import Flask,jsonify,send_from_directory
import psycopg2
from psycopg2.extras import RealDictCursor
import os

app = Flask(__name__)

db_config = {
    "dbname": "your_database_name",
    "user": "your_postgres_user",
    "password": "your_database_password",
    "host": "localhost",
    "port": "5432"
}