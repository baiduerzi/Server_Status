import requests

timeout = 10

key = 'SCU20211T5a48f0049a7d4bff618c5b4c0eba8a515a5d822ca1dfe'

title = "wt vps 6"
content = "The VPS is running 6"

payload = {
    'text': title,
    'desp': content
}

url = 'https://sc.ftqq.com/{}.send'.format(key)
requests.post(url, params=payload, timeout=timeout)