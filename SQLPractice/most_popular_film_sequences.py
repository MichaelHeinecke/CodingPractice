import duckdb

if __name__ == '__main__':
    con = duckdb.connect('data/viewing_db.duckdb')

    con.sql("""
            select *
            from Viewing
            """).show()

    con.sql("""
            with user_sequences
                     as (select film_id,
                                lead(film_id) over(partition by user_id order by event_time asc) as next_film_id
                         from Viewing)

            select film_id,
                   next_film_id,
                   count(*) as num_occurences
            from user_sequences
            where next_film_id is not null
            group by film_id, next_film_id
            order by num_occurences desc
            """).show()

    # Only count sequence if gap is at most 1 hour
    con.sql("""
            with user_sequences
                     as (select film_id,
                                lead(film_id) over(partition by user_id order by event_time asc) as next_film_id,
                                lead(event_time) over(partition by user_id order by event_time asc) - event_time as gap_between_films
                         from Viewing)

            select
                film_id,
                next_film_id,
                count(*) as num_occurences
            from user_sequences
            where next_film_id is not null
                and gap_between_films <= INTERVAL 60 MINUTES
                group by 1, 2
                order by 3 desc
            """).show()
