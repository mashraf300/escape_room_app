import socket
import threading
import time
import pickle


class Server:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 12345

    def __init__(self):
        server_config = (self.host, self.port)
        self.server.bind(server_config)
        self.server.listen(5)

        self.clientsocket, self.addr = self.server.accept()
        print("Connecting to ", self.addr)


    def receive_message(self):
        try:
            while True:
                data = self.clientsocket.recv(1024)
                data = pickle.loads(data)
                time.sleep(0.001)

                if(data['Key'] == 1 and data['Map'] != 1):
                    clue = 'Use the key on the rightmost door'
                elif (data['Key'] == 1 and data['Map'] == 1):
                    clue = "Check under the map"
                elif (data['Map'] == 1 and data['Flashlight'] == 1):
                    clue = "Use the flashlight on the map"
                elif (data['Key'] == 2 and data['Flashlight'] == 1):
                    clue = "Look for the rusty lock"
                else:
                    clue = "Just keep searching"

                self.clientsocket.send(clue.encode())

        except Exception as ex:
            print(ex)

    def chat(self):
        self.rec_msg_thread = threading.Thread(target=self.receive_message)
        self.rec_msg_thread.daemon = True
        self.rec_msg_thread.start()


if __name__ == '__main__':
    server_side = Server()
    server_side.chat()
    server_side.rec_msg_thread.join()
    server_side.server.close()