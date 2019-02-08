
from flask import Flask, render_template

# Instantieer object app van klasse Flask
app = Flask(__name__)

# Definieer een route voor /hallo
@app.route('/hallo')
@app.route('/hallo/<naam>')
def hallo(naam=None):
  return render_template('hallo.html', begroetingsnaam=naam)

# Draai de app op http://ip-adres-van-Raspberry-Pi:8088
app.run(debug=True, host='0.0.0.0', port=8088)
