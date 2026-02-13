import requests
import threading
import time

urls = [
    "https://example.com/data1",
    "https://example.com/data2",
    "https://example.com/data3",
    "https://example.com/data4"
]

def downloadfiles(url):
    try:
        response=requests.get(url)
        filename=url.split("/")[-1]+".txt"
        with open(filename, "w", encoding="utf-8") as f:
           f.write(response.text)
        print(f"Downloaded:{filename}")
    except Exception as e:
        print(f"Error downloading{url}:{e}")
starttime=time.time()
for url in urls:
    downloadfiles(url)
sequentialtime=time.time()-starttime
print(f"\nsequential download time:{sequentialtime}")


threads=[]
starttime1=time.time()
for url in urls:
    thread=threading.Thread(target=downloadfiles,args=(url,))
    threads.append(thread)
    thread.start()
thredingtime=time.time()-starttime1
print(f"\nThreading download time:{thredingtime}")

