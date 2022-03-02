import boto3
import json
import time
from pprint import pprint
from decimal import Decimal
# Get the service resources
sqs = boto3.resource('sqs')
dynamodb= boto3.resource('dynamodb')
# Get the queue
queue = sqs.get_queue_by_name(QueueName='5318_Proj1')
table_name = 'WeatherTable'
#DynamoDB client code
dynamodb_client = boto3.client('dynamodb')
table = dynamodb.Table('WeatherTable')
def lambda_handler(event, context):
# Put item into db, combining sqs and dynamoDB resources
message_bodies=[]
messages_to_delete = []
# Put item into db, combining sqs and dynamoDB resources
for message in queue.receive_messages(MaxNumberOfMessages=10):

#Process message body until there are none left
weatherItem = json.loads(message.body, parse_float=Decimal)
message_bodies.append(weatherItem)
#Add message to delete
messages_to_delete.append({'Id': message.message_id,'ReceiptHandle': message.receipt_handle})

for i in message_bodies:
response = table.put_item(Item=i)

if len(messages_to_delete) == 0:
break
else:
delete_response = queue.delete_messages(Entries=messages_to_delete)