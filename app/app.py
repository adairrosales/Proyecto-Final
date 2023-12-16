from flask import Flask, render_template, url_for, redirect, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from flask_login import login_user
from flask_login import LoginManager, UserMixin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
#app.config['SQLALCHEMY_DATABASE_URI '] = 'sqlite:///database/datos.db'
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Modelo de usuario
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# formulario de registro
class RegistrationForm(FlaskForm):
    username = StringField('Usuario', validators=[validators.DataRequired(), validators.Length(min=2, max=20)])
    password = PasswordField('Contraseña', validators=[validators.DataRequired()])
    confirm_password = PasswordField('Confirmar Contraseña', validators=[validators.DataRequired(), validators.EqualTo('password')])
    submit = SubmitField('Registrarse')

#   formulario de inicio de sesión    
class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[validators.DataRequired(), validators.Length(min=2, max=20)])
    password = PasswordField('Contraseña', validators=[validators.DataRequired()])
    submit = SubmitField('Iniciar Sesión')

@app.route('/')
def index():
    flash_messages = None

    # Verifica si estamos en el contexto de una solicitud antes de intentar acceder a flash
    if request:
        flash_messages = request.environ.get('FLASK_FLASH_MESSAGES', [])

    return render_template('index.html', flash_messages=flash_messages)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('¡Cuenta creada exitosamente!', 'success')
        return redirect(url_for('index'))
    return render_template('registro.html',form=form)

@app.route('/iniciar_sesion', methods=['GET', 'POST'])
def iniciar_sesion():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('index'))
        else:
            flash('Inicio de sesión fallido. Verifica tu usuario y contraseña.', 'danger')

    return render_template('iniciar_sesion.html',form=form)

@app.route('/tareas')
def tareas():
    return render_template('tareas.html')

@app.route('/habitos')
def habitos():
    return render_template('habitos.html')

#def pagina_no_encontrada(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)