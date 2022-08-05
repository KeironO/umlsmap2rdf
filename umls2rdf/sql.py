import sqlite3

def generate_sqlite_file(output_fp: str) -> None:
    conn = sqlite3.connect(output_fp)
    cursor = conn.cursor()


generate_sqlite_file("dev.sql")