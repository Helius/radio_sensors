Metarepository for radio sensors project based on nrf24l01.

Main goal is to build network of nodes with sensors, which work on battery or other power source and send data to main node.

Now i have one DHT22 based temperature-humidity sensor which works on battery and sends data each minutes to main node. Main node has USB interface and looks like virtual COM-port (ttyUSB, ttyACM on Linux), it receives data from sensor-node and print it to virtual COM-port in JSON data. 

For example this is DHT22 JSON

{"type":1,"uid":2,"data":[1,152,1,9,0,0]}

type 1 is DHT22
uid - unique id
data is array of temperature and humidity data
[0] = 0x01;         // kind: DHT22 = 1
[1] = 0x02;         // UID
[2] = dht._bits[0]; // humidity_0
[3] = dht._bits[1]; // humidiry_1
[4] = dht._bits[2]; // tempr_0
[5] = dht._bits[3]; // tempr_1
[6] = Vbat;
[7] = temp;

Update submodules:
``` bash
git submodule init && git submodule sync && git submodule update
```
