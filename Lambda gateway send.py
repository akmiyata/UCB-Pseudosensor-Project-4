import json
import boto3
from decimal import Decimal
dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table = dynamodb.Table('WeatherTable')
#Fix issue with json and decimals
class DecimalEncoder(json.JSONEncoder):
def default(self, obj):
if isinstance(obj, Decimal):
return float(obj)
return json.JSONEncoder.default(self, obj)
def lambda_handler(event, context):
# TODO implement
response = table.scan()
#Gimme my stuff
return {
'statusCode': 200,
'body': json.dumps(response['Items'], cls=DecimalEncoder)
}
