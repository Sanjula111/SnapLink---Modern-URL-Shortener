# 📱 Quick Installation Guide

## For Mobile Devices

### 🤖 Android Installation

1. **Open in Chrome Browser**
   - Navigate to `http://your-server-ip:5000`
   - Make sure you're using Chrome (not Firefox or other browsers)

2. **Install the App**
   - Look for the install banner at the top of the page
   - OR tap the three dots menu (⋮) → "Add to Home screen"
   - Tap "Install" or "Add"

3. **Launch the App**
   - Find the SnapLink icon on your home screen
   - Tap to open - it works like a native app!

### 🍎 iOS (iPhone/iPad) Installation

1. **Open in Safari**
   - Navigate to `http://your-server-ip:5000`
   - Must use Safari (Chrome won't work for PWA on iOS)

2. **Add to Home Screen**
   - Tap the Share button (square with arrow pointing up)
   - Scroll down and tap "Add to Home Screen"
   - Edit the name if you want
   - Tap "Add" in the top right

3. **Launch the App**
   - Find the SnapLink icon on your home screen
   - Tap to open - full screen experience!

## 💻 Desktop Installation

### Windows, Mac, Linux

1. **Open in Chrome/Edge**
   - Navigate to `http://localhost:5000`

2. **Install the App**
   - Look for the install icon (⊕) in the address bar
   - Click "Install"
   - The app will open in its own window

## 🌐 Running on Your Network

### To Access from Other Devices

1. **Find Your Computer's IP Address**
   
   **Windows:**
   ```
   ipconfig
   ```
   Look for "IPv4 Address" (e.g., 192.168.1.100)
   
   **Mac/Linux:**
   ```
   ifconfig
   ```
   Look for "inet" (e.g., 192.168.1.100)

2. **Access from Mobile**
   - On your phone, open browser
   - Go to `http://YOUR-IP:5000`
   - Example: `http://192.168.1.100:5000`

3. **Install on Mobile**
   - Follow the installation steps above

## ⚠️ Important Notes

- **Same Network**: All devices must be on the same WiFi network
- **Firewall**: You may need to allow port 5000 in your firewall
- **HTTPS**: For full PWA features on some devices, you'll need HTTPS
- **Keep Running**: Keep the server running on your computer

## 🔧 Troubleshooting

**Can't connect from phone?**
- Check if both devices are on same WiFi
- Try turning off firewall temporarily
- Verify the IP address is correct

**Install button not showing?**
- Make sure you're using Chrome (Android) or Safari (iOS)
- PWA features require HTTPS for production (localhost is okay)
- Clear browser cache and try again

**App not working offline?**
- Open the app at least once while online
- Service worker needs to cache resources first

## 🎉 You're All Set!

Now you can shorten URLs from anywhere on your network!
