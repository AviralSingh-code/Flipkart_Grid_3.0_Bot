import pyfirmata
import time
pin = 13
port = "COM3"
board = pyfirmata.Arduino(port)
while True:
    board.digital[pin].write(1)
    print("ON")
    time.sleep(5)
    board.digital[pin].write(0)
    print("OFF")
    time.sleep(5)