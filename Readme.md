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

##Code Explanation
Serial Port Configuration
The script connects to the ESP32 over the specified COM port and baud rate:
serial_port = "COM8"  # Update this as per your setup
baud_rate = 115200
CSV Data Logging
The script writes the following parameters to a CSV file:

Voltage (V)
Current (A)
Power (W)
Energy (Wh)
Sample Data Format
The ESP32 should send data in this format:

makefile
Copy code
Voltage: 230.0V
Current: 1.5A
Power: 345.0W
Energy: 12.5Wh
Output File
All received data is saved into sensor_data.csv:

csv
Copy code
Voltage (V),Current (A),Power (W),Energy (Wh)
230.0,1.5,345.0,12.5
Example Output
Upon running the script, you'll see data logged in the terminal:

vbnet
Copy code
Connected to COM8
Received: Voltage: 230.0V
Received: Current: 1.5A
Received: Power: 345.0W
Received: Energy: 12.5Wh
The data will also be saved into sensor_data.csv.

Applications
Home energy consumption analysis.
Device energy efficiency comparison.
Energy logging for smart home systems.

