import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from django.http import HttpResponse
from django.template.loader import get_template
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
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
   "http://www.w3.org/TR/html4/loose.dtd">
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name="viewport" content="initial-scale=1.0">    <!-- So that mobile webkit will display zoomed in -->
    <meta name="format-detection" content="telephone=no"> <!-- disable auto telephone linking in iOS -->

    <title>Antwort - responsive Email Layout</title>
    <link href="http://fonts.googleapis.com/css?family=Open+Sans:300italic,300,400italic,400,600italic,600,700italic,700,800italic,800" rel="stylesheet" type="text/css">
    <style type="text/css">

        /* Resets: see reset.css for details */
        .ReadMsgBody { width: 100%; background-color: #ebebeb;}
        .ExternalClass {width: 100%; background-color: #ebebeb;}
        .ExternalClass, .ExternalClass p, .ExternalClass span, .ExternalClass font, .ExternalClass td, .ExternalClass div {line-height:100%;}
        body {-webkit-text-size-adjust:none; -ms-text-size-adjust:none;}
        body {margin:0; padding:0;}
        table {border-spacing:0;}
        table td {border-collapse:collapse;}
        .yshortcuts a {border-bottom: none !important;}

        td[class="container-padding"] {
            padding-left: 30px; padding-right: 30px; font-size: 13px; font-family: Open Sans, sans-serif; color: #333;
        }
        h3[class="header"] {
            color:#fff; font-family: Open Sans, sans-serif;font-size:30px; font-weight:400;
        }



        /* Constrain email width for small screens */
        @media screen and (max-width: 600px) {
            table[class="container"] {
                width: 95% !important;
            }
        }

        /* Give content more room on mobile */
        @media screen and (max-width: 480px) {
            td[class="container-padding"] {
                padding-left: 12px !important;
                padding-right: 12px !important;
            }
        }


        /* Styles for forcing columns to rows */
        @media only screen and (max-width : 600px) {

            /* force container columns to (horizontal) blocks */
            td[class="force-col"] {
                display: block;
                padding-right: 0 !important;
            }
            table[class="col-3"] {
                /* unset table align="left/right" */
                float: none !important;
                width: 100% !important;

                /* change left/right padding and margins to top/bottom ones */
                margin-bottom: 12px;
                padding-bottom: 12px;
                border-bottom: 1px solid #eee;
            }

            /* remove bottom border for last column/row */
            table[id="last-col-3"] {
                border-bottom: none !important;
                margin-bottom: 0;
            }

            /* align images right and shrink them a bit */
            img[class="col-3-img"] {
                /*float: right;
                margin-left: 6px;
                max-width: 130px;*/
            }
        }

    </style>
</head>
<body style="margin:0; padding:0px; padding-bottom:180px; font-family:Open Sans;" bgcolor="#fff" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0"><!-- made bg white for footer -->
<!-- 100% wrapper (grey background) -->
<table border="0" width="100%" height="100%" cellpadding="0" cellspacing="0" bgcolor="#1295FF">
  <tr>
    <td align="center" valign="top" bgcolor="#ebebeb" style="background-color: #1295FF"> <!-- blue side background -->

      <!-- 600px container (white background) -->
      <table border="0" width="600" cellpadding="0" cellspacing="0" class="container" >
        <tr>
          <td class="container-padding" style="" align="center">
            <br>

            <!-- ### BEGIN CONTENT ### -->

            <div style="font-family:Open Sans; font-size: 18px; color: #D03C0F;">
            <img alt="StockUp!" class="logo" src="http://research.stockup.co/personalized_deals/img/logo-email.png">
            </div>
            <br>

            <h3 class="header" style="color:#fff; font-family: Open Sans, sans-serif;font-size:30px; font-weight:400;">Best Deals This Week</h3>
            <p style="color:#fff; font-family: Open Sans, sans-serif; font-size:14px;font-weight:300;">Get the StockUp app save your favorite items!<br>We'll send you updates when they go on sale.</p>

            <br>

            <table border="0" cellpadding="0" cellspacing="0" class="columns-container" style="margin-bottom:20px;">
              <tr>
                <td class="force-col" style="padding-right: 20px;" valign="top">

                    <!-- ### COLUMN 1 ### -->
                    <table align="left" style="display:inline-block; margin-left:40px; width:200px;">
                        <tr>
                            <td align="center" class="card">
                                <div class="content" style=" background-color:#fff; margin-bottom:10px;">
                                    <div class="store-logo" style="float:right;">
                                        <img style="margin:10px;" alt="CVS logo" class="store-logo" src="http://prod-1.yopocket.com:8080/imagestore/getimage?imageId=2013/7/20/18/88358c13-59ef-4a55-9252-8fb3b06594c9&amp;width=40&amp;height=40">
                                    </div>
                                    <div class="list-price" style="font-size:14px; text-align:left; margin:0 10px; text-decoration:line-through;">$10.99</div>
                                    <div class="sale-price" style="text-align:left; margin:0 5px; font-size:36px; color:#6bc22b; font-weight:600;">$6.99</div>
                                    <div class="expiration-date" style="font-size:14px; text-align:left; margin:0 5px;">exp 05/09/2015</div>
                                    <img class="image" alt="image"
                                         src="http://prod-1.yopocket.com:8080/imagestore/getimage?imageId=2014/3/17/22/b705e373-fcf3-4d2d-b7f0-bb366531906c&amp;width=120&amp;height=150">

                                    <div style="width:80%; padding-bottom:10px;">Dawn Ultra Dish Soap<br>9 Fl Oz Bottle</div>
                                </div>
                            </td>
                        </tr>
                          <tr>
                            <td align="center" class="card">
                                    <div class="content" style=" background-color:#fff; margin-bottom:10px;">
                                        <div class="store-logo" style="float:right;">
                                            <img style="margin:10px;" alt="CVS logo" class="store-logo" src="http://prod-1.yopocket.com:8080/imagestore/getimage?imageId=2013/7/20/19/9acae2e1-dcda-4209-b2cf-1ef1d1315322&amp;width=40&amp;height=40">
                                        </div>
                                        <div class="list-price" style="font-size:14px; text-align:left; margin:0 5px; text-decoration:line-through;">$4.79</div>
                                        <div class="sale-price" style="text-align:left; margin:0 5px; font-size:36px; color:#6bc22b; font-weight:600;">$3.99</div>
                                        <div class="expiration-date" style="font-size:14px; text-align:left; margin:0 5px;">exp 06/30/2015</div>
                                        <img class="image" alt="image"
                                             src="http://prod-1.yopocket.com:8080/imagestore/getimage?imageId=2013/8/18/12/fcb66878-17c7-4800-b29e-79cbebfafba1&amp;width=120&amp;height=150">
                                        <div style="width:80%; padding-bottom:10px;">Vermont Bread Soft Whole Wheat Bread<br>24 Oz Bag</div>
                                    </div>
                            </td>
                          </tr>
                    </table>



                    <table style="display:inline-block; width:200px; margin-left:10px;" align="right">
                        <tr>
                            <td align="center" class="card" align="right">
                                <div class="content" style=" background-color:#fff; margin-bottom:10px;">
                                    <div class="store-logo" style="float:right;">
                                        <img style="margin:10px;" alt="CVS logo" class="store-logo" src="http://prod-1.yopocket.com:8080/imagestore/getimage?imageId=2013/7/20/19/5b2dae6f-67da-4055-9216-675053c3e274&amp;width=40&amp;height=40">
                                    </div>
                                    <div class="list-price" style="font-size:14px; text-align:left; margin:0 5px; text-decoration:line-through;">$3.99</div>
                                    <div class="sale-price" style="text-align:left; margin:0 5px; font-size:36px; color:#6bc22b; font-weight:600;">$2.99</div>
                                    <div class="expiration-date" style="font-size:14px; text-align:left; margin:0 5px;">exp 04/09/2015</div>
                                    <img class="image" alt="image"
                     src="http://prod-1.yopocket.com:8080/imagestore/getimage?imageId=2014/1/25/9/649db54c-2762-46d5-af18-5d7a04829469&amp;width=120&amp;height=150">

                                    <div style="width:80%; padding-bottom:10px;">Pup-Peroni Lean Beef Flavor Dog Snacks<br>5.6 Oz Bag</div>
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <td align="center" class="card">
                                    <div class="content" style=" background-color:#fff; margin-bottom:10px; ">
                                        <div class="store-logo" style="float:right;">
                                            <img style="margin:10px;" alt="CVS logo" class="store-logo" src="http://prod-1.yopocket.com:8080/imagestore/getimage?imageId=2013/7/21/3/399849d0-56fe-4d4c-a65c-bf9344986451&amp;width=40&amp;height=40">
                                        </div>
                                        <div class="list-price" style="font-size:14px; text-align:left; margin:0 5px; text-decoration:line-through;">$25.99</div>
                                        <div class="sale-price" style="text-align:left; margin:0 5px; font-size:36px; color:#6bc22b; font-weight:600;">$6.49</div>
                                        <div class="expiration-date" style="font-size:14px; text-align:left; margin:0 5px;">exp 04/09/2015</div>
                                        <img class="image" alt="image"
                                             src="http://prod-1.yopocket.com:8080/imagestore/getimage?imageId=2014/2/1/5/0a84bb69-abbb-4192-b796-feb4043eae58&amp;width=120&amp;height=150">
                                        <div style="width:80%; padding-bottom:10px;">Keratin Complex Complex Vanilla Bean Deep Conditioner<br>7 Oz Tube</div>
                                    </div>
                            </td>
                        </tr>
                    </table>
                <!-- end -->
                </td>
            </tr>
        </table><!--/ end .columns-container-->
    </td>
</tr>
<tr>
    <td class="container-padding"  style="padding-left: 30px; padding-right: 30px; font-size: 13px; line-height: 20px; font-family: Open Sans, sans-serif; color: #333;" align="left">
        <table border="0" cellpadding="0" cellspacing="0" class="columns-container" style="width:100%; height:82px;">
            <tr>
                <td align="center" class="force-col" style="background-image:url('http://research.stockup.co/personalized_deals/img/btn-email.png'); background-repeat:no-repeat;">
                    <div id="more-savings">
                        <a href="http://stockupsales.com/" style="text-decoration:none;">
                            <div class="show-more" style="color: #fff; font-size: 30px; font-weight:400; text-align:left; margin-left:40px;">Show me more savings!<img style="margin-left:60px;" alt="Show me more savings!" src="http://research.stockup.co/personalized_deals/img/arrow-email.png"></div>
                        </a>
                    </div>
                </td>
            </tr>
        </table>
        <br>
        <table border="0" cellpadding="0" cellspacing="0" class="columns-container" style="width:100%;">
            <tr>
                <td align="left">
                    <div id="app-promo">
                        <h4 style="color:#fff; font-family:Open Sans, sans-serif; font-weight:600; font-size:30px;line-height:1em;">Get the app and save more money on your favorite items!</h4>

                    </div>
                </td>
                <td align="right">
                    <img alt="App favorite." src="http://research.stockup.co/personalized_deals/img/img-faves-email.png">
                </td>
            </tr>
        </table>
        <!-- ### END CONTENT ### -->

    </td>
</tr>
      </table>
      <!--/600px container -->

    </td>
  </tr>
</table>
<!--/100% wrapper-->

</body>
</html>


 """

    # template2 = get_template('mcpy/personal_email.html')
    template2 = get_template('mcpy/personal_email.html')

    # passes mailchimp api key
    m = get_mailchimp_api()

    # getting all the emails from a mailchimp list. i happened to name
    # my list "DEVELOPER_LIST" so, oops?

    lists = m.lists.list({'list_id': DEVELOPER_LIST_ID})
    to = m.lists.members(DEVELOPER_LIST_ID)['data']
    recipients = [recipient['email'] for recipient in to]

    # setting up the email

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "template!"
    msg['From'] = USERNAME
    msg['To'] = ", ".join(recipients)
    msg.preamble = msg['Subject']
    #html_content = render_to_response(template2)
    msg.attach(MIMEText(template, 'html'))

    # using gmail's smtp

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(USERNAME, PASSWORD)
    server.sendmail(USERNAME, recipients, msg.as_string())
    server.quit()

    # I just got lazy here I know...

    return HttpResponse('sent')



