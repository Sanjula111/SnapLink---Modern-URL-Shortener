# ⚡ SnapLink - Modern URL Shortener

A beautiful, fast, and mobile-responsive URL shortener with PWA support. Install on any mobile device and use it like a native app!

## ✨ Features

- 🎨 **Modern UI** - Beautiful gradient design with smooth animations
- 📱 **Mobile First** - Fully responsive, works perfectly on all devices
- 💾 **PWA Support** - Install as a native app on iOS/Android
- 🔗 **QR Code Generation** - Automatic QR codes for every shortened URL
- 📊 **Analytics** - Track clicks and view statistics
- ⚡ **Lightning Fast** - Instant URL shortening
- 🌙 **Dark Theme** - Easy on the eyes

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or download the files**

2. **Install Python dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python app.py
```

4. **Open in browser**
```
http://localhost:5000
```

## 📱 Install on Mobile

### Android

1. Open the app in Chrome
2. Tap the menu (⋮) and select "Add to Home screen"
3. Or look for the install prompt at the top of the page
4. Tap "Install" and you're done!

### iOS (iPhone/iPad)

1. Open the app in Safari
2. Tap the Share button (□↑)
3. Scroll down and tap "Add to Home Screen"
4. Tap "Add" in the top right
5. The app icon will appear on your home screen!

## 🎯 How to Use

1. **Shorten a URL**
   - Paste your long URL into the input field
   - Click "Shorten URL"
   - Get your shortened link instantly!

2. **Share**
   - Copy the shortened URL
   - Download the QR code
   - Share on social media

3. **Track**
   - View click statistics
   - See when the link was created
   - Monitor all your recent links

## 🛠️ Configuration

### Change Port

Edit `app.py` and modify the port:
```python
app.run(host='0.0.0.0', port=5000, debug=True)
```

### Database

The app uses SQLite (`urls.db`) which is created automatically. No configuration needed!

## 🌐 Deploy to Production

### Using Gunicorn

1. Install Gunicorn:
```bash
pip install gunicorn
```

2. Run with Gunicorn:
```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

### Using Docker (Optional)

Create a `Dockerfile`:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

Build and run:
```bash
docker build -t snaplink .
docker run -p 5000:5000 snaplink
```

## 📂 Project Structure

```
snaplink/
├── app.py                 # Flask backend
├── requirements.txt       # Python dependencies
├── urls.db               # SQLite database (auto-created)
└── static/
    ├── index.html        # Frontend UI
    ├── manifest.json     # PWA manifest
    └── sw.js            # Service worker
```

## 🎨 Customization

### Change Colors

Edit the CSS variables in `static/index.html`:
```css
:root {
    --accent-primary: #00d9ff;      /* Primary color */
    --accent-secondary: #ff006e;    /* Secondary color */
    --bg-primary: #0a0a0f;         /* Background */
}
```

### Change App Name

Update in these files:
- `static/index.html` - `<title>` and `.logo` text
- `static/manifest.json` - `name` and `short_name`

## 🔒 Security Notes

For production use, consider:
- Adding user authentication
- Rate limiting API endpoints
- HTTPS/SSL certificate
- Input validation and sanitization
- CORS configuration for specific domains

## 📱 Browser Support

- ✅ Chrome/Edge (Desktop & Mobile)
- ✅ Safari (Desktop & Mobile)
- ✅ Firefox (Desktop & Mobile)
- ✅ Samsung Internet
- ✅ Opera

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

MIT License - feel free to use this project for personal or commercial purposes.

## 💡 Tips

- The app works offline after first load (PWA)
- You can use custom short codes by modifying the API
- QR codes can be downloaded by right-clicking
- All data is stored locally in SQLite

## 🐛 Troubleshooting

**App won't start?**
- Make sure Python 3.8+ is installed
- Check if port 5000 is available
- Install all dependencies from requirements.txt

**Can't install on mobile?**
- Make sure you're using HTTPS (required for PWA)
- Try using Chrome on Android or Safari on iOS
- Check if your browser supports PWA

**URLs not shortening?**
- Check your internet connection
- Verify the URL format is correct
- Look at browser console for errors

## 🎉 Enjoy!

Made with ⚡ and lots of ☕

---

For questions or support, create an issue on the repository.
