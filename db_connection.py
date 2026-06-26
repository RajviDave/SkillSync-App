from flask import Flask,jsonify,send_from_directory
import psycopg2
from psycopg2.extras import RealDictCursor
import os