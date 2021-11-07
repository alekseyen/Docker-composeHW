from sqlalchemy import create_engine
import os
import pandas as pd

# conn = psycopg2.connect(dbname='example',
#                         user='admin',
#                         password='admin',
#                         host='postgres')  # host = NAME of DOCKER Container wiht POSTGRE_SQL
# cursor = conn.cursor()

# example how to read
# cursor.execute('SELECT * FROM cats LIMIT 10')
# records = cursor.fetchall()

engine = create_engine(os.getenv('DATABASE_CONNECTION_URL'), echo=True)
data_to_record = pd.read_csv('../data/cats.csv', delimiter=';')

data_to_record.to_sql('cats', con=engine, if_exists='fail', index=False)
