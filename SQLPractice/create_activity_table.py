import duckdb

if __name__ == '__main__':
    con = duckdb.connect('data/activity_db.duckdb')

    con.execute("""
                DROP TABLE IF EXISTS Activity
                """)
    con.execute("""
                CREATE TABLE IF NOT EXISTS Activity
                (
                    user_id integer,
                    event_time timestamp,
                    country varchar
                )
                """)


    rows = [
        # -- User 1 active multiple days in same week
        (1, '2025-08-25 10:00:00', 'US'),
        (1, '2025-08-26 12:00:00', 'US'),
        (1, '2025-09-01 09:00:00', 'US'),

        # -- User 2 active across multiple weeks
        (2, '2025-08-25 11:00:00', 'US'),
        (2, '2025-08-30 14:00:00', 'US'),
        (2, '2025-09-02 15:00:00', 'US'),

        # -- User 3 only active one week
        (3, '2025-08-27 16:00:00', 'CA'),

        # -- User 4 active every week
        (4, '2025-08-25 17:00:00', 'CA'),
        (4, '2025-09-01 18:00:00', 'CA'),

        # -- User 5 churned after one day
        (5, '2025-08-25 19:00:00', 'US'),
    ]

    con.executemany("INSERT INTO Activity VALUES (?, ?, ?)", rows)
