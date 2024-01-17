[![Github Badge](http://img.shields.io/badge/-Github-black?style=flat-square&logo=github&link=https://github.com/Ammarkhan561/)](https://github.com/MuhammadHammad001/) 
[![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/hemanthkollipara/)](https://www.linkedin.com/in/muhammad-hammad-bashir/)

# Useful-Scipts
This repository includes the scripts for important day-day tasks in Ubuntu
## How to clone and use this
  Simply, press `ctrl+Alt+T` and the terminal will be opened. Then, simple run the following command to clone this repository:
  ```bash
    git clone https://github.com/MuhammadHammad001/Useful-Scipts
  ```
  Then, change the directory to the working directory using the following command:
  ```bash
    cd Useful-Scripts
  ```
  Now, simply use the following scripts depending upon your need. :)
## 1. Youtube Videos Downloader
  This is a python based interactive application used to download youtube videos without any ads :) localy in your computer.
  ### How to run this locally?
  After cloning the repository, you may simply run the following command to start the application
  ```bash
    ./youtube_downloader.sh
  ```
  The remaining process for downloading the videos is self explanatory. Feel free to suggest me any improvements in the app by creating a issue or
  a PR yourself by contributing to this project.
  
## 2. DDIP(Divide the Documents into Parts)
  The purpose of this script is to divide the document(docx) into multiple parts and the output will be in the .txt format.
  ### How to use this?
  Please use the following flag `-n` with the number of parts you want the document to be divided in.
  To understand how this works, run the following command in the main directory:
  ```bash
  ./ddip.sh -n 4 examples/test_document.docx
  ```
  As you can see that this will create the output directory in the folder in which the input document is.
  If you skip the flag, then it will automatically assign the number of division to be 2.
  ```bash
  ./ddip.sh examples/test_document.docx
  ```
