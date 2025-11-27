from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# --- configure your mail ---
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'rohitkamati28@gmail.com'  # replace with yours
app.config['MAIL_PASSWORD'] = 'fxze ykgk bnog yccg'      # Gmail app password, not normal password

mail = Mail(app)

@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')

    msg = Message('New Contact Submission',
                  sender='your_email@gmail.com',
                  recipients=['your_email@gmail.com'])
    msg.body = f"""
    New connection from your portfolio:
    Name: {name}
    Email: {email}
    Phone: {phone}
    """
    mail.send(msg)
    return jsonify({"message": "Email sent successfully!"}), 200


if __name__ == '__main__':
    app.run(debug=True)
