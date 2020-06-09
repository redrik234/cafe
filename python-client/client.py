from locallib import config
from locallib import channel

import tornado.httpserver
import tornado.ioloop
import tornado.web
import socket

app = tornado.web.Application([
    (r'/',
     channel.ChannelHandler)
])

if __name__ == '__main__':
    conf = config.Config()

    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.listen(conf.getPort(), conf.getAddress())

    myIP = socket.gethostbyname(socket.gethostname())
    print('*' * 50)
    print(' ' * 2 + '*** Websocket Server Started at %s***' % myIP)
    print('*' * 50)

    try:
        loop = tornado.ioloop.IOLoop.current()
        loop.start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.current().stop()
