from flask import Flask
app_bismayan= Flask(__name__)

@app_bismayan.route('/hello_page_bismayan')
def hello_world_bismayan():
	return 'Hello_world'


if __name__=='__main__':
	app_bismayan.run(debug=True)

