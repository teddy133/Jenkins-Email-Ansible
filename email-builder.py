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











































































































































































































































































































































































































































# A Cloud Guru - Data Generating Script - Weatherstation_data
# Author - Adrian Cantrill - 2016 - v1
# Aug 2018 problems with 'date' type data being passed to Boto3. Treatment by converting to string during generation RL.

## PREREQS
##          configured AWS tools
##          installed python2.7+
##          installed boto3 (pip install boto3)
##          Installed tqdm module
##          'loadmin' AWS configuration profile - with admin rights
##          _retry.json file from lesson files - adjusted for 1mil+ auto retries
##              for retryable operations

# import boto3, random, tqdm, time, botocore, uuid
# from botocore.exceptions import ClientError
# from tqdm import trange
# from tqdm import tqdm
#
# # Boto init
# loadmin_session = boto3.Session(profile_name='loadmin')
# db_c = loadmin_session.client('dynamodb')
# db_r = loadmin_session.resource('dynamodb')
#
# #------------------------------------------------------------------------------
# def strTimeProp(start, end, format, prop):
#     """Get a time at a proportion of a range of two formatted times.
#     start and end should be strings specifying times formated in the
#     given format (strftime-style), giving an interval [start, end].
#     prop specifies how a proportion of the interval to be taken after
#     start.  The returned time will be in the specified format.
#     """
#     stime = time.mktime(time.strptime(start, format))
#     etime = time.mktime(time.strptime(end, format))
#     ptime = stime + prop * (etime - stime)
#     return time.strftime(format, time.localtime(ptime))
# #------------------------------------------------------------------------------
# def randomDate(start, end, prop):
#     return strTimeProp(start, end, '%Y%m%d%H%M', prop)
# #------------------------------------------------------------------------------
# def d_table(): # define table configuration
#     table_config={}
#     ## starting provisioned throughput settings for each table
#     table_config['ProvisionedThroughput'] = { 'ReadCapacityUnits' : 5, 'WriteCapacityUnits' : 5 }
#     table_config['KeySchema'] = [
#             {'AttributeName' : 'station_id', 'KeyType' : 'HASH'}, \
#             {'AttributeName' : 'dateandtime', 'KeyType' : 'RANGE'}, \
#     ]
#     table_config['AttributeDefinitions'] = [
#         {'AttributeName' : 'station_id', 'AttributeType' : 'S'},\
#         {'AttributeName' : 'dateandtime', 'AttributeType' : 'S'},\
#     ]
#     table_config['TableName'] = 'weatherstation_data'
#
#     return table_config
# #------------------------------------------------------------------------------
# def c_table (c): # create dynamo DB tables
#     try:
#         print "INFO :: Creating %s Table....." % c['TableName']
#         db_r.create_table(**c)
#         print "INFO :: Waiting for completion..."
#         db_r.Table(c['TableName']).wait_until_exists()
#     except botocore.exceptions.ClientError as e:
#         if e.response['Error']['Code'] == "ResourceInUseException":
#             print "INFO :: WeatherstationInc %s Table exists, deleting ...." % c['TableName']
#             db_r.Table(c['TableName']).delete()
#             print "INFO :: Waiting for delete.."
#             db_r.Table(c['TableName']).wait_until_not_exists()
#             c_table (c)
#         else:
#             print "Unknown Error"
# #------------------------------------------------------------------------------
# def p_table (stations, datapoints): # Populate Table
#     with db_r.Table('weatherstation_data').batch_writer() as batch:
#         for station in trange(stations, desc='Stations'):
#             for datapoint in trange(datapoints, desc='Datapoints'):
#                 item = item_gen(station)
#                 batch.put_item(Item=item)
# #------------------------------------------------------------------------------
# def item_gen(station_id): # Generate ITEM for a given station ID
#     i={}
#     i['station_id'] = str(station_id)
#     i['dateandtime'] = str(randomDate("201601010000", "201606302359", random.random()))
#     i['rainfall'] = random.randrange(0,10)
#     i['temperature'] = random.randrange(10,30)
#     i['uvindex'] = random.randrange(1,9)
#     i['windspeed'] = random.randrange(1,20)
#     i['lightlevel'] = random.randrange(1,100)
#     return i;
# #------------------------------------------------------------------------------
# if __name__ == "__main__":
#     num_of_stations=10
#     num_of_datapoints=100
#     print "Re-creating weatherstation_data table,"
#     table_config = d_table() # create table config.
#     t_conf=d_table() # generate table config
#     c_table(t_conf) # create table, with the above config
#     p_table(num_of_stations, num_of_datapoints) # populate the table with X rows
#     print('INFO :: Data Entry Complete')






















# db_testTable.put_item(
#     Item={
#         "name": "Kristen",
#         "Occuppation": "Developer",
#         "Salary": 9000,
#         "Location": "India"
#     }
# )

# def d_table(): # define table configuration
#     table_config={}
#     ## starting provisioned throughput settings for each table
#     table_config['ProvisionedThroughput'] = { 'ReadCapacityUnits':5, 'WriteCapacityUnits': 5}
#     table_config['KeySchema'] = [
#             {'AttributeName' : 'station_id', 'KeyType' : 'HASH'}, \
#             {'AttributeName' : 'dateandtime', 'KeyType' : 'RANGE'}, \
#     ]
#     table_config['AttributeDefinitions'] = [
#         {'AttributeName' : 'station_id', 'AttributeType' : 'S'},\
#         {'AttributeName' : 'dateandtime', 'AttributeType' : 'S'},\
#     ]
#     table_config['TableName'] = 'weatherstation_data'
#
#     return table_config








#
# weather_table={}
#
# weather_table['ProvisionedThroughput'] = {'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
# weather_table['TableName'] = 'weather_table'
# weather_table['AttributeDefinitions'] = [
#     {"AttributeName":"name", "AttributeType":'S'}
# ]
# weather_table['KeySchema'] = [
#     {'AttributeName':'name', 'KeyType':'HASH'}
# ]
#
#
# dynamodb.create_table(**weather_table)
