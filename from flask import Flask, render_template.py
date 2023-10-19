from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import MySQLdb.cursors
from cryptography.fernet import Fernet ## library used for encryption and decryption

secret_key = Fernet.generate_key()
cipher_suite = Fernet(secret_key)

print ("Hello World")
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'codingthunder'

mysql = MySQL(app)

@app.route('/', methods =['GET', 'POST'])
def register():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
		name = request.form['username']
		email = request.form['email']
		PhoneNumber = request.form['PhoneNumber']
		data = PhoneNumber.encode('utf-8')
		hashed_password  = cipher_suite.encrypt(data)

		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		
		cursor.execute('INSERT INTO user_info VALUES (NULL, % s, % s, % s)', (name,email, hashed_password,  ))
		decrypted_data = cipher_suite.decrypt(hashed_password).decode('utf-8')
		print (decrypted_data)
		mysql.connection.commit()
		msg = 'You have successfully registered !'
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('register.html', msg = msg)

if __name__ == "_main_":
	app.run(debug=True)