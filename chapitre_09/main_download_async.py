import requests
import httpx
from bs4 import BeautifulSoup
import time
import asyncio

def requests_download_and_save(url,log_file):
    url_log = url+log_file
    response = requests.get(url_log)
    with open(log_file,"w") as f:
        f.write(response.text)

async def requests_download_and_save_async(url,log_file):
    url_log = url+log_file

    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, requests.get, url_log)

    with open(log_file,'w') as f:
        f.write(response.text)


async def httpx_download_and_save(url,log_file):
    url_log = url+log_file
    async with httpx.AsyncClient() as client:
        response = await client.get(url_log)
        with open(log_file,"w") as f:
            f.write(response.text)


async def main():
    start = time.perf_counter()
    url = "https://logs.eolem.com/"
    all_threads = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_a = [a['href'] for a in soup.find_all('a') if a['href'].endswith('.log')]
    
    download_coroutines = []
    for a in all_a:
        download_coroutines.append(httpx_download_and_save(url,a))

    await asyncio.gather(*download_coroutines)



    end = time.perf_counter()

    print(f"{end-start:.3}s")

if __name__ == '__main__':
    asyncio.run(main())