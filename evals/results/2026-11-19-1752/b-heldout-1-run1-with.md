**12 November**

- **Goal:** Stop the DHT22 on the ESP32 returning NaN.
- **Tried:** ESP32 DevKit, Arduino IDE 2.3.2, DHT22 data on GPIO 4. Readings returned NaN every few tries. Board package version: [ask]

| Signal | From | To | Notes |
|---|---|---|---|
| DATA | DHT22 data pin | GPIO 4 | [ask: DHT22 pin number] |
| Pull-up | DATA line | 3.3 V | 10 kΩ resistor |

- **Changed:** Added a 10 kΩ pull-up resistor between the data line and 3.3 V.
- **Result:** 100 readings after the change, 0 NaN. Conditions: [ask: sampling interval, room temperature, cable length]
- **Next:** [ask: next step]
