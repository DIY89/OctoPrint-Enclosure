import sys
import smbus2
import bme280

if len(sys.argv) == 2:
    DEVICE = int(sys.argv[1], 16)
else:
    print('-1 | -1')
    sys.exit(1)

# Rev 2 Pi, Pi 2 & Pi 3 & Pi 4 use bus 1
# Rev 1 Pi uses bus 0
bus = smbus2.SMBus(1)

def read_dht():
  data = bus.read_i2c_block_data(80, 0, 5)
  return data

def main():
  try:
    data = read_dht()

    print('{0:0.1f} | {1:0.1f}'.format(data.temperature, data.humidity))
  except:
     print('-1 | -1')

if __name__== "__main__":
   main()
