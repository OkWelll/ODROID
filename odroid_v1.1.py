import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)
t = 0
while True:
    if t < 10:
        file = open("text.txt", "a")
        file.write(str(ser.readline()) + '\n')
        t += 1
        file.close()
    else:
        break
