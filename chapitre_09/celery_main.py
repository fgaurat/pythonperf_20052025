from celery import Celery,signature,group,chain
import requests
from bs4 import BeautifulSoup
import time

def main():
    app = Celery('tasks', broker='pyamqp://guest@localhost//',backend='rpc://')
    result = app.send_task('celery_tasks.add',args=[2,3])
    i = result.get(timeout=1)
    print(i)
    print(50*"-")
    url = "https://logs.eolem.com/"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_a = [url+a['href'] for a in soup.find_all('a') if a['href'].endswith('.log')]
    # # Download
    # download_tasks = [signature("celery_tasks.download",args=[url]) for url in all_a]
    # download_group = group(download_tasks)
    # result_download = download_group()
    
    # # Save
    # save_tasks = [signature("celery_tasks.save",args=[to_save]) for to_save in result_download.get()]
    # save_group = group(save_tasks)
    # result = save_group()

    for url in all_a:
        chain(
            signature("celery_tasks.download",args=[url]),
            signature("celery_tasks.save")       
        )()



if __name__ == '__main__':
    main()