from socket import *
import random
import json
from time import sleep
from datetime import datetime

serverName = "255.255.255.255"
serverPort = 10000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)


while True:
    data = {
        "SensorName": "xiao speedtrap",
        "Speed": random.randint(50, 120) ,
        "DataTime": str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    }
    message = json.dumps(data)
    clientSocket.sendto(message.encode(),(serverName, serverPort))
    sleep(random.randint(1,5))