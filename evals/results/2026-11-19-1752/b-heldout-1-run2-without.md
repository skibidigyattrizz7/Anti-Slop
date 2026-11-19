**12 November**

Today I worked on the ESP32 DevKit with a DHT22 temperature sensor wired to GPIO 4. I compiled and uploaded the sketch in Arduino IDE 2.3.2. Readings were intermittent: every few tries, the sensor returned NaN instead of a valid value. To address this, I added a 10 kΩ pull-up resistor between the data line and 3.3 V. After adding the resistor, I ran the sketch for 100 readings and got zero NaN results.
