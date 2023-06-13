from google.cloud import bigquery
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('Credentials/faris_bq.json')
project_id: str = 'faris-bq-traning'

client = bigquery.Client(credentials=credentials, project=project_id)

query_job = client.query(""" 
  
SELECT *  FROM faris_dataset_1.test_table_1 
order by id asc

 """)

query_job_result = query_job.result()

for row in query_job_result:
    print(row.id)
