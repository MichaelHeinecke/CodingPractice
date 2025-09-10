import duckdb

if __name__ == '__main__':
    con = duckdb.connect('data/activity_db.duckdb')

    # Daily active users: count per date
    # Weekly active users: count per rolling 7 days
    # Monthly active users: count per rolling 28 days

    con.sql("""
            select *
            from Activity
            order by event_time
            """).show()

    con.sql("""
            select distinct
                date (event_time) as event_date, count (distinct user_id) over(order by date (event_time) range between current row and current row) as DAU, count (distinct user_id) over(order by date (event_time) range between interval 6 day preceding and current row) as WAU, count (distinct user_id) over(order by date (event_time) range between interval 27 day preceding and current row) as MAU,
            from
                Activity
            order by event_date
            """).show()

    # Weekly retention
    con.sql("""
            with first_week as (
                select
                    user_id,
                    date_trunc('week', min(event_time)) as cohort_week
                from Activity
                group by user_id
            ),
                 cohort_size as (
                     select
                         cohort_week,
                         count(distinct user_id) as cohort_size
                     from first_week
                     group by cohort_week
                 ),
                 active_weeks as (
                     select
                         distinct user_id,
                                  date_trunc('week', event_time) as activity_week
                     from Activity
                 ),
                 users_active_per_week_and_cohort as (
                     select
                         f.cohort_week,
                         a.activity_week,
                         c.cohort_size,
                         count(distinct a.user_id) as active_users
                     from first_week f
                              join active_weeks a on f.user_id = a.user_id
                              join cohort_size c on f.cohort_week = c.cohort_week
                     group by f.cohort_week, a.activity_week, c.cohort_size
                 )
            select
                cohort_week,
                activity_week,
                datediff('week', cohort_week, activity_week) as week_offset,
                active_users,
                cohort_size,
                active_users * 1.0 / cohort_size as retention
            from users_active_per_week_and_cohort
            order by cohort_week, week_offset;
            """).show()
