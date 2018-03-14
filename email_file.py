from tabulate import tabulate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import yaml

yml_file_path = 'C:\\Users\\Ronak Shah\\Google Drive\\nsedata\\credentials.yml'

def read_credentials () :
    with open(yml_file_path, 'r') as f:
        content = yaml.load(f)

    return content

def sendEmail(content) :
    doc = read_credentials()
    #Get the credentials from the yaml file
    gmail_user = doc['gmail_client']
    gmail_pwd = doc['gmail_password']
    To = doc['To']
    FROM = gmail_user
    data = content
    #Generate the html body for the email
    html = """
    <html><body><p>Hello Ronak, </p>
    <p>Here is your data:</p>
    {table}
    <p>Regards,</p>
    <p>Ronak Shah</p>
    </body></html>
    """

    html = html.format(table=tabulate(data, headers="keys", tablefmt="html"))

    message = MIMEMultipart(
        "alternative", None, [MIMEText(html, 'html')])
    try :
        message['Subject'] = "Today's rate comparison"
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, To, message.as_string())
        server.close()
        return True
    except :
        return False


def email_main(df) :
   isSuccessfull = sendEmail(df)
