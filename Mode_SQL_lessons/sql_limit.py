

#for sql server limit clause cannot be used, instead we can go for "top"
select top 5 Id,JournalId,ArticleId,JobDoneDate as "job_done_date" from ArticleAnalysis.EditReport

#for other sql servers
SELECT * FROM tutorial.us_housing_units LIMIT 100

--------x-----------x--------x-----------x------------

