from flask import Flask, request, jsonify, redirect, send_from_directory
from flask_cors import CORS
import sqlite3
import string
import random
import qrcode
import io
import base64
from datetime import datetime
import os

app = Flask(__name__, static_folder='static')
CORS(app)

# Database initialization
def init_db():
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS urls
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  original_url TEXT NOT NULL,
                  short_code TEXT UNIQUE NOT NULL,
                  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                  clicks INTEGER DEFAULT 0)''')
    conn.commit()
    conn.close()

init_db()

def generate_short_code(length=6):
    """Generate a random short code"""
    characters = string.ascii_letters + string.digits
    while True:
        short_code = ''.join(random.choice(characters) for _ in range(length))
        # Check if code already exists
        conn = sqlite3.connect('urls.db')
        c = conn.cursor()
        c.execute('SELECT short_code FROM urls WHERE short_code = ?', (short_code,))
        if not c.fetchone():
            conn.close()
            return short_code
        conn.close()

def generate_qr_code(url):
    """Generate QR code for URL"""
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Convert to base64
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return f"data:image/png;base64,{img_str}"

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/manifest.json')
def manifest():
    return send_from_directory('static', 'manifest.json')

@app.route('/sw.js')
def service_worker():
    return send_from_directory('static', 'sw.js')

@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    """Create a shortened URL"""
    data = request.json
    original_url = data.get('url')
    
    if not original_url:
        return jsonify({'error': 'URL is required'}), 400
    
    # Add http:// if not present
    if not original_url.startswith(('http://', 'https://')):
        original_url = 'https://' + original_url
    
    # Generate short code
    short_code = generate_short_code()
    
    # Store in database
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute('INSERT INTO urls (original_url, short_code) VALUES (?, ?)',
              (original_url, short_code))
    conn.commit()
    conn.close()
    
    # Generate short URL
    short_url = f"{request.host_url}{short_code}"
    qr_code = generate_qr_code(short_url)
    
    return jsonify({
        'original_url': original_url,
        'short_url': short_url,
        'short_code': short_code,
        'qr_code': qr_code
    })

@app.route('/api/stats/<short_code>')
def get_stats(short_code):
    """Get statistics for a shortened URL"""
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute('SELECT original_url, clicks, created_at FROM urls WHERE short_code = ?', 
              (short_code,))
    result = c.fetchone()
    conn.close()
    
    if not result:
        return jsonify({'error': 'URL not found'}), 404
    
    return jsonify({
        'original_url': result[0],
        'clicks': result[1],
        'created_at': result[2]
    })

@app.route('/api/recent')
def get_recent():
    """Get recently created URLs"""
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute('SELECT short_code, original_url, clicks, created_at FROM urls ORDER BY created_at DESC LIMIT 10')
    results = c.fetchall()
    conn.close()
    
    urls = []
    for row in results:
        urls.append({
            'short_code': row[0],
            'original_url': row[1],
            'clicks': row[2],
            'created_at': row[3],
            'short_url': f"{request.host_url}{row[0]}"
        })
    
    return jsonify(urls)

@app.route('/<short_code>')
def redirect_url(short_code):
    """Redirect to original URL and increment click counter"""
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute('SELECT original_url FROM urls WHERE short_code = ?', (short_code,))
    result = c.fetchone()
    
    if result:
        # Increment click counter
        c.execute('UPDATE urls SET clicks = clicks + 1 WHERE short_code = ?', (short_code,))
        conn.commit()
        conn.close()
        return redirect(result[0])
    
    conn.close()
    return "URL not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
