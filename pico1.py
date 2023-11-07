import machine
import utime
import uos

# Configure the PWM pin and set its frequency
pwm_pin = machine.Pin(15) # Define pin 15 as the PWM output pin.
pwm = machine.PWM(pwm_pin) # Create a PWM object on pin 15.
pwm.freq(50) # Set the PWM frequency to 50Hz.

# Configure UART
uart = machine.UART(1, baudrate=9600) # Initialize UART 1 with a baud rate of 9600.

# Function to set the PWM duty cycle and send the data via UART
def set_pwm(duty_cycle, frequency=50):
    pwm.freq(frequency)
    pwm.duty_u16(duty_cycle)
    send_pwm_data(duty_cycle, frequency) # Send the PWM data through UART.

# Function to send PWM data through UART
def send_pwm_data(value, frequency):
    message = 'START:{}:{}END'.format(value, frequency)
    uart.write(message)

# Function to receive feedback from UART
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
