# Social Media Summarizer

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28-red?style=for-the-badge&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**📱 Summarize social media posts instantly - Text & Images**

> Completely free, runs locally, no API keys needed!

[Features](#features) • [Quick Start](#quick-start) • [Usage](#usage) • [Installation](#installation)

</div>

---

## ✨ Features

- 📝 **Text Summarization** - Summarize Instagram captions, tweets, and social posts
- 🖼️ **Image Summarization** - Extract text from screenshots and summarize them
- 🌐 **Web UI** - Beautiful Streamlit interface
- 💻 **CLI Tool** - Command-line interface for power users
- 🆓 **100% Free** - No API keys, no subscriptions
- 🖥️ **Local Only** - All processing runs on your machine
- ⚡ **Fast** - CPU-based processing

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Tesseract OCR (for image processing)

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/yustianfelix/social-media-summarizer.git
cd social-media-summarizer
```

**2. Install Tesseract OCR**

**macOS:**
```bash
brew install tesseract
```

**Ubuntu/Debian:**
```bash
sudo apt-get install tesseract-ocr
```

**Windows:**
Download from: https://github.com/UB-Mannheim/tesseract/wiki

**3. Install Python dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the app**

**Option A: Web UI (Recommended)**
```bash
streamlit run streamlit_app.py
```
Opens at: `http://localhost:8501`

**Option B: CLI**
```bash
python app.py --mode text --input "Your post text here"
python app.py --mode image --input ./screenshot.jpg
```

---

## 📖 Usage

### Web UI (Streamlit)

Simply launch the app and use the interface:

```bash
streamlit run streamlit_app.py
```

**Features:**
- 📝 **Text Tab** - Paste and summarize social media posts
- 🖼️ **Image Tab** - Upload screenshots for OCR + summarization

### CLI Mode

**Summarize text:**
```bash
python app.py --mode text --input "Just completed a 30-day fitness challenge..."
```

**Summarize image:**
```bash
python app.py --mode image --input ./instagram_screenshot.jpg
```

---

## 📁 Project Structure

```
social-media-summarizer/
├── streamlit_app.py      # 🌐 Web UI
├── app.py                # 💻 CLI tool
├── requirements.txt      # Dependencies
├── .gitignore
└── README.md
```

---

## 🔒 Privacy

✓ All processing runs **locally**  
✓ No data sent to external servers  
✓ No API keys required  
✓ Works completely offline  

---

## 🐛 Troubleshooting

**"Tesseract not found"**
- macOS: `brew install tesseract`
- Ubuntu: `sudo apt-get install tesseract-ocr`
- Windows: Install from https://github.com/UB-Mannheim/tesseract/wiki

**"Model download fails"**
- Check internet connection
- Delete `.cache/huggingface/` folder
- Run again to re-download

**"No text extracted from image"**
- Image must be clear and readable
- Text should be horizontal
- Ensure text has good contrast

---

<div align="center">

</div>
