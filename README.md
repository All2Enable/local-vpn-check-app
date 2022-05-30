# local-vpn-check-app
A small app made on django, made for linux servers with OpenVPN
Requirements: unix-system, python ver. > 3.0, OpenVPN server config file
Getting started:
1. open file VPNsite/VPNcheck/views.py" and change "path" variable to your OpenVPN config file
2. open terminal in VPNsite directory and write "python3 manage.py runserver"
3. check if local server is running
4. check if you can get server status
Deploying:
1. go to VPNsite/VPNsite/settings.py
2. look for secret_key and change it to the one you need(it shoud go to enviroment variables)
3. open terminal and write python3 manage.py check --deploy
4. after that change "Debug" to false
5. change "allowed_hosts" variable to your site address


# Run in Docker:
1. Clone repo
`git clone https://github.com/devSLAVUS/local-vpn-check-app.git`
`cd local-vpn-check-app/`
2. Build image
`docker build --tag devmaxfork:latest .`
3. Run image
`docker run --name devmax_site_fork -d -p 8999:8999 --cap-add=NET_ADMIN --device /dev/net/tun devmax:latest`
4. Check
`curl 127.0.0.1:8999`
