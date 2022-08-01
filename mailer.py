from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

API_KEY = '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'
HTMLMESSAGE= '<strong>WELCOME BACK TO MY HOUSE, DARLING</strong>'

def mailer():

    message = Mail(
    from_email='danielorkin06@gmail.com',
    to_emails='orka3103@gmail.com',
    subject='WELCOME',
    html_content= HTMLMESSAGE
    )

    try:
        sg = SendGridAPIClient(api_key=API_KEY)
        sg.send(message)

    except Exception as e:

        print(e.message)