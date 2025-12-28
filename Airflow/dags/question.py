from google import genai
from google.cloud import bigquery

client = genai.Client(api_key='')
project_id = ''
bq_client = bigquery.Client(project=project_id)

SCHEMA_CONTEXT = """
Table Name: your_project.your_dataset.your_table
Columns:
- transactionID (STRING)
- order_date (STRING)
- paymentType (STRING)
- category (STRING)
- item (STRING)
- price (STRING) -> Note: Needs to be CAST to FLOAT64 for math
- quantity (STRING) -> Note: Needs to be CAST to INT64 for math
- name (STRING)
- state (STRING)
- accountID (STRING)
"""

def ask_Gemini(question):
    dataset_table = "salesmart.bronze" 
        
    print("Read Table successfully")
    
    prompt = (
        f"You are a Data Analyst skilled in BigQuery SQL. "
        f"Table: {dataset_table}\n"
        f"Schema: {SCHEMA_CONTEXT}\n"
        f"Question: {question}\n"
        f"Return ONLY the SQL query. Do not use markdown backticks."
    )
    response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents=prompt
    )
    sql = response.text.strip()
    sql = sql.replace('```sql', '').replace('```', '').strip()

    print(f"Executing: {sql}")
    
    try:
        query_job = bq_client.query(sql)
        return query_job.to_dataframe()
    except Exception as e:
        return f"Error executing SQL: {e}"

df = ask_Gemini(input())
print(df)