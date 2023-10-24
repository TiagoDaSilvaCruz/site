from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

# Configurações de e-mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'jogosoficial.be@gmail.com'
app.config['MAIL_PASSWORD'] = 'ouvz btrc tpqg mhul'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/')
def enviar_email():
    try:
        msg = Message("Assunto do E-mail", sender='jogosoficial.be@gmail.com', recipients=['jogosoficial.be@gmail.com'])
        msg.body = "Corpo do e-maildddddddd"
        mail.send(msg)
        return "E-mail enviado com sucesso"
    except Exception as e:
        return f"Erro ao enviar o e-mail: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
