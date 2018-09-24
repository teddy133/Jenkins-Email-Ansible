import smtplib
from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = "<your REAL email>"
PASSWORD = r"<your REAL email password>"
BODY = "<file of text with template variables>"
CONTACTS = "<Text file of contacts>"
STMP_CLIENT = "<your stmp mailer address>" #for example for gmail you would use 'smtp.gmail.com' however you need to find your for your custom provider

def get_contacts(filename):
    """
        Return two lists names, emails containing names and email addresses
        read from a file specified by filename.
        """
    
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails


def read_template(filename):
    """
        Returns a Template object comprising the contents of the
        file specified by filename.
        """
    
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


def main():
    names, emails = get_contacts(CONTACTS)  # read contacts
    message_template = read_template(BODY)
    
    # set up the SMTP server
    s = smtplib.SMTP_SSL(STMP_CLIENT)
    s.login(MY_ADDRESS, PASSWORD)
    
    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()  # create a message
        
        # add in the actual person name to the message template
        # create your own custom Exhange variable templates
        message = message_template.substitute(PERSON_NAME=name.title())
        
        # Prints out the message body for our sake
        print(message)
        
        # setup the parameters of the message
        msg['From'] = MY_ADDRESS
        msg['To'] = email
        msg['Subject'] = "This is TEST"
        
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        
        # send the message via the server set up earlier.
        s.sendmail(MY_ADDRESS, email, msg.as_string())
    s.quit()




if __name__ == '__main__':
    main()