import serial
import sys


try:
    printer_serial = serial.Serial('COM3', 115200, timeout=5)
    print("Connected to printer.")
except serial.SerialException as e:
    print(f"Failed to connect: {e}")
    sys.exit(1)


while True: 
    input_user = input("Enter G-code command (or exit): ")
    if input_user.lower() == 'exit':
        print("Exiting")
        break

    command = input_user + "\n"
    printer_serial.write(command.encode())

    while True:
        response = printer_serial.readline().decode().strip()
        if response:
            print(response)
        if response.lower() == "ok":
            break

printer_serial.close()
