import urllib.request
from datetime import datetime
from time import sleep


while True:
    begin = datetime.now()
    begin_time = begin.strftime("%H:%M:%S")
    page = urllib.request.urlopen(url="http://localhost:8000/test", timeout=1000)
    end = datetime.now()
    end_time = end.strftime("%H:%M:%S")
    print(page.read(), begin_time," - ", end_time)				
    sleep(3)