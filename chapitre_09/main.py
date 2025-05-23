import requests
from bs4 import BeautifulSoup
import time
def main():
    start = time.perf_counter()
    url = "https://logs.eolem.com/"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_a = [a['href'] for a in soup.find_all('a') if a['href'].endswith('.log')]
    
    for a in all_a:
        url_log = url+a
        response = requests.get(url_log)
        with open(a,"w") as f:
            f.write(response.text)

    end = time.perf_counter()

    print(f"{end-start:.3}s")
if __name__ == '__main__':
    main()