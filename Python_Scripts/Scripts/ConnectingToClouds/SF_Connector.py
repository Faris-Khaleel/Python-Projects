import snowflake.connector
import json
import maskpass

with open('Credentials/faris_sf.json') as f:
    data = json.load(f)

sf_pwd = maskpass.askpass(prompt="Enter your Snowflake password: ", mask="*")


conn = snowflake.connector.connect(
    user=data['user'],
    password=sf_pwd,
    account=data['account'],
    warehouse=data['warehouse'],
    database=data['database'],
    schema=data['schema'],
    role=data['role'])
cur = conn.cursor()

cur.execute("SELECT * from FARIS_SF_DB.FARIS_SF_DATA_SET.FARIS_TABLE")

while True:
    row = cur.fetchone()
    if not row:
        break
    print(row)
