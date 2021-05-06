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

        # get the chapter numbers
        chapterNumbers = chrome.find_elements_by_css_selector("[class^=chapter-title] em")
        chapterNumbers.reverse()
        sanitizedNumbers = list(map(lambda nr: ''.join(c for c in nr.text if c.isdigit() or c == "."), chapterNumbers))

        title = chrome.find_element_by_css_selector(".widget-title")

        print(chapterNumbers[0].text)

        return {
            "title": title.text,
            "chapters": sanitizedNumbers,
            "chapterLinks": links
        }

    def download_chapters(self, destination, chapterLinks, chapterNames, start, end):
        print("downloading chapters")
        print(destination, chapterLinks, chapterNames, start, end)


    def getChapterList(self, link):
        chrome = Chrome(chrome_options=self.chrome_options)

        chrome.get(link)
        links = chrome.find_elements_by_css_selector("[class^=chapter-title] a")
        links.reverse()
        for chapter_index, link in enumerate(links):
            chapter_link = link.get_attribute("href")
            chrome.get(chapter_link)
            page_count = len(chrome.find_elements_by_css_selector("#page-list option"))

            for ix in range(1, page_count):
                chrome.get(f'{chapter_link}/{ix}')
                download_link = chrome.find_element_by_css_selector('.scan-page').get_attribute("src")
                remote_file = urllib.request.urlopen(download_link)
                info = remote_file.info()['Content-Disposition']
                value, params = cgi.parse_header(info)
                filename = params["filename"]

                if not os.path.exists(f'/Users/Midori/Downloads/Manga/{chapter_index + 1}'):
                    os.mkdir(f'/Users/Midori/Downloads/Manga/{chapter_index + 1}')

                urllib.request.urlretrieve(download_link, f'/Users/Midori/Downloads/Manga/{chapter_index + 1}/{filename}')

            break

        print(links)