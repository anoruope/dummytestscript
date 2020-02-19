import paho.mqtt.client as mqtt
from dotenv import load_dotenv
from random import seed
from random import randint
import json
import os
from os import path
import time

val1 = "Harz"
val2 = "Haerter"
val3 = "fuellstoff1"
val4 = "fuellstoff2"
val5 = "fuellstoff3"
arrd = [val1,val2,val3,val4,val5]
mqtturl = os.getenv("MQTT_URL")
mqttport = int(os.getenv("MQTT_PORT"))
instance_name = os.getenv("INSTANCE_NAME")

def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag = True
        print("connected Returned code =",rc)
    else:
        client.connected_flag = False
        print("Bad connection Returned code=",rc)

def testlogic():
    try:
        mqtt.Client.connected_flag = False
        seed(1)
        print("Process Started....")
        client = mqtt.Client(instance_name)
        client.on_connect = on_connect
        client.loop_start()
        print("Connecting to broker ",mqtturl)  
        client.connect(mqtturl,mqttport,300)
        while not client.connected_flag:
            print("In wait loop")
            time.sleep(4)
        while True:
            try:
                for v in arrd:
                    for _ in range(1):
                        value = randint(0,10)
                        client.publish("sensor", json.dumps({"sensor": v+"Box", "value":float(value)}))
            except:
                print("Exception in publish")
    except:
        print("Exception in connection")


testlogic()