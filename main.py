# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import requests, subprocess, time

def connection_checker():
    url = 'https://ifconfig.io/ip'
    r = requests.get(url)

    print(r.text)
    result = ''
    path = '/home/petusharix/monitor.ovpn'
    process = subprocess.Popen(f"sudo openvpn --auth-nocache --config {path}", shell=True)
    time.sleep(5)
    r2 = requests.get(url)
    print(r2.text)
    process.kill()
    if r.text != r2.text:
        result = 'NICE ONE!'
    else:
        result = 'man, cringe...'



connection_checker()
subprocess.run("sudo killall openvpn", shell=True)