"""
Youtube Downloader App
Copyright (c) 2024 Muhammad Hammad Bashir

This application allows users to download YouTube videos.

Created by Muhammad Hammad Bashir
"""

import sys
from pytube import YouTube
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMessageBox
import time

class YoutubeDownloaderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.title_for_video = ""
        self.path_for_the_video = ""
        self.views_count_video = ""
        self.url_for_the_video = ""
        self.setWindowTitle("Youtube Downloader")
        self.setGeometry(100, 100, 400, 200)  # Adjust the window size as needed
        self.layout = QVBoxLayout()
        self.init_ui(self.layout)

    def init_ui(self,layout):

        self.label = QLabel("Welcome to the Youtube Videos and Playlist Downloader")
        self.label.setFont(QFont('Arial', 14, QFont.Bold))
        layout.addWidget(self.label)

        self.title_label = QLabel("Video Title")
        self.title_label.setFont(QFont('Arial', 14, QFont.Bold))
        layout.addWidget(self.title_label)

        self.views_label = QLabel("Views: ")
        self.views_label.setFont(QFont('Arial', 12))
        layout.addWidget(self.views_label)

        self.url_field = QLineEdit()
        self.url_field.setObjectName("url_field")
        self.url_field.setPlaceholderText("Enter the URL")
        layout.addWidget(self.url_field)

        self.path = QLineEdit()
        self.path.setObjectName("path")
        self.path.setPlaceholderText("Enter the Path where you want to save the video/playlist")
        layout.addWidget(self.path)

        self.resolution_combo = QComboBox()
        layout.addWidget(self.resolution_combo)        

        self.fetch_details_button = QPushButton("Fetch the details!", clicked=lambda: self.fetch())
        layout.addWidget(self.fetch_details_button)

        self.download_button = QPushButton("Start Downloading!", clicked=lambda: self.start_download())
        layout.addWidget(self.download_button)

        self.restart_button = QPushButton("Download More Videos!", clicked=lambda: self.reset_ui())
        layout.addWidget(self.restart_button)

        # Copyright and Acknowledgment
        self.copyright_label = QLabel("Copyright (c) 2024 Muhammad Hammad Bashir.\n Github: MuhammadHammad001")
        # Styling the copyright and acknowledgment labels
        self.copyright_label.setFont(QFont('Arial', 8))
        layout.addWidget(self.copyright_label)

        # Initially, hide the resolution dropdown and download,restart button and path field
        self.resolution_combo.hide()
        self.download_button.hide()
        self.restart_button.hide()
        self.path.hide()

        #Also hide the video title and views label
        self.title_label.hide()
        self.views_label.hide()

        self.setLayout(layout)

        self.show()

    def fetch(self):
        self.url_for_the_video = self.url_field.text()
        url = self.url_field.text()
        # Validate the URL
        if url:
            try:
                # Hide the fetch button
                self.fetch_details_button.hide()
                self.url_field.hide()
                title, views = self.populate_resolution_dropdown(url)
                self.title_for_video = title
                self.views_count_video = views
                # Show the resolution dropdown and the download button
                self.resolution_combo.show()
                self.label.setText(f'Select resolution for \n{title}:')
                self.download_button.show()
                self.path.show()
            except Exception as e:
                error_message = f"Error fetching details: {str(e)}"
                QMessageBox.critical(self, "INVALID URL", error_message)
                self.reset_ui()
        else:
            self.label.setText('Please enter a valid URL!')

        self.url_field.setText("")

    def start_download(self):
        selected_details=self.resolution_combo.currentText()
        self.path_for_the_video = self.path.text()
        #Hide all the un necessary details
        self.resolution_combo.hide()
        self.download_button.hide()
        self.path.hide()
        #Show the details of video/playlist
        self.title_label.show()
        self.views_label.show()
        self.title_label.setText(f'Video Title:\n {self.title_for_video}')
        self.views_label.setText(f'Views count:\n {self.views_count_video}')
        self.label.setText(f'Downloading has started!!')
        # Force the GUI to update
        QApplication.processEvents()
        self.download_video(self.url_for_the_video, selected_details)

    def reset_ui(self):
        self.title_for_video = ""
        self.path_for_the_video = ""
        self.views_count_video = ""
        self.url_for_the_video = ""

        self.restart_button.hide()
        self.label.hide()
        self.copyright_label.hide()

        self.init_ui(self.layout)
    # Helper functions
    def download_video(self, url, selected_details):
        resolution = selected_details.split(" -- ")[0]
        video_type = selected_details.split(" -- ")[1]
        try:
            yt = YouTube(url)
            selected_stream = yt.streams.filter(res=resolution, file_extension='mp4').first()
            if selected_stream:
                    selected_stream.download(self.path_for_the_video)
                    self.title_label.hide()
                    self.views_label.hide()
                    self.label.setText(f'Video has been Downloaded!!')
                    self.restart_button.show()
            else:
                self.label.setText(f"No suitable stream found for {video_type} with resolution {resolution}")
                QApplication.processEvents()
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            QMessageBox.critical(self, "Error", error_message)
            self.label.setText(error_message)
            QApplication.processEvents()
    def populate_resolution_dropdown(self, url):
        self.label.setText(f'Fetching available resolutions...\n Please wait\n Note: If you face Force Quit Problem, Just wait for few seconds!!!')

        # Force the GUI to update
        QApplication.processEvents()
        self.resolution_combo.clear()
        yt = YouTube(url)
        title = yt.title
        views = yt.views
        resolution_list = []
        for stream in yt.streams:
            if stream.type == "video":
                resolution_list.append(f"{stream.resolution} -- {stream.type}")
        self.resolution_combo.addItems(resolution_list)
        return title, views
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = YoutubeDownloaderApp()
    window.show()
    sys.exit(app.exec_())
