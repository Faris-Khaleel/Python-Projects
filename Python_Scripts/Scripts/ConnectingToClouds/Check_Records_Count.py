import snowflake.connector
from google.cloud import bigquery
from google.oauth2 import service_account
from getpass import getpass
import maskpass
import json


print('\nEstablishing Connection to Both BigQuery and Snowflake...')

# Snowflake Connection
# sf_pwd = getpass(prompt="Enter your Snowflake password: ")
sf_pwd2 = maskpass.askpass(prompt="Enter your Snowflake password: ", mask="*")

with open('Credentials/faris_sf.json') as f:
    data = json.load(f)


conn = snowflake.connector.connect(
    user=data['user'],
    password=sf_pwd2,
    account=data['account'],
    warehouse=data['warehouse'],
    database=data['database'],
    schema=data['schema'],
    role=data['role'])
cur = conn.cursor()

# BigQuery Connection
credentials = service_account.Credentials.from_service_account_file('Credentials/faris_bq.json')
project_id: str = 'faris-bq-traning'
client = bigquery.Client(credentials=credentials, project=project_id)

print('Connection Established Successfully \n -> Comparing Records Count Now...')

# Snowflake Query
cur.execute("SELECT count(*) from FARIS_SF_DB.FARIS_SF_DATA_SET.FARIS_TABLE")
sf_count = cur.fetchone()[0]

# BigQuery Query
BQ_query_job = client.query(""" 
SELECT count(*) FROM faris-bq-traning.Faris_Goals.skills 
""")
bq_count = [row[0] for row in BQ_query_job.result()][0]

print('Records count is ', end='')
if sf_count == bq_count:
    print(f'the same - BigQuery records count is {bq_count} = Snowflake records count {sf_count}')
else:
    print(f'not the same - BigQuery records count is {bq_count} != Snowflake records count {sf_count}')
