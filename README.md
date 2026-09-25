# Telegram Face Anonymizer Bot

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8%2B-green.svg)](https://opencv.org/)
[![pyTelegramBotAPI](https://img.shields.io/badge/TelegramBotAPI-4.12%2B-blue.svg)](https://github.com/eternnoir/pyTelegramBotAPI)

A privacy-focused Telegram Bot that automatically detects human faces in uploaded images and applies Gaussian Blur filters using **OpenCV Computer Vision**.

---

## 🚀 Key Features

* **Computer Vision Processing**: Automated human face detection using OpenCV Haar Cascade Classifiers.
* **Privacy Protection**: Applies dynamic Gaussian Blur to detected facial bounding boxes.
* **Automated Cleanup**: Secure resource management ensuring temporary files are immediately deleted post-processing using `try-finally` blocks.
* **Asynchronous File Handling**: Streamlined photo download and delivery pipeline.

---

## 🛠️ Tech Stack

* **Language**: Python 3.10+
* **Computer Vision**: OpenCV (`opencv-python`)
* **Bot Framework**: pyTelegramBotAPI

---

## ⚙️ Configuration & Setup

### 1. Clone the repository
git clone https://github.com/DrRafael/telegram-face-blur-bot.git
cd telegram-face-blur-bot

### 2. Install dependencies
pip install -r requirements.txt

### 3. Configure API Credentials
Copy `config.py.example` to `config.py` and insert your Bot Token:
```python
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
