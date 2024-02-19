#!/usr/bin/python3
"""
lists all states from the hbtn_0e_0_usa database
"""
from sys import argv
import MySQLdb


def list_all_states(username, password, database):

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        password=password,
        db=database,
        port=3306
    )

    cursor = db.cursor

    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()

    db.close()


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: <script> <username> <password> <database>")
        exit(1)
    list_all_states(argv[1], argv[2], argv[3])
