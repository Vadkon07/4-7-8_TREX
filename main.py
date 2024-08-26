import time
import os
from pynput import keyboard
from datetime import datetime

i = 1
count = 0
loop_duration = 19  # Duration of one loop in seconds (4 + 7 + 8)

def clear_screen():
    if os.name == 'nt':
        os.system('cls')  # WINDOWS
    else:
        os.system('clear')  # LINUX

def on_press(key):
    global i
    try:
        if key.char == 'x':
            print("X pressed, your statistics file was saved and soon app will be closed, but before you have to finish to do this loop. Please, wait...")
            total_time = (count * loop_duration) / 60
            finished = datetime.now()
            finished_f = finished.strftime("%d/%m/%Y %H:%M:%S")
            sessions.write(f'{line}. STARTED AT: {started_f}. FINISHED AT: {finished_f} LOOPS: {count}. TIME: {total_time:.2f} MINUTES\n')
            i = 0
            return False  # Stop listener
    except AttributeError:
        pass

clear_screen()
print("*Click 'x' to close app\n\n")
print("Are you ready?")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1!")
time.sleep(1)

started = datetime.now()
started_f = started.strftime("%d/%m/%Y %H:%M:%S")


with open('sessions.txt', 'r') as sessions:
    contents = sessions.read()
    line = contents.count("\n") + 1

    sessions.close()


with open('sessions.txt', 'a') as sessions:
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    while i == 1:
        clear_screen()
        print(f"Loop count: {count}")
        print("Inhale (nose)...")
        for j in range(0, 5):
            print(f"{j}...")
            time.sleep(1)

        clear_screen()
        print(f"Loop count: {count}")
        print("Hold...")
        for j in range(0, 8):
            print(f"{j}...")
            time.sleep(1)

        clear_screen()
        print(f"Loop count: {count}")
        print("Exhale (mouth)...")
        for j in range(0, 9):
            print(f"{j}...")
            time.sleep(1)

        count += 1

    listener.join()

    print(f'Meditation is finished! STARTED AT: {started_f}. FINISHED AT: {finished_f} LOOPS: {count}. TIME: {total_time:.2f} MINUTES\n')
