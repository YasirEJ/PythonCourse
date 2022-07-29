from requests import get
from datetime import datetime


def measure(func):
    def wrapper(*args):
        start = datetime.now()
        func(*args)
        end = datetime.now() - start
        return end
    return wrapper 

@measure
def get_url(url):
    result = get(url)
    return result

print(get_url('https://google.com'))
print(get_url('https://youtube.com'))