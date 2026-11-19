**12 November**

Today I worked on the DHT22 temperature sensor connected to GPIO 4 of my ESP32 DevKit. I wrote and uploaded the code in Arduino IDE 2.3.2. The readings were returning NaN every few tries, so some reads were failing intermittently.

I added a 10 kilohm pull-up resistor between the data line and 3.3 V. A pull-up keeps the data line at a defined high level when the sensor is not driving it, which is a common fix for this symptom. After adding the resistor, I ran the sketch for 100 readings and got 0 NaN values.

No other measurements were taken today.
