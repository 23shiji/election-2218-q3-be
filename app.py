from flask import (
  Flask,
  request,
  jsonify
)
from schema import (
  Schema,
  Use
)
import facade
import model
from hashlib import sha256
import os

app = Flask(__name__)

@app.route('/')
def index():
  return jsonify(dict(
    message = 'ok'
  ))

submit_schema = Schema({
  'party_name': str,
  'independent_candidates': [str]
})
@app.route('/submit', methods=['POST'])
def submit():
  req = request.get_json()
  submit_schema.validate(req)
  ip = sha256(request.remote_addr.encode('ascii')).hexdigest()
  if facade.exists_ip(ip) and os.environ.get('env') == 'prod':
    return jsonify({
      'success': False,
      'message': '该IP已投过票了'
    })
  facade.save_record(ip, req)
  return jsonify({
    'success': True,
    'message': '成功'
  })

@app.route('/result')
def result():
  return jsonify(model.get_lastest_history())