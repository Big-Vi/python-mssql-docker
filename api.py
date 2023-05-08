import config
import pyodbc

from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        f'SERVER={config.db_url};'
        f'DATABASE={config.db_name};'
        f'UID={config.db_user};'
        f'PWD={config.db_pass}',
        autocommit=True
    )
    print(connection)
    return "Server is running..."

if __name__ == '__main__':
    app.run()
