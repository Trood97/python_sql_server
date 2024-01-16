

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