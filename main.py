import requests
from bs4 import BeautifulSoup

def fetch_proxies_from_json_urls(urls):
    all_links = []

    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            links = [entry['link'] for entry in data]
            all_links.extend(links)
        else:
            print(f'Failed to fetch data from URL: {url}')

    return all_links

def fetch_proxies_from_telegram_channel(url):
    proxies = []
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        proxy_elements = soup.find_all('a', text='پروکسی')
        proxies = [element.get('href') for element in proxy_elements]
    else:
        print(f"Failed to fetch data from URL: {url}")

    return proxies

def save_proxies_to_file(proxy_list):
    with open('proxy.txt', 'w', encoding='utf-8') as file:
        for proxy in proxy_list:
            file.write(proxy + '\n')

if __name__ == "__main__":
    json_urls = [
        "https://raw.githubusercontent.com/yebekhe/MTProtoCollector/main/proxy/mtproto.json",
        "https://raw.githubusercontent.com/miladesign/MTProtoCollector/main/proxy/mtproto.json"
    ]
    extracted_json_proxies = fetch_proxies_from_json_urls(json_urls)

    telegram_urls = [
        "https://t.me/s/iporoto",
        "https://t.me/s/iproxy",
        "https://t.me/s/iRoProxy",
        "https://t.me/s/proxyforopeta",
        "https://t.me/s/IRN_Proxy",
        "https://t.me/s/MProxy_ir",
        "https://t.me/s/PyroProxy"
    ]

    extracted_telegram_proxies = []
    for url in telegram_urls:
        extracted_telegram_proxies.extend(fetch_proxies_from_telegram_channel(url))

    all_proxies = extracted_json_proxies + extracted_telegram_proxies

    save_proxies_to_file(all_proxies)
