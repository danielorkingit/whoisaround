from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

API_KEY = 'YOUR_API_KEY '
HTMLMESSAGE= '<strong>YOUR MESSAGE WITHIN HTML</strong>'

def mailer():

    message = Mail(
    from_email='SENDER_MAIL',
    to_emails='RECIPIENT_EMAIL',
    subject='WELCOME',
    html_content= HTMLMESSAGE
    )

    try:
        sg = SendGridAPIClient(api_key=API_KEY)
        sg.send(message)

    except Exception as e:

        print(e.message)
