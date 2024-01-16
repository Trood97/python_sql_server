

Note: the clauses always need to be in this order: SELECT, FROM, WHERE.

#for sql server , single quotes are needed and ennding with a semi colon
select top 5 Id, JournalId, ArticleId, JobDoneDate as "job_done_date" from ArticleAnalysis.EditReport where JournalId = 'GHG';

#for other sql servers:
SELECT * FROM tutorial.us_housing_units WHERE month = 1


-------x-----------x-----------x---------------x-----------




