-- https://www.hackerrank.com/challenges/occupations/problem
with names_ordered_per_occupation as (select row_number() over (partition by Occupation order by name) as row_num,
                                             Name,
                                             Occupation
                                      from Occupations)
select min(IF(Occupation = "Doctor", Name, null))    as Doctor,
       min(IF(Occupation = "Professor", Name, null)) as Professor,
       min(IF(Occupation = "Singer", Name, null))    as Singer,
       min(IF(Occupation = "Actor", Name, null))     as Actor
from names_ordered_per_occupation
group by row_num;