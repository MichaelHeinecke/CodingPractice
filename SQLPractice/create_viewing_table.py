import datetime

import duckdb

if __name__ == '__main__':
    con = duckdb.connect('data/viewing_db.duckdb')

    # Create the Viewing table
    con.execute("""
                DROP TABLE IF EXISTS Viewing
                """)
    con.execute("""
                CREATE TABLE IF NOT EXISTS Viewing
                (
                    user_id    STRING,
                    film_id    INTEGER,
                    event_time TIMESTAMP
                )
                """)

    # Generate sample data
    rows = [
        ("user_1", 100, datetime.datetime(2025, 6, 1, 12, 0, 0)),
        ("user_1", 101, datetime.datetime(2025, 6, 1, 13, 0, 0)),
        ("user_2", 100, datetime.datetime(2025, 6, 1, 12, 30, 0)),
        ("user_2", 101, datetime.datetime(2025, 6, 1, 13, 45, 0)),
        ("user_2", 102, datetime.datetime(2025, 6, 1, 14, 10, 0)),
        ("user_2", 100, datetime.datetime(2025, 6, 1, 16, 0, 0)),
        ("user_3", 102, datetime.datetime(2025, 6, 1, 17, 0, 0)),
        ("user_3", 100, datetime.datetime(2025, 6, 1, 18, 0, 0)),
        ("user_4", 102, datetime.datetime(2025, 6, 1, 17, 0, 0)),
        ("user_4", 100, datetime.datetime(2025, 6, 1, 18, 1, 0)),
        ("user_4", 102, datetime.datetime(2025, 6, 2, 17, 0, 0)),
        ("user_4", 100, datetime.datetime(2025, 6, 2, 18, 0, 0)),
    ]

    # Insert data
    con.executemany("INSERT INTO Viewing VALUES (?, ?, ?)", rows)
