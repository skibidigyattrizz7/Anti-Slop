**12 November**

Worked on the temperature sensor setup for an ESP32 DevKit. The DHT22 data pin is connected to GPIO 4, and the sketch is written and uploaded with Arduino IDE 2.3.2.

Problem: the sensor readings were returning NaN every few tries. Those failed reads produced no valid temperature or humidity values, so the output could not be trusted as it stood. Floating data lines are a common cause of this kind of intermittent failure, and the DHT22 needs a pull-up on its data line to hold the signal reliably high between reads.

Change: I added a 10 kΩ pull-up resistor between the data line and 3.3 V.

Result: after adding the resistor, I ran the sketch for 100 readings and got 0 NaN values.

No other measurements were taken, so this result covers only that 100-reading run.
