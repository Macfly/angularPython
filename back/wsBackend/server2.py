import logging
import threading

from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from flask_debugtoolbar import DebugToolbarExtension
from flask_socketio import SocketIO, join_room, leave_room

from market_engine.market import RandomMarket, simulate_market

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
CORS(app)
toolbar = DebugToolbarExtension(app)
market = RandomMarket()
thread = None
thread_lock = threading.Lock()

logging.getLogger('flask_cors').level = logging.DEBUG


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('connect')
def connect():
    global thread
    print('Client connected')
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=send_market_price)


@socketio.on('join')
def on_join(room):
    print('join room: ' + room)
    join_room(room)
    stock = simulate_market(room)
    socketio.emit('stock', stock, room=stock['symbol'])


@socketio.on('leave')
def on_leave(data):
    print("leave")
    leave_room(data)


@socketio.on('disconnect')
def disconnect():
    print('Client disconnected')


def send_market_price():
    while True:
        print('sending price ws')
        stock = simulate_market()
        socketio.emit('stock', stock, room=stock['symbol'])
        socketio.sleep(1)


@app.route('/api/market', methods=['GET'])
def get_random_sotck():
    print('sending random price get')
    stock = simulate_market()
    return jsonify(stock)


@app.route('/api/market/<stock>')
def get_stock(stock):
    print('sending stock from get')
    stock = simulate_market(stock)
    return jsonify(stock)


@app.route('/api/market', methods=['POST'])
def get_stock_post():
    print('sending stock from POST')
    stock = simulate_market(request.json['stock'])
    return jsonify(stock)


if __name__ == '__main__':
    print('starting')
    socketio.run(app, debug=True, log_output=True)
