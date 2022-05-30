import requests, subprocess, time


def index(request):
    result = 'none'

    if (request.method == 'POST'):
        url = 'https://ifconfig.io/ip'
        r = requests.get(url)
        path = '/home/___/monitor.ovpn'
        # your path to server cfg file
        process = subprocess.Popen(f"sudo openvpn --auth-nocache --config {path}", shell=True)
        time.sleep(5)
        r2 = requests.get(url)
        process.kill()
        if r.text != r2.text:
            subprocess.run("sudo killall openvpn", shell=True)
#надо килять коннект при успехе, иначе  докер контейнер падаетfrom django.shortcuts import render
            result = 'NICE ONE!'

        else:
            result = 'man, cringe...'
        subprocess.run("sudo killall openvpn", shell=True)

        context = {'info': result}

    context = {'info': result}
    return render(request, 'vpn/index.html', context)
