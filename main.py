# This is the code for my stonklat.com WEBISTE
# I decided to build it with flask because i just prefer it this way
# I also decided to host it on replit for now, because its just the cheapest option for me

# Import packages
from flask import Flask, send_file, render_template, url_for, Blueprint

# Define the app
app = Flask('stonklat')

bp = Blueprint("website", __name__, url_prefix="/", 
template_folder="templates", static_folder="static")
def website():
    return bp

# root route of the website
@app.route('/')
def hello_world():
  return render_template('index.html')

# Communism routes
@app.route('/communism')
def communism_root():
  return render_template('communism/communism.html')
@app.route('/communism/manifesto.txt')
def manifesto():
  return send_file('communist.txt')
@app.route('/communism/anthem')
def communism_anthem():
  return render_template('communism/anthem.html')
  
# Discord Bot routes
@app.route('/bot')
def bots():
  return render_template('bot/index.html')
@app.route('/bot/commands/kandalf')
def kandalf_commands():
  return render_template('bot/commands/kandalf.html')
@app.route('/bot/commands/hikairus')
def hikirusbot_commands():
  return render_template('bot/commands/hikairus.html')
@app.route('/bot/source/hikairus')
def hikirusbot_source():
  return render_template('bot/source/Shikairus.html')

@app.route('/rock')
def return_files_tut():
	try:
		return send_file('vid.mp4', attachment_filename='video.mp4')
	except Exception as e:
		return str(e)

# Handle the 404 exception
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return '<title>404 - Not found</title><h1>404 Not found</h1>\n<h2>The url you entered has not been found on the STONKLAT servers.</h2>'


# Files

@app.route('/files/kandalf.png')
def kandalf_img():
	return send_file('kandalf.png')

@app.route('/files/shrek.png')
def shrek_img():
	return send_file('shreck.ico')

@app.route('/files/papyrus.mp3')
def papyrus_mp3():
	return send_file('papyrus.mp3')
  
# Start Flask 
app.run(host='0.0.0.0', port=8080)