import socket, json
from enum import Enum

class XSMessageType(Enum):
        Notification = 1
        MediaPlayer = 2

class XSIconType(str, Enum):
        Default = 'default'
        Error = 'error'
        Warning = 'warning'

class XSAudioDefault(str, Enum):
        Default = 'default'
        Error = 'error'
        Warning = 'warning'

class XSOMessage:
    def __init__(self, index=0, messageType=XSMessageType.Notification, volume=0.7, audioPath=XSAudioDefault.Default, timeout=3.0,
    title='', content='', icon=XSIconType.Default, height=175.0, opacity=1.0, useBase64Icon=False, sourceApp=''):
        self.index = index
        self.messageType = messageType
        self.volume = volume
        self.audioPath = audioPath
        self.timeout = timeout
        self.title = title
        self.content = content
        self.icon = icon
        self.height = height
        self.opacity = opacity
        self.useBase64Icon = useBase64Icon
        self.sourceApp = sourceApp

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, val):
        if val < 0.0 or val > 1.0 :
            raise ValueError("Volume must be between 0.0 and 1.0")
        else:
            self._volume = val

    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, val):
        if val < 0.0 or val > 60.0:
            raise ValueError("Timeout must be between 0.0 and 60.0")
        else:
            self._timeout = val

    @property
    def opacity(self):
        return self._opacity

    @opacity.setter
    def opacity(self, val):
        if val < 0.0 or val > 1.0 :
            raise ValueError("Opacity must be between 0.0 and 1.0")
        else:
            self._opacity = val
    
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, val):
        if val < 0.0 or val > 250.0 :
            raise ValueError("Height must be between 0.0 and 250")
        else:
            self._height = val

    def json_bytes(self):
        obj = self.__dict__
        obj['volume'] = self.volume
        obj['timeout'] = self.timeout
        obj['opacity'] = self.opacity
        obj['height'] = self.height
        return json.dumps(obj).encode('utf-8')


class XSNotifier:
    def __init__(self, ip="127.0.0.1", port=42069):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_notification(self, noti):
        self.sock.sendto(noti.json_bytes(), (self.ip, self.port))
