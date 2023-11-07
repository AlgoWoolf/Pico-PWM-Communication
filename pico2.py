from machine import Pin, UART, PWM
import utime

uart = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9))
uart.init(bits=8, parity=None, stop=1)


# Function to read PWM data from UART
def read_pwm_data():
    data = uart.read()
    if data:
        start_index = data.find(b'START') # Find the start of the data packet.
        end_index = data.find(b'END') # Find the end of the data packet.
        if start_index != -1 and end_index != -1:
            pwm_data = data[start_index+6:end_index].decode() # Decode the data between START and END.
            
            data = pwm_data.split(":")
            print(data)
            duty_cycle, frequency = data[0], data[1]
            # Split the data to get duty cycle and frequency.
            return int(duty_cycle), int(frequency)
    return None, None

# Function to send feedback through UART
def send_feedback(duty_cycle, frequency):
    feedback = "Received PWM with duty cycle {} at {}Hz".format(duty_cycle, frequency)
    message = 'START{}END'.format(feedback)
    uart.write(message)

while True:
    duty_cycle, frequency = read_pwm_data()
    print("it's running")
    print(duty_cycle, frequency)
    if duty_cycle and frequency:
        print("Received PWM Value:", duty_cycle, "Frequency:", frequency)
        send_feedback(duty_cycle, frequency)
    utime.sleep(1)
