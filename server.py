import requests

timeout = 10

key = ''

title = "wt vps 6"
content = "The VPS is running 6"

payload = {
    'text': title,
    'desp': content
}

url = 'https://sc.ftqq.com/{}.send'.format(key)
requests.post(url, params=payload, timeout=timeout)
