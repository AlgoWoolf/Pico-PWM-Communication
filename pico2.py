import machine
import utime

uart = machine.UART(1, baudrate=9600)

def read_pwm_value():
    # Functionality Change 3: Data Packaging
    while True:
        data = uart.read()
        if data:
            start_index = data.find('START')
            end_index = data.find('END')
            if start_index != -1 and end_index != -1:
                return int(data[start_index+5:end_index])

while True:
    pwm_value = read_pwm_value()
    print("Received PWM Value:", pwm_value)
    utime.sleep(1)
