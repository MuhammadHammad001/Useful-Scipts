# Useful-Scipts
This repository includes the scripts for important day-day tasks in Ubuntu
## How to clone and use this
  Simply, press `ctrl+shift+N` and the terminal will be opened. Then, simple run the following command to clone this repository:
  ```bash
    git clone https://github.com/MuhammadHammad001/Useful-Scipts
  ```
  Then, change the directory to the working directory using the following command:
  ```bash
    cd Useful-Scripts
  ```
  Now, simply use the following scripts depending upon your need. :)
## 1. DDIP(Divide the Documents into Parts)
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
