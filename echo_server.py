import asyncio

class EchoServerClientProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print(f'Connection made from {peername}')
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        peername = self.transport.get_extra_info('peername')
        print(f'Received from client {peername[1]}: {message}')

        # and now echoing back
        self.transport.write((f'Echoing back: {message}').encode())


loop = asyncio.get_event_loop()
coro = loop.create_server(EchoServerClientProtocol, '127.0.0.1', 8888)
server = loop.run_until_complete(coro)

print(f'Serving on {server.sockets[0].getsockname()}')

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
print('Closing server')
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
