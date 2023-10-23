import machine
import utime
import uos

pwm_pin = machine.Pin(15)
pwm = machine.PWM(pwm_pin)
pwm.freq(50)

uart = machine.UART(1, baudrate=9600)

def set_pwm(duty_cycle, frequency=50):
    pwm.freq(frequency)
    pwm.duty_u16(duty_cycle)
    send_pwm_data(duty_cycle, frequency)

def send_pwm_data(value, frequency):
    message = 'START:{}:{}END'.format(value, frequency)
    uart.write(message)

def receive_feedback():
    data = uart.read()
    if data:
        start_index = data.find(b'START')
        end_index = data.find(b'END')
        if start_index != -1 and end_index != -1:
            feedback = data[start_index+5:end_index].decode()
            print("Feedback Received:", feedback)

# Example usage
set_pwm(32768, 60)  # 50% duty cycle at 60Hz

while True:
    receive_feedback()
    utime.sleep(1)
