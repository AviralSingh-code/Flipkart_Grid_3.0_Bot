import pyfirmata
import time
port = "COM3"
board = pyfirmata.Arduino(port)
pin = 7
sensor = board.get_pin('d:7:i')

it = pyfirmata.util.Iterator(board)
it.start()

while True:
    a = sensor.read()
    print(a)
    time.sleep(0.5)