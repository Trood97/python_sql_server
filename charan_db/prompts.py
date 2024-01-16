
prompt = '''Given below are the table structures in  database raw schema in Sql_server cloud database, I want you to go through each columns carefully and produce relevant results
	       JobMaster (
                         jobid VARCHAR(150),
                         userid BIGINT,
                         Articleid VARCHAR(-1),
                         clientid BIGINT,
                         inputfilename VARCHAR(-1),
                         pagecount BIGINT,
                         journalid VARCHAR(-1),
                         inputpackagepath VARCHAR(-1),
                         outputpackagepath VARCHAR(-1),
                         wippackagepath VARCHAR(-1)
                         Status VARCHAR(-1),
                         Jobcreatedon DATETIME,
                         paginationRequired bit,
                         modifiedOn DATETIME,
                         jobdone DATETIME,
                         MathCount int,
                         stage nvarchar,
                 );
                 take user questions and response back with sql query.
           example :
           User question: "Show me the articles with the highest pagecount."
            Your generated SQL query: |
              SELECT Articleid, editcount
              FROM tbJobMaster
              ORDER BY editcount DESC
	       User question: "how many journals are not onboarded"
	       answer : SELECT COUNT(journalid) from dbo.tbjobmaster where status like 'Journal not onboarded'
'''