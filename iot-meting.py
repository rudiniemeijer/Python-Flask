from flask import Flask, request
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from iot_basis import Basis, Meting

app = Flask(__name__)

@app.route('/m')
def bewaar_nieuwe_meting():
  meting = request.args.get('meting', default=None, type=float)
  if meting is not None:
    sessie = DBSession()
    nieuwe_meting = Meting(meetwaarde=meting, tijdstempel=datetime.now())
    sessie.add(nieuwe_meting)
    sessie.commit()
    return '<small>('+str(nieuwe_meting.meetwaarde)+','+ \
      str(nieuwe_meting.tijdstempel)+')</small>'
  else:
    return 'Gebruik: <b>/m?meting=</b>waarde'

engine = create_engine("mysql://dbroot:$ecret1@localhost/iot_metingen") 

Basis.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

app.run(debug=True, host='0.0.0.0', port=8088)
