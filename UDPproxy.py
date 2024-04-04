from socket import *
import requests
import json
ip=""
serverPort = 10000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((ip, serverPort))
print("The server is ready")


while True: 
    try:
        data, addr = serverSocket.recvfrom(1024) 
        print("Received data :", data.decode())
        response = requests.post('http://localhost:5155/api/Fotovogns', json=json.loads(data.decode()))
        
    except Exception as e:
        print("Error sending to REST service:", e)