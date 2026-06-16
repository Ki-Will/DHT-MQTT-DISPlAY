# Temperature Display and MQTT Monitoring

A complete embedded system for temperature monitoring using Arduino, LCD, PC Client, and MQTT Broker.

## Live Dashboard
The dashboard is deployed on a VPS and available at:
[http://157.173.101.159:8228/](http://157.173.101.159:8228/)

## System Architecture
<<<<<<< HEAD

[SYSTEM_ARCHITECTURE.png]/(SYSTEM_ARCHITECTURE.png)
=======
```mermaid 
flowchart TD
    A[DHT11 Temperature Sensor] --> B[Arduino Uno]
    B --> C[16x2 LCD Display]
    B --> D[USB Serial 9600bps]
    D --> E[Python PC Client]
    E --> F[MQTT Broker broker.hivemq.com]
    F --> G[Dashboard on VPS \n http://157.173.101.159:8228]
>>>>>>> f2c655bb7fd99e32ab53c9b848212547dd2467a3

    style A fill:#1E3A8A,color:#FFFFFF,stroke:#60A5FA,stroke-width:2px
    style B fill:#065F46,color:#FFFFFF,stroke:#34D399,stroke-width:2px
    style C fill:#5B21B6,color:#FFFFFF,stroke:#A78BFA,stroke-width:2px
    style D fill:#9D174D,color:#FFFFFF,stroke:#F472B6,stroke-width:2px
    style E fill:#92400E,color:#FFFFFF,stroke:#FBBF24,stroke-width:2px
    style F fill:#0F766E,color:#FFFFFF,stroke:#5EEAD4,stroke-width:2px
    style G fill:#991B1B,color:#FFFFFF,stroke:#F87171,stroke-width:2px
```
## Project Structure
```
DHT-MQTT-DISPlAY/
├── arduino/
│   └── DHT_Temperature_LCD/
│       └── DHT_Temperature_LCD.ino
├── pc-client-python/
│   ├── index.py
│   └── requirements.txt
├── pc-client-nodejs/
│   ├── index.js
│   ├── package.json
│   └── package-lock.json
├── ui/
│   └── index.html
├── PROCESS.md
└── README.md

```

## Part 1: Arduino Setup

### Components Required
- Arduino Uno
- DHT11 Temperature Sensor (3-pin)
- 16x2 I2C LCD Display
- Breadboard and Jumper Wires

### Wiring

#### 1. DHT11 Sensor (3-pin)
| DHT11 Pin | Arduino Uno Pin |
|-----------|-----------------|
| VCC       | 5V              |
| GND       | GND             |
| DATA      | Digital Pin 2   |

#### 2. I2C LCD Display
| LCD Pin | Arduino Uno Pin |
|---------|-----------------|
| VCC     | 5V              |
| GND     | GND             |
| SDA     | A4 (SDA)        |
| SCL     | A5 (SCL)        |

### Required Arduino Libraries
Install these via Arduino Library Manager:
- `DHT sensor library` by Adafruit
- `Adafruit Unified Sensor`
- `LiquidCrystal I2C` by Frank de Brabander

### Code
The Arduino sketch is in `arduino/DHT_Temperature_LCD/DHT_Temperature_LCD.ino`. Don't forget to:
1. Set your candidate name in the code
2. Verify your LCD I2C address (common addresses: 0x27 or 0x3F)

## Part 2: PC Client Setup (Python)

### Installation
```bash
cd pc-client-python
pip install -r requirements.txt
```

### Configuration
Update the following in `pc-client-python/index.py`:
- `SERIAL_PORT`: Your Arduino's COM port (e.g., COM10 on Windows)
- `MQTT_BROKER`: broker.benax.rw (already set)
- `MQTT_PORT`: 1883 (already set)
- `MQTT_TOPIC`: prince_bonheur/sensor_data (already set)

### Running the Client
```bash
py index.py
```

**Note**: Make sure no other program (like Arduino IDE Serial Monitor) is using the same COM port!

## Part 3: Dashboard Setup

The dashboard is a simple HTML page located in `ui/index.html`.
To use it:
1. Open `ui/index.html` in your browser
2. The dashboard will connect to broker.hivemq.com automatically
3. It shows real-time temperature data and recent history!

## Communication Details

- **Serial Communication**: Between Arduino and PC at 9600 baud
- **MQTT Broker**: broker.hivemq.com
- **MQTT Port**: 1883
- **MQTT Topic**: prince_bonheur/sensor_data
- **MQTT Websocket Port (for dashboard): 8884

**Visit [PROCESS.md]/(./PROCESS.md) to see how everyting ws made togehter with screenshots**
