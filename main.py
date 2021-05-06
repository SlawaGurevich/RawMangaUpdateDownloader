from PyQt5.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow )

from Browser import Browser
from ConfigHandler import ConfigHandler

from MainWindow import Ui_MainWindow

import sys
import os


class App():
    main_window = None

    def __init__(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.main_window.setWindowTitle("Raw Manga Update Downloader")


class MainWindow(QMainWindow, Ui_MainWindow):
    browser = None
    meta = {}
    config = ConfigHandler()

    def __init__(self, *args, obj=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.browser = Browser()
        self.setupUi(self)

        self.load_config()
        self.set_ui()
        self.set_signals()


    def load_config(self):
        if not self.config.has_section("main"):
            self.config.add_section("main")

        self.i_link.setText(self.config.get("main", "link", fallback=""))
        self.i_destination.setText(self.config.get("main", "destination", fallback=""))

        if not self.i_link.text() is "" and not self.i_destination.text() is "":
            self.update_info()


    def set_ui(self):
        self.pb_download.setValue(0)

    def set_signals(self):
        self.i_link.textChanged.connect(self.update_info)
        self.b_destination.clicked.connect(self.set_dest)
        self.b_download.clicked.connect(self.start_download)

    def set_dest(self):
        dialog = QFileDialog()
        dialog.setDirectory(self.i_destination.text() or "/")
        destination = str(QFileDialog.getExistingDirectory(self, "Select Target Directory"))
        if destination:
            self.i_destination.setText(destination)
            self.config.set("main", "destination", destination)
            self.check_if_download_possible()

    def check_if_download_possible(self):
        if "http://rawmangaupdate.com" in self.i_link.text() and os.path.exists(self.i_destination.text()):
            self.b_download.setEnabled(True)


    def update_info(self):
        print("Info Updated")
        if "http://rawmangaupdate.com" in self.i_link.text():
            self.meta = self.browser.get_info(self.i_link.text())
            manga_chapter_names = self.meta["manga_chapter_names"]
            manga_chapter_links = self.meta["manga_chapter_links"]

            self.i_name.setText(self.meta["manga_title"])
            self.i_chapters.setText(f'{len(manga_chapter_links)}')

            self.cb_start.clear()
            self.cb_start.addItems(manga_chapter_names)
            self.cb_start.setCurrentIndex(0)

            self.cb_end.clear()
            self.cb_end.addItems(manga_chapter_names)
            self.cb_end.setCurrentIndex(len(manga_chapter_names) - 1)

            self.check_if_download_possible()

            self.config.set("main", "link", self.i_link.text())

    def start_download(self):
        self.browser.download_chapters(self.i_destination.text(),
                                       self.meta,
                                       self.cb_start.currentIndex(),
                                       self.cb_end.currentIndex())



if __name__ == "__main__":
    scraper = Browser()

    # scraper.getChapterList('http://rawmangaupdate.com/manga/kimetsu-no-yaiba')

    application = QApplication(sys.argv)
    application.setStyle('Fusion')

    main = App()

    application.exec_()
