from flask import Flask

# Instantieer object app van klasse Flask
app = Flask(__name__)

# Definieer een route
@app.route('/')
def hallo_wereld():
  return 'Hallo wereld!'

# Draai de app op http://ip-adres-van-Raspberry-Pi:8088
app.run(debug=True, host='0.0.0.0', port=8088)
