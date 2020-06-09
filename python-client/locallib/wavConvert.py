import time, datetime

class WavConvert:

    @staticmethod
    def save(fileName, data):
        with open(fileName, mode='bx') as f:
            f.write(data)

    @staticmethod
    def generateFileName():
        dt = datetime.datetime.now()
        value = datetime.datetime.fromtimestamp(time.mktime(dt.timetuple()))
        return 'record-' + value.strftime('%Y-%m-%d-%H-%M-%S')

