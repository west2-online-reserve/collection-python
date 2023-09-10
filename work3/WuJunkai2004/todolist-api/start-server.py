from imp  import load_source
from io   import StringIO
from http import server

import os
import sys
import vercel

def Start(handler = vercel.API, port = 8080):
    server.test(
        HandlerClass = handler,
        ServerClass = server.ThreadingHTTPServer,
        port = port,
        bind = None
    )

class handler(vercel.API):
    def vercel(self, url, data, headers):
        print('url === '+ url)
        if(os.path.isdir(url)):
            self.send_code(200)
            self.send_text( '\n'.join(os.listdir(url)) )
        elif(os.path.isfile(url)):
            if(os.path.splitext(url)[1]=='.py'):
                vercel.ErrorStatu(self, 403)
            else:
                self.send_code(200)
                self.send_file(url)
        else:
            if(os.path.isfile(url + '.py')):
                mod = load_source(url,url + '.py')
                mod.handler.vercel(self, url, data, headers)
            else:
                vercel.ErrorStatu(self, 404)

if(__name__=='__main__'):
    Start( handler )