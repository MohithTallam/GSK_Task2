from sys import stdin
from machine import Pin, I2C, ADC, RTC, UART
uart = machine.UART(1, tx=Pin(4), rx=Pin(5), baudrate=9600)
print(uart)

def UART_Receiver():
    
    # if any chars are available in receive buffer
    if uart.any() != 0:
        buff = uart.readline()
        print(buff)
    
#         if len(str(buff))>4:
#             print("here")
#             buffline = print(buff)
#             print(hex(buffline))         # Print recieved command for Debugging
while True:
    
    UART_Receiver()
