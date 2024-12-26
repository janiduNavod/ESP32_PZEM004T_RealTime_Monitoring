# ESP32 and PZEM-004T Energy Monitoring

This repository provides a Python-based implementation for monitoring electrical parameters such as **Voltage (V)**, **Current (A)**, **Power (W)**, and **Energy (Wh)** using an **ESP32 microcontroller** and a **PZEM-004T energy meter**.

## Features
- Real-time monitoring of electrical parameters.
- User-friendly Python script for reading and visualizing data.
- Designed for home energy monitoring projects.

## Components
1. **ESP32 Development Board**
2. **PZEM-004T Energy Meter**
3. Electrical Load (e.g., a light bulb or electronic device)
4. Jumper Wires

## Circuit Diagram
Connect the ESP32 and PZEM-004T as follows:
- PZEM-004T TX -> ESP32 RX2 
- PZEM-004T RX -> ESP32 TX2 
- PZEM-004T GND -> ESP32 GND
- Power up the PZEM-004T using an external power source.

## Applications
- Home energy consumption analysis
- Device energy efficiency comparison
- Energy logging for smart home systems

## CSV Data Logging
The script writes the following parameters to a CSV file:

- Voltage (V)
- Current (A)
- Power (W)
- Energy (Wh)


