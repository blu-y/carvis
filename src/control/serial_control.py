import serial
import time
import numpy
bytesize = serial.EIGHTBITS
parity = serial.PARITY_NONE
stopbits = serial.STOPBITS_ONE
xonxoff = False
ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM11'
ser.open()

if ser.isOpen():
    print(ser.name + ' is connected...')
    print("Serial details parameters:", ser)
class Car:
    def __init__(self, speed=0, steer1=0, steer0=0):
        self.speed = speed
        self.steer1 = steer1
        self.steer0 = steer0
    def say_state(self):
        print("Speed : {} kph".format(self.speed))
        print("Running")
    def accelerate(self):
        vel = int(input('Speed value 0~20: '))
        y = vel * 10
        if 200 < y:
            self.speed = 0
            print("Speed value error!")
        else:
            sp = (int(y))
            self.speed = sp
    def direction(self):
        dir = int(input('Steer value -2000~2000: '))

        bits = 16
        if dir == 0:
            self.steer1 = 0
            self.steer0 = 0
            degree = dir / 71
            print("Direction :{}", degree, "deg ^")
        elif 0 < dir <= 255:
            st0 = 0
            a = hex((0 << bits) + dir)
            a = a[2:]
            a = a.zfill(len(a) + len(a) % 2)
            b = ''.join(a[i:i + 1] for i in range(0, len(a), 1))
            st1 = (int(b, 16))
            degree = (st0 * 256 + st1)/71
            self.steer1 = st1
            self.steer0 = st0
            print("Steering : {} Right", degree, "deg ")
        elif 256 <= dir <= 2000:
            a = hex((0 << bits) + dir)
            nn = hex((0 << bits) + dir)
            a = a[3:]
            nn = nn[1:3]
            a = a.zfill(len(a) + len(a) % 2)
            b = ''.join(a[i:i + 3] for i in range(0, len(a), 3))
            st00 = ''.join(nn[i:i + 1] for i in range(1, len(a), 3))
            st1 = (int(b, 16))
            st0 = (int(st00))
            degree = (st0*256 + st1)/71
            self.steer1 = st1
            self.steer0 = st0
            print("Steering : {} Right", degree, "deg ")
        elif 2000 < dir or dir < -2000:
            self.steer1 = 0
            self.steer0 = 0
            print("Steer value error!")
        elif -2000 <= dir < 0:
            def tohex(val, nbits):
                return hex((val + (1 << nbits)) % (1 << nbits))
            minus = (tohex(dir, 16))
            # st1
            minus1 = minus[4:]
            st1 = (int(minus1, 16))
            ## st0
            minus0 = minus[2:4]
            st0 = (int(minus0, 16))
            self.steer1 = st1
            self.steer0 = st0
            degree = dir/71
            print("Steering :{} Left", degree, "deg ")
my_car = Car()
print("Start . . . ")
while 1:
    byte = ([0x53, 0x54, 0x58, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x0D, 0x0A])
    number = byte[0:14]
    data = number
    action = input("Ready to start? Key [S]").upper()
    if action not in "S" or len(action) != 1:
        print("Error")
        continue
    if action == 'S':
        my_car.accelerate()
    my_car.direction()
    my_car.say_state()
    for data in range(255):
        time.sleep(0.01)
        number[11] = data #Alive
        number[8] = my_car.steer0
        number[9] = my_car.steer1
        number[6] = 0
        number[7] = my_car.speed
        send = ser.write(serial.to_bytes(number))
        read = ser.readline()
        print("Send =", number)
        print("read = ", read)
ser.close()

























            
