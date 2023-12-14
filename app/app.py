from flask import Flask, render_template, url_for, redirect, request, flash
from flask_sqlalchemy import SQLAlchemy
#from flask_wtf import FlaskForm
#from wtforms import StringField, PasswordField, SubmitField, validators

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI '] = 'sqlite:///database/datos.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    #if request.method == 'POST':
        # Aquí puedes manejar la lógica para registrar el usuario en la base de datos
        # Por ejemplo, obtener los datos del formulario: request.form['nombre'], request.form['correo'], etc.
        # Y luego, almacenar estos datos en la base de datos usando SQLAlchemy

        # Después de registrar, podrías redirigir a otra página o hacer lo que necesites
        #return redirect(url_for('index'))

    return render_template('registro.html')

@app.route('/iniciar_sesion', methods=['GET', 'POST'])
def iniciar_sesion():
    #if request.method == 'POST':
        # Aquí puedes manejar la lógica para iniciar sesión
        # Por ejemplo, verificar las credenciales en la base de datos

        # Después de iniciar sesión, podrías redirigir a otra página o hacer lo que necesites
        #return redirect(url_for('index'))

    return render_template('iniciar_sesion.html')

@app.route('/tareas')
def tareas():
    return render_template('tareas.html')

@app.route('/habitos')
def habitos():
    return render_template('habitos.html')

#def pagina_no_encontrada(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    #app.register_error_handler(404,pagina_no_encontrada)
    app.run(debug=True, port=5000)
