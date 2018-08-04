import logging
import threading

import socketio
import eventlet
import eventlet.wsgi
from flask import Flask, jsonify
from flask_cors import CORS
# from flask_mongoengine import MongoEngine
# from flask_restful import Api, Resource

from market_engine.market import RandomMarket

sio = socketio.Server()
app = Flask(__name__)
CORS(app)
market = RandomMarket()
# api = Api(app)
# app.config['MONGODB_SETTINGS'] = {
#     'db': 'rtproj',
#     'host': 'localhost',
#     'port': 27017
# }
# db = MongoEngine(app)

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s|%(name)s|%(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')
datefmt = '%m/%d/%Y %I:%M:%S %p'
logger = logging.getLogger('server')


@app.route('/api/market', methods=['GET'])
def get_market_positions():
    price = market.update_market()
    logger.debug('get market positions')
    return jsonify(price)


@sio.on('connect')
def connect(sid, environ):
    logger.debug('Client connected')
    print('connect ', sid)


def send_market_price():
    threading.Timer(5.0, send_market_price).start()
    logger.debug('send price')
    sio.emit('market', market.update_market())


# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}
#
#
# api.add_resource(HelloWorld, '/test')
#
# @sio.on('chat message', namespace='/chat')
# def message(sid, data):
#     logger.debug('message from {sid}: {data}', sid, data)
#     sio.emit('reply', room=sid)
#
# @sio.on('connect', namespace='/chat')
# def connect(sid, environ):
#     logger.debug('Client connected  SID: {sid}', sid)
#
#
# @sio.on('disconnect', namespace='/chat')
# def disconnect(sid):
#     print('disconnect ', sid)
#     logger.debug('{sid} disconnect', sid)

if __name__ == '__main__':
    logger.debug('Starting the app')
    app = socketio.Middleware(sio, app)
    send_market_price()
    eventlet.wsgi.server(eventlet.listen(('', 8080)), app)
