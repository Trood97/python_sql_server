

An important thing to remember: aggregators only aggregate vertically.
If you want to perform a calculation across rows, you would do this with simple arithmetic.

COUNT counts how many rows are in a particular column.
SUM adds together all the values in a particular column.
MIN and MAX return the lowest and highest values in a particular column, respectively.
AVG calculates the average of a group of selected values.


Count :
# returns the number of rows associated with the query
select count(EditedBy)from ArticleAnalysis.EditReport where EditedBy = ' '

Sum:
# returns the sum of the entire vertical column from the query
select Sum(Id) from ArticleAnalysis.EditReport where id between 16 and 50000

Min and Max:
# MIN will return the lowest number, earliest date, or non-numerical value as close alphabetically to "A" as possible.
# As you might suspect, MAX does the opposite—it returns the highest number,
# the latest date, or the non-numerical value closest alphabetically to "Z."

select Max(Id) as maximim_value, Min(Id) as minimum_value from ArticleAnalysis.EditReport where id between 16 and 50000


Avg:
select Avg(Id) as Average_id from ArticleAnalysis.EditReport where Id Between 1 and 64000

Group by:
select count(*), ArticleId from ArticleAnalysis.EditReport group by ArticleId     , #select items should reflect in the groupby clause sections

Having:
HAVING is the "clean" way to filter a query that has been aggregated, but this is also commonly done using a subquery
Query for the existing query
select count(*) as count1, ArticleId
from ArticleAnalysis.EditReport group by ArticleId having count(*) > 100

Case:
Every CASE statement must end with the END statement. The ELSE statement is optional,
and provides a way to capture values not specified in the WHEN/THEN statements.
select Id ,case when Id < 50000 then 'yes' else 'nope' end as qualified from ArticleAnalysis.EditReport

Distinct:
Distinct items, say identifying unique elements
select count(Distinct(JournalId)) from ArticleAnalysis.EditReport

Joins:

The real power of SQL, however, comes from working with data from multiple tables at once.
--If you remember from a previous lesson, the tables you've been working with up to this point are all part of the same schema in a relational database. ' \
'The term "relational database" refers to the fact that the tables within it "relate" to one another—they contain common identifiers ' \
that allow information from multiple tables to be combined easily.

A join is all we need

select * from ArticleAnalysis.[User] as user0 join ArticleAnalysis.UserRole as user1 on user1.Id = user0.Id   #joining on the id column from both the tables

The two columns that map to one another, are referred to as "foreign keys" or "join keys." Their mapping is written as a conditional statement

Inner join:
an inner join is the intersection of the two tables.
inner join is simple join
select user1.* from ArticleAnalysis.[User] as user0 join ArticleAnalysis.UserRole as user1 on user1.Id = user0.Id



