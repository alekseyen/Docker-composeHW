import psycopg2

from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_cat_info():
    with psycopg2.connect(dbname='example',
                          user='admin',
                          password='admin',
                          host='postgres') as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM cats LIMIT 10')
            records = cursor.fetchall()

    return str(records), 200


@app.route('/health', methods=['GET'])
def get_health():
    return 200
