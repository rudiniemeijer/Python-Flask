from flask import Flask, url_for
app = Flask(__name__)
@app.route('/')
def index():
    return 'indexpagina'

@app.route('/login')
def login():
    return 'login'

@app.route('/gebruiker/<gebruikernaam>')
def profielpagina(gebruikernaam):
    return '{}\'s profielpagina'.format(gebruikernaam)

app.run(debug=True, host='0.0.0.0', port=8088)

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profielpagina', gebruikernaam='Joep Meloen'))
    

