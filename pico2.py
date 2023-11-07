import machine
import utime

uart = machine.UART(1, baudrate=9600)

# Function to read PWM data from UART
def read_pwm_data():
    data = uart.read()
    if data:
        start_index = data.find(b'START') # Find the start of the data packet.
        end_index = data.find(b'END') # Find the end of the data packet.
        if start_index != -1 and end_index != -1:
            pwm_data = data[start_index+5:end_index].decode() # Decode the data between START and END.
            duty_cycle, frequency = pwm_data.split(":") # Split the data to get duty cycle and frequency.
            return int(duty_cycle), int(frequency)
    return None, None

# Function to send feedback through UART
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
