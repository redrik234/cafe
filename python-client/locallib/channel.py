from locallib import config
from locallib import wavConvert as wc

import tornado.websocket


class ChannelHandler(tornado.websocket.WebSocketHandler):

    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.__conf = config.Config()
    
    def open(self):
        print("New connection")


    def on_message(self, message):
        wc.WavConvert.save(self.__conf.getWavDir() + wc.WavConvert.generateFileName() + '.wav', message)


    def on_close(self):
        print("Connection closed")