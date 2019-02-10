import paho.mqtt.client as mqtt


# The callback for when the client receives a CONNACK response from the server.
import requests


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    service = "github"

    xml = """<play_info>
        <app_key>BjK81vKPdmpxHAsoWcCwMtRJQ4GajczZ</app_key>
        <url>https://NikithaPreetham.github.io/Married%20Life.mp3</url>
        <service>service</service>
        <volume>50</volume>
        </play_info>"""

    print(requests.post('http://192.168.1.26:8090/speaker', data=xml))

    response = requests.get('http://192.168.1.26:8090/now_playing').text

    print response

    return response


def mqtt_listen():
    host = "hackher413.danrowe.com"
    port = 1883

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host, port, 60)

    print('Connecting to %s:%s' % (host, port))


        # Subscribing outside of on_connect() means that if we lose the
        # connection and reconnect then subscriptions won't be renewed.
    client.subscribe("safespace/number")
        # Blocking call that processes network traffic, dispatches
        # callbacks and handles reconnecting.
    client.loop_forever()


if __name__ == '__main__':
    mqtt_listen()