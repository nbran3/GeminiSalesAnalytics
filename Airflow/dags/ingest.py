from Airflow.dags.data import get_DataFrame
import pandas_gbq as gbq

def ingest_data():
    dataframe = get_DataFrame()
    print(dataframe.head(10))

    gbq.to_gbq(dataframe)

    print("Succesfully uploaded ")