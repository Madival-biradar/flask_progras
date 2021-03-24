from flask import Flask
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'madivalbiradar14@gmail.com'
app.config['MAIL_PASSWORD'] = 'Madival.14@'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
   msg = Message('Hello', sender = 'madivalbiradar14@gmail.com', recipients = ['chandanchandy1998@gmail.com'])
   msg.body = "Hello Flask message sent from Flask-Mail  boss when we get holiday........."
   mail.send(msg)
   return "Sent"

if __name__ == '__main__':
   app.run(debug = True)
