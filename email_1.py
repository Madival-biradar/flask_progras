from flask import Flask
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'youremail@gmail.com'
app.config['MAIL_PASSWORD'] = 'your password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
   msg = Message('Hello', sender = 'youremail@gmail.com', recipients = ['recepientsemail@gmail.com'])
   msg.body = "Hello Flask message sent from Flask-Mail  boss when we get holiday........."
   mail.send(msg)
   return "Sent"

if __name__ == '__main__':
   app.run(debug = True)
