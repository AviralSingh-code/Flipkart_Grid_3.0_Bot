import pyfirmata
import time
port = "COM3"
board = pyfirmata.Arduino(port)
sensor = board.get_pin('d:7:i')
buzzer = 12

it = pyfirmata.util.Iterator(board)
it.start()

while True:
    a = sensor.read()
    print(a)
    if a is True:
        board.digital[buzzer].write(1)
    elif a is False:
        board.digital[buzzer].write(0)
