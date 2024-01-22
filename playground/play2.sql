

/*Intermediate SQL */

--Aggregators - aggregate values vertically -
-- COUNT,SUM,MIN,MAX,AVG

/*// Aggregators */
COUNT - counts all the rows of a specified column,  -> returns a single value
/* usage = count(column) -> returns count of only non null values of the column */

SUM - adds all the rows of a column  -> returns a single value
/* usage = sum(column) = if a null is present it treats it as a zero */

MIN/MAX(colunm) -> returns a single value  , =max or min of that column, a-Z, 1-9.

AVG(column) -> returns a single value, = average of the columns rows ignoring NULL

GROUP BY(COLUMN) -> groups identical rows of a column into a single entity, ** works with only aggregate function(what should be done)**

HAVING = The WHERE clause won't work for this because it doesn't allow you to filter on aggregate
         columns—that's where the HAVING clause comes in:
         (playing with the aggregated value)
         -> returns the matched scenarios

CASE - works with select , a new column will be created, config - case when then else end as "column_name" -> creates a column with filters

DISTINCT - unique values from the columns, targeted directly to the column names with select key

JOIN - joins two tables as simple as that,  syn- ...from table_A join table_B on table_B.col = table_A.col..  -> joins two tables (relational)
        "foreign keys" or "join keys.

INNER JOIN - same as join basically, returns intersecting rows only, like intersection, syn - inner join .. on (or) just join
        -> returns intersected rows only

** INNER JOIN IS JOIN , LEFT ALL ARE OUTER ONES **

LEFT JOIN - from table_A.. is the left table , join table_B , is the right table, -> returns all mathced and unmatched rows from left table

RIGHT JOIN - not much difference, anyway matched item only intersect on joining, left join can be used in lieu of this. -> returns matched from right table

WHERE AND ON -  And operator only exectutes from the right table and doesn't eradicate possiblities from the left table. that is where 'WHERE' comes in

UNION , UNION ALL - stacking data on top of the other unlike joins which is side by side. Two select statements here.

JOIN WITH COMPARISION OPERATORS = after joining can use operators with AND or WHERE conditions while joining the tables.

SELF JOINS - joining the same table with aliases for further clarity and operations.