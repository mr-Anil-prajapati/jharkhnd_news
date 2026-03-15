#!/usr/bin/env python3
"""
News Publisher Script
Generates HTML pages from news JSON
"""

import json
import os
from datetime import datetime

# Read news data
with open('news/news.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

news_items = data['news']

# Category names
categories = {
    'jharkhand': 'झारखंड न्यूज़',
    'jobs': 'नौकरी',
    'sports': 'खेल',
    'entertainment': 'मनोरंजन',
    'education': 'शिक्षा',
    'national': 'राष्ट्रीय',
    'international': 'अंतरराष्ट्रीय'
}

# Generate main index.html
index_html = '''<!DOCTYPE html>
<html lang="hi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>झारखंड न्यूज़ - Jharkhand News</title>
  <meta name="description" content="झारखंड की सबसे तेज़ न्यूज़ वेबसाइट">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: 'Segoe UI', Tahoma, sans-serif; background: #f5f5f5; }
    .header { background: linear-gradient(135deg, #e11d48, #be123c); color: white; padding: 20px; text-align: center; }
    .header h1 { font-size: 2.5rem; }
    .nav { background: #1a1a1a; padding: 15px; text-align: center; }
    .nav a { color: white; text-decoration: none; margin: 0 15px; }
    .nav a:hover { color: #fbbf24; }
    .hero { background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('https://images.unsplash.com/photo-1504711434969-e33886168f5c?w=1200'); background-size: cover; color: white; padding: 80px 20px; text-align: center; }
    .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
    .news-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }
    .news-card { background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
    .news-card img { width: 100%; height: 200px; object-fit: cover; }
    .news-card-content { padding: 20px; }
    .news-card h3 { color: #e11d48; margin-bottom: 10px; }
    .news-card .category { background: #e11d48; color: white; padding: 5px 10px; border-radius: 5px; font-size: 0.8rem; }
    .news-card .date { color: #666; font-size: 0.9rem; margin-top: 10px; }
    .footer { background: #1a1a1a; color: white; padding: 30px; text-align: center; margin-top: 50px; }
    .section-title { color: #e11d48; font-size: 1.8rem; margin: 30px 0 20px; border-left: 4px solid #e11d48; padding-left: 15px; }
  </style>
</head>
<body>
  <header class="header">
    <h1>📰 झारखंड न्यूज़</h1>
    <p>Jharkhand's Fastest News Website</p>
  </header>
  <nav class="nav">
    <a href="/">Home</a>
    <a href="/category/jharkhand">झारखंड</a>
    <a href="/category/jobs">नौकरी</a>
    <a href="/category/sports">खेल</a>
    <a href="/category/education">शिक्षा</a>
  </nav>
  
  <div class="container">
    <h2 class="section-title">ताज़ा खबर</h2>
    <div class="news-grid">
'''

# Add news cards
for news in news_items:
    cat_name = categories.get(news['category'], news['category'])
    index_html += f'''
      <div class="news-card">
        <img src="{news['image']}" alt="{news['title']}">
        <div class="news-card-content">
          <span class="category">{cat_name}</span>
          <h3>{news['title']}</h3>
          <p>{news['summary']}</p>
          <p class="date">📅 {news['date']}</p>
        </div>
      </div>
'''

index_html += '''
    </div>
  </div>
  
  <footer class="footer">
    <p>&copy; 2026 झारखंड न्यूज़ | All Rights Reserved</p>
  </footer>
</body>
</html>
'''

# Write index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print(f"✅ Generated index.html with {len(news_items)} news articles")
print("Ready to push to GitHub!")
