
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn

from random import randint

port = 8084
addr = '0.0.0.0'

sessions = {}
SESSION_ID_LEN = 10


class SessionHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        
        self.cookie = None

        try:
            response = 200
            cookies = self.parse_cookies(self.headers["Cookie"])

            if cookies:
                if 'session_id' in cookies:
                    sid =  cookies['session_id']
                    sessions[sid] += 1
                    content = f''' 
                    <html>
                        <body>
                            <h1> Welcome to Site do samuzinho!!!</h1>
                            <h1> Essa é sua visita numero {sessions[sid]}.</h1>
                            <p> Volte sempre!! </p>
                        </body>
                    </html> 
                    
                    '''
                    
            else:
                content = '''
                <html> 
                    <body> 
                        <h1> Bem vindo ao site do samuzinho!!! </h1>
                        <h1> Esta e sua primeira visita!! </h1>
                        <p> Volte sempre!! </p>
                        <p> Qual o seu nome? </p>
                        <input> </input>

                    </body> 
                
                </html>
                
                '''
                sid = self.generate_sid()
                sessions[sid] = 1
                self.cookie = f'session_id = {sid}'
        





        except:
            response = 404
            content = '<html> <body> <h1> Erro ao processar a pagina, tente novamente!! </h1> </body> </html> '
            
            sid = self.generate_sid()
            sessions[sid] = 1
            self.cookie = f'session_id = {sid}'


        self.send_response(response)
        self.send_header('Content-type', 'text/html')

        if self.cookie:
            self.send_header('Set-Cookie', self.cookie)
        
        self.end_headers()

        self.wfile.write(bytes(content, 'utf-8'))
        return


    def generate_sid(self):
        return "".join(str(randint(0,9)) for _ in range(SESSION_ID_LEN) )

    def parse_cookies(self, cookie_list):
        return dict(((c.split("=")) for c in cookie_list.split(";"))) if cookie_list else {}

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass

def main():
    try:
        server = HTTPServer((addr, port), SessionHandler)
        server.serve_forever()

    except KeyboardInterrupt:
        print('Exitting server')
        server.socket.close()

if __name__ == '__main__':
    main()