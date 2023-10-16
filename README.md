# SED1115 Pair-Based project: Pico PWM Communication 

This project establishes communication between two Pico devices using the UART protocol. One Pico device generates a PWM signal and sends its value to the second Pico device over the UART serial link.

## Features

1. Uses the built-in PWM functions of the Pico for a stable PWM signal.
2. Implements UART communication with data packaging for clear data transmission.
3. Modular design for easy modifications and updates.

## Prerequisites

- Two Raspberry Pi Pico microcontrollers.
- MicroPython firmware installed on the Pico devices.
- Necessary hardware setup to establish UART communication between the two devices.

## Installation & Setup

1. Connect the two Pico devices using UART pins (TX to RX and RX to TX).
2. Load the `pico_1.py` script onto the first Pico device.
3. Load the `pico_2.py` script onto the second Pico device.
4. Power up both devices.

## Usage

1. The first Pico device will generate a PWM signal and send its value over UART.
2. The second Pico device will continuously listen for incoming UART data. Once received, it will print the received PWM value.


## Future Work

- Implement error-checking mechanisms for UART data transmission.
- Enhance the resolution and accuracy of the PWM signal.
- Introduce wireless communication methods.

## License

This project is open source and available under the MIT License.


