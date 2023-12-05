from flask import (
    Blueprint, render_template, request, redirect, url_for, current_app
)
import sendgrid
from sendgrid.helpers.mail import *


bp = Blueprint('portfolio', __name__, url_prefix = '/')

@bp.route('/', methods = ['GET'])
def index():
    data = {
        'titulo': 'KAIROS',
        'bienvenida': 'Software Solutions',
        'lorem': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Aut vel porro corrupti ex doloremque praesentium nihil quam amet illo fuga!',
        'soluciones': 'Desarrollamos con pasión software para soluciones empresariales.'
    }
    return render_template('portfolio/index.html', data=data)

@bp.route('/mail', methods = ['GET','POST'])
def mail():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if request.method == 'POST':
        # send_mail(name, email, message)
        return render_template('portfolio/sent_mail.html')

    return redirect(url_for('portfolio.index'))

def send_mail(name, email, message):
    mi_email = 'kairossoftware.com'
    sg = sendgrid.SendGridAPIClient(api_key=current_app.config['SENDGRID_KEY'])

    from_email = Email(mi_email)
    to_email = To(mi_email, substitutions = {
        "-name-": name,
        "-email-": email,
        "-message-": message,
    })

    html_content = """
        <p>Buen día Sr. Carlos, tiene un nuevo contacto desde la web </p>
        <p>Nombre: -name-</p>
        <p>Correo: -email-</p>
        <p>Mensaje: -message-</p>
    """

    mail = Mail(mi_email, to_email, 'Nuevo contacto desde la web', html_content = html_content)
    response = sg.client.mail.send.post(request_body = mail.get())