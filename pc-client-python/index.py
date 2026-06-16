import serial
import serial.tools.list_ports
import paho.mqtt.client as mqtt
import json
from datetime import datetime

SERIAL_PORT = 'COM10'
BAUD_RATE = 9600
MQTT_BROKER = 'broker.benax.rw'
MQTT_PORT = 1883
MQTT_TOPIC = 'temperature/sensor_data_prince'


def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print('Connected to MQTT broker')
    else:
        print(f'Failed to connect to MQTT broker, return code {rc}')


def main():
    mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    mqtt_client.on_connect = on_connect
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
    mqtt_client.loop_start()

    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        print(f'Connected to serial port {SERIAL_PORT} at {BAUD_RATE} baud')

        while True:
            line = ser.readline().decode('utf-8').strip()
            if line:
                try:
                    temperature = float(line)
                    print(f'Received temperature: {temperature} °C')
                    payload = {
                        'temperature': temperature,
                        'timestamp': datetime.now().isoformat()
                    }
                    mqtt_client.publish(MQTT_TOPIC, json.dumps(payload))
                except ValueError:
                    pass

    except serial.SerialException as e:
        print(f'Serial port error: {e}')
        if 'PermissionError' in str(e):
            print('\n**Hint**: Make sure no other program (like Arduino IDE Serial Monitor) is using COM10!')
        print('\nAvailable ports:')
        for port in serial.tools.list_ports.comports():
            print(f'  {port.device}')
    except KeyboardInterrupt:
        print('\nExiting...')
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
        mqtt_client.loop_stop()
        mqtt_client.disconnect()


if __name__ == '__main__':
    main()
