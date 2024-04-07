#Импорт
from flask import Flask, render_template,request, redirect
#Подключение библиотеки баз данных
from flask_sqlalchemy import SQLAlchemy
from speach import speach

app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def process_form():
    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python)

if __name__ == "__main__":
    app.run(debug=True)
