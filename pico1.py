import machine
import utime
import uos

# Functionality Change 1: Using built-in PWM
pwm_pin = machine.Pin(15) # Using pin 15 for PWM output
pwm = machine.PWM(pwm_pin)
pwm.freq(50) # Setting frequency to 50Hz

# Functionality Change 2: Initialize UART only once
uart = machine.UART(1, baudrate=9600)

def set_pwm_duty_cycle(duty_cycle):
    pwm.duty_u16(duty_cycle)
    send_pwm_value(duty_cycle)

def send_pwm_value(value):
    # Functionality Change 3: Data Packaging
    message = 'START' + str(value) + 'END'
    uart.write(message)

# Example usage
set_pwm_duty_cycle(32768) # 50% duty cycle for 16-bit resolution

while True:
    # This loop can be used for other tasks or to change PWM values over time
    utime.sleep(1)
