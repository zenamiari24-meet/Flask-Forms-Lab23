from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "zena"
password = "1234"
facebook_friends=["Yasmeenah","Salma","Rita", "Lilia", "Watan", "Bandora"]
friends_friends="zena"


@app.route('/', methods = ['GET','POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		name = request.form['username']
		p = request.form['password']
		if name == username and p == password:
			return redirect(url_for('home'))
		else:
			return render_template('login.html')


@app.route('/home')
def home():
	facebook_friends=["Yasmeenah","Salma","Rita", "Lilia", "Watan", "Bandora"]
	return render_template('home.html', friends =facebook_friends)


@app.route('/friend_exists/<string:name>')
def friend_exists(name):
	if name in facebook_friends:
		return render_template('friend_exists.html', is_friend=True, n=name)
	else:
		return render_template('friend_exists.html', is_friend=False, n=name)






if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
