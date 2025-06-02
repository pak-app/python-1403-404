# Greenhouse IoT Data Protocol

## 1. Overview

This document describes the binary data protocol used for transmitting sensor readings from IoT devices to the Greenhouse monitoring system. The data is contained within a `.txt` file.

The payload is dynamic, meaning a single transmission can contain any combination of the possible data fields. The presence of each data field is indicated by a 1-byte header at the beginning of the payload.

## 2. Header Byte (Presence Flags)

The first byte of every payload is a header used as a bitmask. Each bit corresponds to a specific data field. If a bit is set to `1`, its corresponding data field is present in the payload, immediately following the header byte. The data fields appear in the same order as the bits.

The bits are read from least significant bit (LSB) to most significant bit (MSB).

| Bit | Data Field | Status      |
|:----|:-----------|:------------|
| 0   | Temperature| Defined     |
| 1   | Humidity   | Defined     |
| 2   | Sunlight   | Defined     |

**Example:** A header byte of `0x03` (binary `00000011`) indicates that **Temperature** (bit 0) and **Humidity** (bit 1) data follows. The payload would be `[Header Byte][Temperature Data][Humidity Data]`.

## 3. Payload Data Structure

This table describes the format for each individual data field. The byte order for multi-byte fields is Big-Endian (Most Significant Byte first).

| Data Field  | Size (Bytes) | Description & Processing                                                                         |
|:------------|:-------------|:-------------------------------------------------------------------------------------------------|
| Temperature | 1            | An integer. Multiply the raw value by `2` to get the final temperature.                            |
| Humidity    | 2            | A 16-bit unsigned integer.                                                                       |
| Sunlight    | 3            | A 24-bit unsigned integer. Divide the raw value by `100.0` to get the actual value.                |
| Date        | 3            | **Byte 1:** Year (e.g., 24 for 2024), **Byte 2:** Month (1-12), **Byte 3:** Day (1-31)               |
| Time        | 3            | **Byte 1:** Hour (0-23), **Byte 2:** Minute (0-59), **Byte 3:** Second (0-59)                      |