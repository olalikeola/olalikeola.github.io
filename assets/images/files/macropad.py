import time

import adafruit_ssd1306
import board
import busio
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Initialize the keyboard HID interface
keyboard = Keyboard(usb_hid.devices)

# Initialize I2C on GP20 (SDA) and GP21 (SCL)
i2c = busio.I2C(scl=board.GP21, sda=board.GP20)

# Initialize the 128x32 OLED display
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Clear the display
oled.fill(0)
oled.show()

# Define pins for keypress detection (GPIO 0-7)
pins = [board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7]

# Initialize GPIO pins as inputs with pull-up resistors
keys = []
for pin in pins:
    key = digitalio.DigitalInOut(pin)
    key.direction = digitalio.Direction.INPUT
    key.pull = digitalio.Pull.UP  # Enable pull-up resistor
    keys.append(key)

# Define a mapping of pins to keycodes based on your updated requirements
key_mapping = {
    0: [Keycode.COMMAND, Keycode.C],  # Pin 0 -> Command + C (Copy)
    1: [Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB],  # Pin 1 -> Control + Shift + Tab
    2: [Keycode.CONTROL, Keycode.TAB],  # Pin 2 -> Control + Tab
    3: [Keycode.COMMAND, Keycode.V],  # Pin 3 -> Command + V (Paste)
    4: Keycode.THREE,  # Pin 4 -> '3'
    5: Keycode.ONE,  # Pin 5 -> '1'
    6: Keycode.FOUR,  # Pin 6 -> '4'
    7: Keycode.TWO,  # Pin 7 -> '2'
}

# Keycode to name mapping for display purposes
keycode_names = {
    Keycode.COMMAND: "Command",
    Keycode.C: "C",
    Keycode.V: "V",
    Keycode.SPACE: "Space",
    Keycode.CONTROL: "Control",
    Keycode.SHIFT: "Shift",
    Keycode.TAB: "Tab",
    Keycode.ONE: "1",
    Keycode.TWO: "2",
    Keycode.THREE: "3",
    Keycode.FOUR: "4",
}

# Main loop to check keypresses
while True:
    for i, key in enumerate(keys):
        if not key.value:  # Key is pressed (active-low)
            keycode = key_mapping.get(i)
            if keycode:
                print(f"Key {i} pressed, sending {keycode} to the computer...")
                
                # Send the key press to the computer
                if isinstance(keycode, list):  # If it's a list (multiple keys, like Command + key combo)
                    for kc in keycode:
                        keyboard.press(kc)  # Press each key in the combination
                    time.sleep(0.1)  # Hold for a short time
                    keyboard.release_all()  # Release all keys
                else:
                    keyboard.press(keycode)  # Single key press
                    time.sleep(0.1)  # Hold the key down for a short time
                    keyboard.release(keycode)  # Release the key
                
                # Display the key(s) on the OLED screen
                oled.fill(0)  # Clear the screen
                if isinstance(keycode, list):  # For key combinations
                    display_text = " + ".join([keycode_names.get(kc, str(kc)) for kc in keycode])
                else:  # Single key
                    display_text = keycode_names.get(keycode, str(keycode))
                oled.text(display_text, 0, 0, 1)
                oled.show()  # Update the display
                
            time.sleep(0.3)  # Debounce delay
    time.sleep(0.1)  # Slight delay before checking the keys again
