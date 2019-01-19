from flask import Flask,request,redirect
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
@app.route('/save', methods=['POST'])
def saveToDynamoDb():
	#uuid = uuid.uuid4()
	message = request.form['message']
	table.put_item(Item={
		'uuid':str(uuid.uuid4()),
		 'message':message
	})
	return redirect("http://f1cfca943-4807-470d-8e1c-1befddb437d9.285c5af8-3a7f-4a1a-bccd-4cfb0ffe2c82.app.fahri.pw/",code=200)

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0',port=8080)
