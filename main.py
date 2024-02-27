import json
import os
import time

import requests
from bs4 import BeautifulSoup
url = "https://www.luxvisage.by/"


# def get_products():
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    # }
    #
    # r = requests.post(url=url, headers=headers)
    #
    # if not os.path.exists("data"):
    #     os.mkdir("data")
    #
    # with open("data/page_main.lxml", "w") as file:
    #     file.write(r.text)
    #
    # with open("data/page_main.lxml") as file:
    #     src = file.read()
    #
    # soap = BeautifulSoup(src, "lxml")
    # all_chapter = soap.find_all("div", class_ ="dropdown-menu")
    # all_chapter_href = []
    # pages_count = 0
    # for chapter in all_chapter:
    #     links = [url + link['href'] for link in chapter.find_all('a')]
    #     all_chapter_href.extend(links)
    #
    # for i in range(len(all_chapter_href)):
    #     r = requests.get(all_chapter_href[i], headers)
    #
    #     with open(f"data/page_{i}.lxml", "w") as file:
    #         file.write(r.text)
    #
    #     #time.sleep(3)
    #
    # for i in range(len(all_chapter_href)):
    #     with open(f"data/page_{i}.lxml") as file:
    #         src = file.read()
    #
    #     soap = BeautifulSoup(src, "lxml")
    #     all_detail_chapter = soap.find_all("a", class_="goods-item__header text-center")
    #     all_detail_chapter_href = []
    #     for chapter in all_detail_chapter:
    #         links = [url + chapter['href'] for chapter in all_detail_chapter]
    #         all_detail_chapter_href.extend(links)
    #         #time.sleep(3)
    #
    #     for i in range(len(all_detail_chapter_href)):
    #         r = requests.get(all_detail_chapter_href[i], "lxml")
    #
    #         with open(f'data/page_{i}_{i}', 'w') as file:
    #             file.write(r.text)
    #
    #         #time.sleep(3)
    #
    #         pages_count += 1
    #
    # return pages_count + 1


def collect_data(pages_count):
    result_list = []
    for page in range(0, 784):
        with open(f"data/page_{page}_{page}") as file:
            src = file.read()

        result_item = {}

        soap = BeautifulSoup(src, "lxml")
        result_item['title'] = soap.find("title").text
        result_item["description"] = soap.find("div", class_="panel-body").text.strip("\n")
        result_item['url'] = soap.find("link", rel="canonical").get("href").strip("https://")

        result_list.append(result_item)

    with open('result.json', 'w', encoding='utf-8') as json_file:
        json.dump(result_list, json_file, ensure_ascii=False, indent=2)


def main():
    # pages_count = get_products()
    collect_data(pages_count=784)


if __name__ == '__main__':
    main()
