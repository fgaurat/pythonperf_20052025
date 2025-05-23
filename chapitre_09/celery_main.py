from celery import Celery,signature,group,chain
import requests
from bs4 import BeautifulSoup
import time


# https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html#first-steps-with-celery

# docker pull rabbitmq
# docker run -d -p 5672:5672 rabbitmq

# pour Windows : 
# celery -A celery_tasks worker --loglevel=INFO -P solo 

# pour les autres 
# celery -A celery_tasks worker --loglevel=INFO



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