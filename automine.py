import win32api
import time
import argparse
from subprocess import Popen
import threading


def get_idle_time():
    return (win32api.GetTickCount() - win32api.GetLastInputInfo()) / 1000.0


def run_miner():
    p = Popen("C:\Mining\ethminer-0.9.41-genoil-1.1.7\\start_nano.bat", cwd=r"C:\Mining\ethminer-0.9.41-genoil-1.1.7")
    try:
        p.communicate()
    except KeyboardInterrupt:
        p.terminate()
    return


def instant_start():
    global user_input
    while True:
        user_input = input('')

parser = argparse.ArgumentParser()
parser.add_argument('-t', required=True, help='Period of inactivity in minutes after which to start the miner')

wait_sec = float(parser.parse_args().t) * 60
print("Waiting", wait_sec, "seconds")
print("Use command 'start' to manually launch miner")

user_input = ''

thread = threading.Thread(target=instant_start)
thread.daemon = True
thread.start()

while True:
    if get_idle_time() > wait_sec or user_input == 'start':
        user_input = ''
        run_miner()
    else:
        time.sleep(30)
