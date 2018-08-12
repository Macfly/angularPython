import logging
import asyncio

import aiohttp_cors
from aiohttp import web
import socketio
from market_engine.market import RandomMarket, simulate_market

sio = socketio.AsyncServer(async_mode='aiohttp')
app = web.Application()
sio.attach(app)
routes = web.RouteTableDef()
market = RandomMarket()

logging.basicConfig(level=logging.DEBUG)


async def send_market_price():
    while True:
        await sio.sleep(1)
        stock = simulate_market()
        await sio.emit('stock', stock, room=stock['symbol'])


@sio.on('connect')
async def connect(sid, message):
    sio.start_background_task(send_market_price)


@sio.on('join')
async def join(sid, room):
    sio.enter_room(sid, room)
    stock = simulate_market(room)
    await sio.emit('stock', stock, room=stock['symbol'])


@sio.on('leave')
async def leave(sid, room):
    print("leave")
    sio.leave_room(sid, room)


@sio.on('disconnect')
async def disconnect(sid):
    print('Client disconnected')


@routes.get('/api/market')
async def get_random_sotck(request):
    print('sending random price get')
    stock = simulate_market()
    return web.json_response(stock)


@routes.get('/api/market/{stock}')
async def get_stock(request):
    print('sending stock from get')
    stock = simulate_market(request.match_info['stock'])
    return web.json_response(stock)


@routes.post('/api/market')
async def get_stock_post(request):
    print('sending stock from POST')
    data = await request.json()
    stock = simulate_market(data['stock'])
    return web.json_response(stock)


# Configure default CORS settings.
cors = aiohttp_cors.setup(app, defaults={
    "*": aiohttp_cors.ResourceOptions(
        allow_credentials=True,
        expose_headers="*",
        allow_headers="*",
        allow_methods=["POST", "PUT"]
    )
})

if __name__ == '__main__':
    app.router.add_routes(routes)
    for route in list(app.router.routes()):
        if route.resource.canonical != '/socket.io/':
            cors.add(route)
    print('starting')
    web.run_app(app, port=5000)
