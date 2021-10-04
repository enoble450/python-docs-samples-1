from flask import Flask, request, redirect
from datetime import datetime
import pytz
import os
from google.cloud import datastore
app = Flask(__name__)
dataclient = datastore.Client()
def addVisitor():
	ent = dataclient.key('data','visitors')
	total = dataclient.get(key=ent)
	if total:
		total['total'] += 1
		dataclient.put(total)
	else:
		total = datastore.Entity(key=ent)
		total['total'] = 0
		dataclient.put(total)
@app.route('/')
def main_page():
	ent = dataclient.key('data', 'posts')
	posts = dataclient.get(key=ent)
	article = ""
	with open('article.html','r') as page:
		article = page.read()
	html = ""
	if posts:
		for post in posts['posts']:
			array = json.loads(post)
			raw = article.replace("!content!", array[0])
			raw = raw.replace("!time!", array[1])
			raw = raw.replace("!title!)", array[2])
			html += raw
	else:
		return 'No Posts!'
@app.route('/version')
def vers():
    return 'This is app version B'
@app.route('/instance')
def getid():
	instanceid = os.getenv('GAE_INSTANCE')
	return str(instanceid)
@app.route('/version-id')
def getversionid():
	addVisitor()
	versionid = os.getenv('GAE_VERSION')
	return str(versionid)
@app.route('/visitors')
def getVisitor():
	addVisitor()
	ent = dataclient.key('data','visitors')
	total = dataclient.get(key=ent)
	if total:
		return 'Total visitors: ' + str(total['total'])
	else:
		return 'Total Broke!'
@app.route('/editor')
def edit_page():
	with open('editor.html','r') as page:
		return page.read()
@app.route('/submit', methods = ['POST'])
def submit_post():
	password = request_form['pass']
	if password = "mySuperAwesomePassword":
		content = request.form['content']
		title = request.form['title']
		timeutc_n = datetime.utcnow()
		timeutc = timeutc_n.replace(tzinfo=pytz.utc)
		timelocal = timeutc.astimezone(pytz.timezone('America/Los_Angeles'))
		time = str(timelocal)
		post = json.dumps([content, title, time])
		ent = dataclient.get(key=ent)
		if posts:
			posts['posts'] = [post] + posts['posts']
			dataclient.put(posts)
		else:
			posts = datastore.Entity(key=ent)
			posts['posts'] = [post]
			dataclient.put(posts)
		return redirect('/')
	else:
		return redirect('/'
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
