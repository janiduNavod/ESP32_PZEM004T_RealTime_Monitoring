import serial
import csv

# Serial Port Configuration
serial_port = "COM8"  # Update this as per your setup
baud_rate = 115200
output_file = "sensor_data.csv"

try:
    # Connect to the serial port
    ser = serial.Serial(serial_port, baud_rate, timeout=1)
    print(f"Connected to {serial_port}")
except serial.SerialException as e:
    print(f"Error: Could not connect to ESP32. Details: {e}")
    exit()

# Open CSV file to save data
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the headers
    writer.writerow(["Voltage (V)", "Current (A)", "Power (W)", "Energy (Wh)"])

    try:
        while True:
            # Read data from Serial
            line = ser.readline().decode('utf-8').strip()
            if line:
                print(f"Received: {line}")  # Debug print
                # Process key:value pairs
                if "Voltage" in line:
                    voltage = line.split("Voltage:")[1].split("V")[0].strip()
                if "Current" in line:
                    current = line.split("Current:")[1].split("A")[0].strip()
                if "Power" in line:
                    power = line.split("Power:")[1].split("W")[0].strip()
                if "Energy" in line:
                    energy = line.split("Energy:")[1].split("Wh")[0].strip()

                    # Write to CSV once all values are available
                    writer.writerow([voltage, current, power, energy])
                    file.flush()  # Ensure data is written immediately
    except KeyboardInterrupt:
        print("\nStopped by User")
    finally:
        ser.close()
        print(f"Data saved to {output_file}")
