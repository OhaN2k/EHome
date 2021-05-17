import sys
from sql import *
from Adafruit_IO import *

conn = ConnectDB("ehome.db")
conn.create_table()
conn.log_light()

ADAFRUIT_IO_USERNAME = "Ohan"
ADAFRUIT_IO_KEY = "aio_YUUj11sBFfZNygLRWvLygfR0SbJG"
topics = ["sound", "light"]

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
    if feed_id == "sound":
        sound_mes(payload)
        conn.sound_entry(payload)
    elif feed_id == "light":
        light_mes(payload)
        conn.light_entry(payload)
    else:
        print("Undefined feed")

def sound_mes(payload):
    data = aio.receive('sound')
    print("Received message on topic sound {} at {}.".format(payload, data.created_at))
    if int(payload) > 80:
        print("Warning! Loud volume")
    

def light_mes(payload):
    data = aio.receive('light')
    print("Received message on topic light {} at {}.".format(payload, data.created_at))
    if int(payload) < 20:
        print("Warning! Inefficient light")
    elif int(payload) > 80:
        print("Warning! Ambient too bright")



# data['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '_asdict', '_field_defaults', '_fields', '_fields_defaults', '_make', '_replace', 
# 'completed_at', 'count', 'created_at', 'created_epoch', 'ele', 'expiration', 'feed_id', 'from_dict', 'id', 'index', 'lat', 'lon', 'position', 'updated_at', 'value']
    


# Create an MQTT client instance.
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

 

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