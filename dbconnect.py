import os
import MySQLdb
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
DB_PASSWORD = os.getenv('DB_PASSWORD')

def connections():
    conn = MySQLdb.connect(host="localhost",
                            user="root",
                            passwd=DB_PASSWORD,
                            db="pythonprogramming")

    c = conn.cursor()

    return c, conn
