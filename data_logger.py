import csv
import time
import logging
import serial
'''
Serial port is configured at 9600 baud rate and it depends upon the Arduino configurations
'''
ser = serial.Serial(port='/dev/ttyUSB0',
                    baudrate=115200,
                    parity=serial.PARITY_NONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1)
ser.flushInput()
counter = 0
'''
Creating the logging configurations
file mode ='a'--> means continous append
level- just stores the information
'''
logging.basicConfig(filename="logfile.log",
                    filemode='a',
                    level=logging.INFO,
                    datefmt='%H:%M:%S')
while True:
    try:
        timestamp = time.strftime("%j,%H:%M:%S", time.gmtime(time.time()))
        ser_bytes_1 = ser.readline()
        ser_bytes = ser_bytes_1.decode("utf-8")

        decoded_bytes = ser_bytes.split(';')

        logData = timestamp + "  " + ser_bytes
        logging.info(logData)
        if len(decoded_bytes) > 2:
            with open("test_data.csv", "a") as f:
                print("Writing to csv")
                writer = csv.writer(f, delimiter=',')
                print(timestamp)
                print(decoded_bytes)

                writer.writerow([
                    timestamp, decoded_bytes[0], decoded_bytes[1],
                    decoded_bytes[2], decoded_bytes[3], decoded_bytes[4],
                    decoded_bytes[5]
                ])
                #time.sleep(2)
    except:
        # just incase if there is any exceptions during runtime
        logData = timestamp + "   Something went wrong!!"
        logging.info(logData)
