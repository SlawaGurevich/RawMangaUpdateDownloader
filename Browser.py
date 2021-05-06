from selenium.webdriver import (Chrome, ChromeOptions)
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

import urllib.request
import cgi

import os
import requests
import re

class Browser():
    chrome_options = ChromeOptions()

    def __init_(self):
        pass

        # self.chrome_options.add_argument("window-size=1920,1080")
        # self.chrome_options.add_argument("--headless")

    def get_info(self, link):
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")

        chrome = Chrome(chrome_options=chrome_options)
        chrome.get(link)

        # get the links to the chapters
        links = chrome.find_elements_by_css_selector("[class^=chapter-title] a")
        links.reverse()
        chapter_urls = list(map(lambda a: a.get_attribute("href"), links))

        # get the chapter numbers
        chapter_numbers = chrome.find_elements_by_css_selector("[class^=chapter-title] em")
        chapter_numbers.reverse()
        sanitized_numbers = list(map(lambda nr: ''.join(c for c in nr.text if c.isdigit() or c == "."), chapter_numbers))

        title = chrome.find_element_by_css_selector(".widget-title")

        print(chapter_numbers[0].text)

        return {
            "manga_title": title.text,
            "manga_chapter_names": sanitized_numbers,
            "manga_chapter_links": chapter_urls
        }

    def download_chapters(self, destination, meta, start, end):
        print("downloading chapters")
        print(destination, meta, start, end)
        manga_title = meta["manga_title"]
        manga_chapter_names = meta["manga_chapter_names"];

        if os.path.exists(destination):
            manga_dir = os.path.join(destination, manga_title)

            if not os.path.isfile(destination):
                if not os.path.exists(manga_dir):
                    os.mkdir(os.path.join(destination, manga_dir))

                chrome_options = ChromeOptions()
                chrome_options.add_argument("--headless")

                chrome = Chrome(chrome_options=chrome_options)

                for index, chapter_link in enumerate(meta["manga_chapter_links"]):
                    print(chapter_link)
                    chapter_dir = os.path.join(manga_dir, manga_chapter_names[index])

                    if not os.path.exists(chapter_dir):
                        os.mkdir(chapter_dir)

                    chrome.get(chapter_link)
                    page_count = len(chrome.find_elements_by_css_selector("#page-list option"))

                    for ix in range(1, page_count):
                        chrome.get(f'{ chapter_link }/{ manga_chapter_names[ix] }')

                        download_link = chrome.find_element_by_css_selector('.scan-page').get_attribute("src")

                        # remote_file = urllib.request.urlopen(download_link)
                        # info = remote_file.info()['Content-Disposition']
                        # value, params = cgi.parse_header(info)
                        # filename = params["filename"]

                        urllib.request.urlretrieve(download_link,
                                                   os.path.join(chapter_dir, f'{ix}.jpg'))

                    break # remove after testing

            else:
                print("Path is a file!")
        else:
            print("Path already exists")
