Nov 12

**Goal:** Stop NaN readings from the DHT22 temperature sensor.

**Tried:** DHT22 data pin on GPIO 4 of an ESP32 DevKit, running from Arduino IDE 2.3.2. Readings returned NaN every few tries.

| Signal | From | To | Pin | Wire colour |
|---|---|---|---|---|
| DHT22 data | DHT22 | ESP32 DevKit | GPIO 4 | [ask] |
| Pull-up | 10 kΩ resistor, data line to 3.3 V | | | [ask] |

**Changed:** Added a 10 kΩ pull-up resistor between the data line and 3.3 V.

**Result:** 0 NaN in 100 readings after the change. No other measurements taken.

**Next:** [ask: next step]
