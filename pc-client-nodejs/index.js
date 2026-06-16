const { SerialPort } = require('serialport');
const { ReadlineParser } = require('@serialport/parser-readline');
const mqtt = require('mqtt');

const SERIAL_PORT = 'COM10';
const BAUD_RATE = 9600;
const MQTT_BROKER = 'mqtt://broker.benax.rw:1883';
const MQTT_TOPIC = 'temperature/sensor_data_prince';

const serialPort = new SerialPort({ path: SERIAL_PORT, baudRate: BAUD_RATE });
const parser = serialPort.pipe(new ReadlineParser({ delimiter: '\n' }));
const mqttClient = mqtt.connect(MQTT_BROKER);

mqttClient.on('connect', () => {
  console.log('Connected to MQTT broker');
});

parser.on('data', (data) => {
  const temperature = parseFloat(data.trim());
  if (!isNaN(temperature)) {
    console.log(`Received temperature: ${temperature} °C`);
    mqttClient.publish(MQTT_TOPIC, JSON.stringify({ temperature, timestamp: new Date().toISOString() }));
  }
});

serialPort.on('error', (err) => {
  console.error('Serial port error:', err.message);
});
