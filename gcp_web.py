#!/usr/bin/env python
import cherrypy
import threading,subprocess
import os
config = {
    'global' : {
        'server.socket_host' : '0.0.0.0',
        'server.socket_port' : 8080
    }
}
class HelloWorld(object):
    def __init__(self):
        subprocess.Popen(['python /home/vr760/request.py'],shell=True)
        print("hihi")
    @cherrypy.expose
    def index(self):
        # <input type="button" value="goalA" onclick="location.href='192.168.3.3:8080/goalA_to'">
        # ERIC https://github.com/VirtuosoEric/robot_web_service/blob/pn60/home.html
        f = open("buttonsellector.html", "r")
        return f

    @cherrypy.expose
    def upload(self, ufile):
        # Either save the file to the directory where server.py is
        # or save the file to a given path:
        # upload_path = '/path/to/project/data/'
        upload_path = os.path.dirname(__file__)
        print(upload_path)
        # Save the file to a predefined filename
        # or use the filename sent by the client:
        # upload_filename = ufile.filename
        upload_filename = 'saved.png'

        upload_file = os.path.normpath(
            os.path.join(upload_path, upload_filename))
        size = 0
        with open(upload_file, 'wb') as out:
            while True:
                data = ufile.file.read(8192)
                if not data:
                    break
                out.write(data)
                size += len(data)
        out = '''
File received.
Filename: {}
Length: {}
Mime-type: {}
''' .format(ufile.filename, size, ufile.content_type, data)
        return out

if __name__ == '__main__':
    # print("hihi")
    # while True:
    #     r=os.popen('uptime --p').read()
    #     now=int(r[3]+r[4])
    #     if now>1:
    #         subprocess.Popen(['python /home/vr760/request.py'],shell=True)
    #         break
    cherrypy.quickstart(HelloWorld(), '/',config)
