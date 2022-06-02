import requests, subprocess, time
from django.shortcuts import render


def getopenVPNserver(path):
    url = 'https://ifconfig.io/ip'
    r = requests.get(url)
    process = subprocess.Popen(f"sudo openvpn --auth-nocache --config {path}", shell=True)
    time.sleep(5)
    r2 = requests.get(url)
    process.kill()
    if r.text != r2.text:
        subprocess.run("sudo killall openvpn", shell=True)
        result = 'Nice one!'
    else:
        result = 'Man, cringe...'
    subprocess.run("sudo killall openvpn", shell=True)
    return result


def index(request):
    get = 0
    get2 = 0

    if (request.method == 'POST'):
        #path to config files
        path = '/home/___/monitor.ovpn'
        path2 = '/home/___/venom.ovpn'
        get = getopenVPNserver(path)
        get2 = getopenVPNserver(path2)

    context = {'info': get, 'info2': get2}
    return render(request, 'vpn/index.html', context)
