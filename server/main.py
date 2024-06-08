from flask import Flask, render_template, send_file
from threading import Thread
import ssl
import socket
# from flask_socketio import SocketIO, emit


SERVER_PORT = 8080
SERVER_HOST = socket.gethostbyname(socket.gethostname())

server = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
# server_socket = SocketIO(server)
server_socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM,socket.BTPROTO_RFCOMM)
wallet_connection_status = False


# context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# context.load_default_certs()


for i in range(0,20):
    try:
        Thread(target=server_socket.connect(('c0:2e:25:54:c2:38', i))).start()
        print(f"[ + ] Connected @ CH {i} !")
        wallet_connection_status = True
        break
    except:
        print(f"{i} --> Not available")
        wallet_connection_status = False




def wallet_checking():
    global wallet_connection_status
    while True:
        server_socket.send("1".encode('utf-8'))
        if (server_socket.recv(1024)):
            wallet_connection_status = True
        else:
            wallet_connection_status = False
            print("lost connection")
            server_socket.close()
        return wallet_connection_status

@server.route("/connections.js", methods=["GET", "POST"])
def javascript():
    return render_template("connections.js")
@server.route("/style.css", methods=["GET", "POST"])
def stylesheet():
    return render_template("style.css")
@server.route("/background.jpeg", methods=["GET", "POST"])
def background():
    return send_file("templates/background.jpeg")
@server.route("/logo.jpeg", methods=["GET", "POST"])
def logo():
    return send_file("templates/logo.jpeg")

@server.route("/alert.mp3", methods=["GET", "POST"])
def alert_audio():
    return send_file("templates/alert.mp3", as_attachment=False)
@server.route("/check", methods=["GET", "POST"])
def check_wallet():
    return str(wallet_connection_status)
    # return status


@server.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    Thread(target=wallet_checking).start()
    server.run(SERVER_HOST, SERVER_PORT, debug=True, ssl_context='adhoc')