import sys
import os
import termios
import tty

# ogs the file in the home directory of the user
log_path = os.path.expanduser("~/terminal_input.log")

logfile = open(log_path, "a", buffering=1)
logfile.write("\n\n=== Logging session started ===\n")
logfile.flush()

print("Start typing (Ctrl+C to stop). Keystrokes will be saved to the file:")

# Save the terminal settings
fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)

# Define custom mapping for keys
key_map = {
    'a': '1-',
    'b': '2-',
    'c': '3-',
    'd': '4-',
    'e': '5-',
    'f': '6-',
    'g': '7-',
    'h': '8-',
    'i': '9-',
    'j': '10-',
    'k': '11-',
    'l': '12-',
    'm': '13-',
    'n': '14-',
    'o': '15-',
    'p': '16-',
    'q': '17-',
    'r': '18-',
    's': '19-',
    't': '20-',
    'u': '21-',
    'v': '22-',
    'w': '23-',
    'x': '24-',
    'y': '25-',
    'z': '26-',
    '\r': '[ENTER]',
    '\n': '[ENTER]',
    '\x7f': '[BS]',
    ' ': '[SPACE]',
}

try:
    tty.setraw(fd)  # set terminal to raw mode
    while True:
        ch = sys.stdin.read(1)  # read 1 keypress immediately

        # Exit on Ctrl+C
        if ch == '\x03':
            print("\nStopped logging.")
            break

        # Determine what to log
        if ch in key_map:
            output = key_map[ch]
        else:
            output = ch  # default: log the raw character

        # Echo to terminal
        if ch == '\x7f':  # backspace visual handling
            sys.stdout.write('\b \b')
        elif ch == '\r' or ch == '\n':
            sys.stdout.write('\n')
        else:
            sys.stdout.write(ch)
        sys.stdout.flush()

        # Write mapped value to logfile
        logfile.write(output)
        logfile.flush()

finally:
    # Restore terminal settings and close the file
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    logfile.close()