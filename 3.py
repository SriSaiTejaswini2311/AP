import threading
import requests
import time

def download_file(url):
    file_name = url.split('/')[-1]
    response = requests.get(url)
    with open(file_name, 'wb') as file:
        file.write(response.content)

def sequential_download(url_list):
    for url in url_list:
        download_file(url)

def concurrent_download(url_list):
    threads = []
    for url in url_list:
        thread = threading.Thread(target=download_file, args=(url,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

def read_urls_from_file(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines() if line.strip()]

if __name__ == "__main__":
    urls = read_urls_from_file("urls.txt")

    start = time.perf_counter()
    sequential_download(urls)
    print("Time taken for sequential download:", time.perf_counter() - start)

    start = time.perf_counter()
    concurrent_download(urls)
    print("Time taken for concurrent download:", time.perf_counter() - start)
