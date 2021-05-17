import sys
from sql import *
from Adafruit_IO import *

conn = ConnectDB("ehome.db")
conn.create_table()

ADAFRUIT_IO_USERNAME = "Ohan"
ADAFRUIT_IO_KEY = "aio_Xdzo29tz5l6N5SFckUXaquhaAdGA"
topics = ["led", "temperature", "sound", "light", "infrared", "time"]

def connected(client):
    for feed in topics:
        client.subscribe(feed)
        print('Connected to Adafruit IO!  Listening for {0} changes...'.format(feed))

def subscribe(client, userdata, mid, granted_qos):
    print('Subscribed to {0} with QoS {1}'.format(topics[mid-1], granted_qos[0]))

def disconnected(client):
    print('Disconnected from Adafruit IO!')
    sys.exit(1)

def message(client, feed_id, payload):
    if feed_id in topics:
        date = str(datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S"))
        print("Received message on topic {} with value {} at {}.".format(feed_id, payload, date))
        conn.data_entry(feed_id, date, payload)
    else:
        print("Undefined feed")
        return

# Create an MQTT client instance.
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
# aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Setup the callback functions defined above.
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message
client.on_subscribe  = subscribe

# Connect to the Adafruit IO server.

try:
    client.connect()
except:
    print("Can't connect")
    sys.exit(1)

client.loop_blocking()