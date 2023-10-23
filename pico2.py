import machine
import utime

uart = machine.UART(1, baudrate=9600)

def read_pwm_data():
    data = uart.read()
    if data:
        start_index = data.find(b'START')
        end_index = data.find(b'END')
        if start_index != -1 and end_index != -1:
            pwm_data = data[start_index+5:end_index].decode()
            duty_cycle, frequency = pwm_data.split(":")
            return int(duty_cycle), int(frequency)
    return None, None

def send_feedback(duty_cycle, frequency):
    feedback = "Received PWM with duty cycle {} at {}Hz".format(duty_cycle, frequency)
    message = 'START{}END'.format(feedback)
    uart.write(message)

while True:
    duty_cycle, frequency = read_pwm_data()
    if duty_cycle and frequency:
        print("Received PWM Value:", duty_cycle, "Frequency:", frequency)
        send_feedback(duty_cycle, frequency)
    utime.sleep(1)
