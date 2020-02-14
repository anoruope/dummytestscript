import paho.mqtt.client as mqtt
from dotenv import load_dotenv
from random import seed
from random import randint
import json
import os
from os import path

val1 = "Harz"
val2 = "Haerter"
val3 = "fuellstoff1"
val4 = "fuellstoff2"
val5 = "fuellstoff3"
arrd = [val1,val2,val3,val4,val5]
mqtturl = os.getenv("MQTT_URL")
mqttport = int(os.getenv("MQTT_PORT"))
def testlogic():
    seed(1)
    print("Process Started....")
    while True:
        try:
            for v in arrd:
                for _ in range(1):
                    value = randint(0,10)
                    client = mqtt.Client()
                    client.connect(mqtturl,mqttport,60)
                    client.publish("sensor", json.dumps({"sensor": v+"Box", "value":float(value)}))
                    #print( v+"Box" + " " + str(value))
        except:
            print("doings the rounds")


testlogic()