import datetime
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# HOCANIN KODU


def send(filename):
    # 587=port
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('***', 'BA_Python_2021')

    from_address = '***'
    to_address = '***'

    # to_list = ['***',
    #            "***"]

    subject = "YFscrapper'dan mail geldi! " + datetime.datetime.now().strftime('%H:%M:%S')

    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    # today = str(datetime.date.today()) + ".csv"
    my_attachment = open(filename, 'rb')

    part = MIMEBase('application', 'octet-stream')
    # pdf dosyası göndermek istersek:
    # part = MIMEBase('application', 'pdf')
    part.set_payload(my_attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment;filename=' + filename)
    msg.attach(part)

    body = """<b>Selamlar<b> <hr/> 
    Python Programından mail gönderiyoruz. <br/> 
    Aleyna <hr/>
    <a href=https://www.koredenkozmetik.com.tr/collections/tum-urunler>Visit Page</a>
    """
    msg.attach(MIMEText(body, 'html'))
    message = msg.as_string()

    # for to_single in to_list:
    server.sendmail('***', to_address, message)

    # msg = MIMEText(message, "plain", "UTF-8")
    # server.sendmail(from_address, to_address, msg.as_string())

    # for to_single in to_list:
    #    server.sendmail(from_address, to_list, msg.as_string())

    server.quit()
