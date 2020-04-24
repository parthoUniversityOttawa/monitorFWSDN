import csv,json
import parser
from flask import Flask, json

#companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]
#test = [{"switch": 1, "thoughput": "Company One"}, {"delay": 0, "switch name": "xxxxxx"}]

api = Flask(__name__)


#@api.route('/test', methods=['GET'])
#def get_test():
#  return json.dumps(test)

@api.route('/thoughput', methods=['GET'])
def get_thoughtput():
  return  parser.getThoughput()

@api.route('/packetloss', methods=['GET'])
def get_packetloss():
  return  parser.getPacketLoss()

@api.route('/delay', methods=['GET'])
def get_delay():
  return  parser.getDelay()
  

#if __name__ == '__main__':
api.run()
