import paho.mqtt.client as mqtt



client = mqtt.Client()

mqtt_topics = {
    "S0": "SFB/Sensor/S0",
    "S1": "SFB/Sensor/S1",
    "S2": "SFB/Sensor/S2",
    "Q1": "SFB/Aktor/Q1" ,
    # ..............

  }





#Multi_sub







def publish(topic, message):
    client.publish(topic, message)
    print(f"📤 Versendet `{message}` → `{topic}`")

def phase1():

    if S1 == 1 and S0 == 0:
         publish(mqtt_topics["Q1"], "1") 
         publish(mqtt_topics["Y3"], "1") 
         if B2 == 1 :
            publish(mqtt_topics["Y3"], "0") 
            publish(mqtt_topics["Q1"], "0") 


#def phase2():
#    if
phase1()
