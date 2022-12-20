--https://www.hackerrank.com/challenges/what-type-of-triangle
select case
           when A + B <= C or A + C <= B or B + C <= A then "Not A Triangle"
           when A = B and B = C and C = A then "Equilateral"
           when A = B or B = C or C = A then "Isosceles"
           when A <> B and B <> C and A <> C then "Scalene"
           end as type_of_triangle
from Triangles;