import sqlite3
from sqlite3 import Connection

def create_connection(db_file: str) -> Connection:
    """Create a database connection to the SQLite database specified by db_file."""
    conn = sqlite3.connect(db_file)
    return conn
