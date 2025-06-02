# Protocol Description

This protocol is for getting some data from IoT devices into Greenhouse. These data is located on .bin file and the Prorocol information is available at the rest of this file.

## What is its data

This file contains data of tempreture, humidity, amount of sunlight and data and time.

## Size of data

The size of data is measured and available in bytes. For example if tempreture is 2 it mean 2 bytes. and when reading a file each unit is byte.

* Tempreture → 1 byte
    * product by 2
* Humidity → 2 byte
    * Order of bytes: MSB → LSB
* Sunlight → 3
    * Order of bytes: MSB → LSB
    * Divide on 100 two get acual number
* Date → 3
    * Byte 1 → Year
    * Byte 2 → Month
    * Byte 3 → Day
* Time → 3
    * Byte 1 → Hour
    * Byte 2 → Minutes
    * Byte 3 → Seconds

* **Note:** Some times the payload can contain all data or multiple of them and or signle one. This seperation can be done with one byte at the first of payload. each bits of this byte is one it mean that data is available in that payload.

* Order of bits
    - 0 → Tempreture
    - 1 → Humidity
    - 2 → Sunlight
