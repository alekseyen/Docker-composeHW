import psycopg2

from flask import Flask

app = Flask(__name__)
conn = psycopg2.connect(dbname='example',
                        user='admin',
                        password='admin',
                        host='postgres')  # host = NAME of DOCKER Container with POSTGRE_SQL


@app.route('/', methods=['GET'])
def get_cat_info():
    print('!!! get_query !!!')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cats LIMIT 10')
    records = cursor.fetchall()
    cursor.close()

    return records, 200


@app.route('/health', methods=['GET'])
def get_health():
    if conn.closed:
        return 404
    return 200

conn.close()

################

# import psycopg2
# import pandas as pd
#
# conn = psycopg2.connect(dbname='example',
#                         user='admin',
#                         password='admin',
#                         host='postgres')  # host = NAME of DOCKER Container wiht POSTGRE_SQL
# cursor = conn.cursor()
#
# # example how to read
# # cursor.execute('SELECT * FROM cats LIMIT 10')
# # records = cursor.fetchall()
#
#
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS cats (
#     name text,
#     price int,
#     breed text);
# """)
#
# conn.commit()
#
# data_to_record = pd.read_csv('../data/cats.csv', delimiter=';')
#
# with open('data/cats.csv', 'r') as f:
#     cursor.copy_from(f, 'cats', sep=';')
#
# conn.commit()
#
# cursor.close()
# conn.close()
