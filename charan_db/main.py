import openai
from charan_db.sql_query import exectute_sql_query
from prompts import prompt
# Set your OpenAI GPT-3 API key


openai.api_key="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"
def analyze_sentiment(sentence):
	# Use OpenAI GPT-3 to analyze sentiment
	response = openai.Completion.create(
		engine="text-davinci-002",  # You can also use "text-davinci-002" or other engines
		prompt=f"input:{sentence}, {prompt} \n give me the relevant sql query to execute for Microsoft SQL Server database,  table-name = dbo.tbjobmaster ",
		temperature=0,
		max_tokens=100,
		top_p=1.0,
		frequency_penalty=0,
		presence_penalty=0
	)

	# Extract sentiment from the response
	output_query = str(response.choices[0].text.strip().lower())
	print(output_query)
	output_query = output_query.replace('\n',' ')
	print(output_query)
	sql_result = exectute_sql_query(output_query)
	print(sql_result)



	return sql_result

print(analyze_sentiment("what is the total articles recieved in a month in 2023"))



