import requests

proxy_pool_flash = 'http://127.0.0.1:5555/random'
ip = requests.get(proxy_pool_flash).text
print('http://' + ip)