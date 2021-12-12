import serial
import time

from handler import handle_input


arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)


def read():
    data = arduino.readline()
    data = data.decode("utf-8").rstrip()

    if data:
        return handle_input(data)
    else:
        return None


def run():
    while True:
        value = read()
        if value:
            print(value)
        time.sleep(0.1)


if __name__ == "__main__":
    run()
