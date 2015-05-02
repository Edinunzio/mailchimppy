import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from django.http import HttpResponse
import mailchimp

from utils import *


def get_mailchimp_api():
    return mailchimp.Mailchimp(MAILCHIMP_API_KEY)


def index(request):
    """
    Proof of concept using https://github.com/mailchimp/mcapi2-python-examples

    My repo: https://github.com/Edinunzio/mailchimppy

    After starting up the server, going to localhost:8000 triggers
    hardcoded email sent to subscribers grouped by mailchimp list id


    Neccesary credentials kept out of git:
    *************************************

    MAILCHIMP_API_KEY = '<got my own key>'
    DEVELOPER_LIST_ID = '<list id for the poorly named list, "developer list">'
    USERNAME='<sender>'
    PASSWORD='<sender's email password>'

    *************************************
    :param request:
    :return:
    """
    template = """
    <table width="600" style="border:5px solid #000;">
        <tr>
            <td>Col1</td>
            <td>Col2</td>
            <td>Col3</td>
        </tr>
        <tr>
            <td>aaa</td>
            <td>bbb</td>
            <td>ccc</td>
        </tr>
    </table>
    """

    # passes mailchimp api key
    m = get_mailchimp_api()

    # getting all the emails from a mailchimp list. i happened to name
    # my list "DEVELOPER_LIST" so, oops?

    lists = m.lists.list({'list_id': DEVELOPER_LIST_ID})
    to = m.lists.members(DEVELOPER_LIST_ID)['data']
    recipients = [recipient['email'] for recipient in to]

    # setting up the email

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Hello World again!"
    msg['From'] = 'earlsammich@gmail.com'
    msg['To'] = ", ".join(recipients)
    msg.preamble = msg['Subject']
    msg.attach(MIMEText(template, 'html'))

    # using gmail's smtp

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(USERNAME, PASSWORD)
    server.sendmail('earlsammich@gmail.com', recipients, msg.as_string())
    server.quit()

    # I just got lazy here I know...

    return HttpResponse('sent')

