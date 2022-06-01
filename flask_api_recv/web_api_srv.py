from flask import Flask;
from flask import request;
import logging
from logging.handlers import RotatingFileHandler
import json


app = Flask(__name__);

@app.route("/")
def helloWorld():
  return "Hello world";

@app.route("/github/pr/req_review", methods=["POST"])
def recvPushrequest():
  req_data = request.get_json()
  #print(req_data)
  print(req_data['data'])
  #resp_data = req_data.
  app.logger.info("request.data ="+str(req_data));
  return "ok";

if __name__ == "__main__":
  handler = RotatingFileHandler('/Users/eygon.park/githubs/python_sandbox/flask_api_recv/logs/api_srv.log', maxBytes=1000000, backupCount=10);
  handler.setLevel(logging.DEBUG);
  formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s");
  handler.setFormatter(formatter);
  app.logger.addHandler(handler);
  app.run(debug=True, host='0.0.0.0', port=5009);