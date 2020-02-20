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

def testlogic():
    try:
        seed(1)
        client = mqtt.Client(instance_name)
        client.username_pw_set("swsfile","swsflorian")
        client.connect(mqtturl,mqttport,5)
        client.loop_start()
        
        while True:
            try:
                for v in arrd:
                    value = randint(0,10)
                    client.publish("sensor", json.dumps({"sensor": v+"Box", "value":float(value)}))
            except:
                print("Exception in publish")
    except:
        print("Exception in connection")
        


testlogic()