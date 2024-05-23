table - theater

seat , availability (1 or 0)

with cte as(
select *, dense_rank() over(availability) as rank from theater 
) 

select cte where count(rank) >1

seat , availability (1 or 0), rank
1       1                       1
2       0                       2
3       1                       3
4       1                       3
5       1                       3
5       0                       4

have to find seat numbers with consecutive avilablity of "1"





