import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from django.http import HttpResponse
import mailchimp

from utils import *


def get_mailchimp_api():
    return mailchimp.Mailchimp(MAILCHIMP_API_KEY)



# Create your views here.
def index(request):
    template = """
    <table>
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
    m = get_mailchimp_api()
    lists = m.lists.list({'list_id': DEVELOPER_LIST_ID})
    list = lists['data'][0]
    to = m.lists.members(DEVELOPER_LIST_ID)['data']
    recipients = []
    for e in to:
        recipients.append(e['email'])

    """subject, from_email, to = 'hello', 'e.dinunzio@gmail.com', recipients
    text_content = 'Plain text'
    html_content = '<p>This is an <strong>important</strong> message.</p>'
    #msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    """

    # msg = MIMEMultipart()
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Hello World"
    msg['From'] = 'earlsammich@gmail.com'
    msg['To'] = ", ".join(recipients)
    msg.preamble = msg['Subject']
    msg.attach(MIMEText(template, 'html'))

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(USERNAME, PASSWORD)
    server.sendmail('earlsammich@gmail.com', recipients, msg.as_string())
    server.quit()


    # return  HttpResponseRedirect('http://www.google.com')
    return HttpResponse('sent')

