from data import get_DataFrame
import pandas_gbq as gbq

destination_table = 'salesmart.bronze'
project_id='salesanalytics-482412'

def ingest_data():
    dataframe = get_DataFrame()
    print(dataframe.head(10))

    gbq.to_gbq(dataframe, destination_table, project_id=project_id, if_exists='append')

    print("Succesfully uploaded")

if __name__ == "__main__":
    ingest_data()
