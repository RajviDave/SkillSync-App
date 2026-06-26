from flask import Flask,jsonify,send_from_directory
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