from flask import Flask,request,render_template
import boto3
import uuid
import os
app = Flask(__name__)
client= boto3.resource(
    'dynamodb',
    aws_access_key_id=os.environ['AWS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_ACCESS_KEY'],
    region_name= 'eu-central-1'
)
table = client.Table('tezdemo')
@app.route('/', methods=['GET'])
def showItems():
	#uuid = uuid.uuid4()
	items=table.scan()['Items']
	#print(items)
	return render_template('show.html', list = Items)

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0',port=8080)