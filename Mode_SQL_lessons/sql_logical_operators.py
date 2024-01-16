


LIKE - allows you to match similar values, instead of exact values.
IN -  allows you to specify a list of values you'd like to include.
BETWEEN  - allows you to select only rows within a certain range.
IS NULL  -  allows you to select rows that contain no data in a given column.
AND    -  allows you to select only rows that satisfy two conditions.
OR -  allows you to select rows that satisfy either of two conditions.
NOT  -  allows you to select rows that do not match a certainn not condition

LIke :
select * from ArticleAnalysis.EditReport where role like 'edi_o%'  # _ for a character wildcard,  % wildcard for further chars

In:
select * from ArticleAnalysis.EditReport where Role in ('editor','manager')       #(array of elements of targets)

Between :
select * from ArticleAnalysis.EditReport where Id between 1 and 16             #between 1 and 16

is Null :
select * from ArticleAnalysis.EditReport where Before_Without_Tags is Null

And:
select * from ArticleAnalysis.EditReport where Before_Without_Tags is Null and After like '1%'  #And logic,

or:
select * from ArticleAnalysis.EditReport where Before_Without_Tags is Null or After like '1%'   #or logic

not:
select * from ArticleAnalysis.EditReport where  not Before_Without_Tags is Null and After like '1%'   #not reversing the query.

order by:
You 'll notice that the results are now ordered alphabetically from a to z based on the content is None
select * from ArticleAnalysis.EditReport order by EditedBy asc

Commenting on SQL:

--select * from ArticleAnalysis.EditReport order by EditedBy asc  COMMENTING THE ENTIRE LINE
 /* for a specific
      area, can use this commeting technique*/


--------------x----------------x-------------------x----------------------x-------------





