import requests
from bs4 import BeautifulSoup
import time
import concurrent.futures

def download_and_save(url,log_file):
    url_log = url+log_file
    response = requests.get(url_log)
    with open(log_file,"w") as f:
        f.write(response.text)


def main():
    start = time.perf_counter()
    url = "https://logs.eolem.com/"
    all_threads = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_a = [a['href'] for a in soup.find_all('a') if a['href'].endswith('.log')]

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(download_and_save,[url]*len(all_a),all_a)

    # download_and_save("https://logs.eolem.com/","apache_logs_01.log")
    # download_and_save("https://logs.eolem.com/","apache_logs_02.log")
    # download_and_save("https://logs.eolem.com/","apache_logs_03.log")
    # download_and_save("https://logs.eolem.com/","apache_logs_04.log")
    # download_and_save("https://logs.eolem.com/","apache_logs_05.log")
    # ...

    
    # for a in all_a:
    #     # download_and_save(url,a)
    #     th = threading.Thread(target=download_and_save,args=(url,a))
    #     th.start()
    #     all_threads.append(th)

    
    [t.join() for t in all_threads]


    end = time.perf_counter()

    print(f"{end-start:.3}s")
if __name__ == '__main__':
    main()