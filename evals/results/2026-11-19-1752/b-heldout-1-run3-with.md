**12 November**

**Goal:** Stop the DHT22 returning NaN on the ESP32.

**Tried:** ESP32 DevKit, DHT22 temperature sensor on GPIO 4, Arduino IDE 2.3.2. Readings came back NaN every few tries. [ask: ESP32 board package version, DHT library and version, DHT22 VCC and GND pins]

| Signal | From | To |
|---|---|---|
| DHT22 data | GPIO 4 | DHT22 data pin |
| Pull-up | DHT22 data line | 3.3 V, 10 kΩ resistor |

**Result (before):** NaN every few tries. [measure: NaN count per 100 readings]

**Changed:** Added a 10 kΩ pull-up resistor between the data line and 3.3 V.

**Result (after):** 100 readings, 0 NaN.

**Next:** [ask: next test, such as a longer run or different conditions]
