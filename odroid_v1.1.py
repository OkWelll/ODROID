import serial

file = open("/home/qst1798/PycharmProjects/odroid_prototype_v1.1/text.txt", "w")
file.write('Beginning of file')
file.close()
ser = serial.Serial('/dev/ttyUSB0', 9600)
t = 0
while True:
    if t < 10:
        file = open("/home/qst1798/PycharmProjects/odroid_prototype_v1.1/text.txt", "a")
        print(str(ser.readline()) + '\n')
        file.write('str № ' + str(t))
        file.write(str(ser.readline()) + '\n')
        t += 1
        file.close()
    else:
        break
