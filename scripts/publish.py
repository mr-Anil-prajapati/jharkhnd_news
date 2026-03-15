#!/usr/bin/env python3
"""
News Publisher Script - Generates HTML pages from news JSON
"""

import json
import os

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

def create_page_header(title):
    return f'''<!DOCTYPE html>
<html lang="hi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - झारखंड न्यूज़</title>
  <meta name="description" content="झारखंड की सबसे तेज़ न्यूज़ वेबसाइट">
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{ font-family: 'Segoe UI', Tahoma, sans-serif; background: #f5f5f5; }}
    .header {{ background: linear-gradient(135deg, #e11d48, #be123c); color: white; padding: 20px; text-align: center; }}
    .header h1 {{ font-size: 2.5rem; }}
    .nav {{ background: #1a1a1a; padding: 15px; text-align: center; }}
    .nav a {{ color: white; text-decoration: none; margin: 0 15px; }}
    .nav a:hover {{ color: #fbbf24; }}
    .container {{ max-width: 1200px; margin: 0 auto; padding: 20px; }}
    .news-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }}
    .news-card {{ background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
    .news-card img {{ width: 100%; height: 200px; object-fit: cover; }}
    .news-card-content {{ padding: 20px; }}
    .news-card h3 {{ color: #e11d48; margin-bottom: 10px; }}
    .news-card .category {{ background: #e11d48; color: white; padding: 5px 10px; border-radius: 5px; font-size: 0.8rem; }}
    .news-card .date {{ color: #666; font-size: 0.9rem; margin-top: 10px; }}
    .footer {{ background: #1a1a1a; color: white; padding: 30px; text-align: center; margin-top: 50px; }}
    .section-title {{ color: #e11d48; font-size: 1.8rem; margin: 30px 0 20px; border-left: 4px solid #e11d48; padding-left: 15px; }}
    .back-link {{ display: inline-block; margin-bottom: 20px; color: #e11d48; text-decoration: none; }}
    .no-news {{ text-align: center; padding: 50px; color: #666; }}
  </style>
</head>
<body>
  <header class="header">
    <h1>📰 झारखंड न्यूज़</h1>
  </header>
  <nav class="nav">
    <a href="/">Home</a>
    <a href="/jharkhnd_news/category/jharkhand">झारखंड</a>
    <a href="/jharkhnd_news/category/jobs">नौकरी</a>
    <a href="/jharkhnd_news/category/sports">खेल</a>
    <a href="/jharkhnd_news/category/education">शिक्षा</a>
  </nav>
  <div class="container">'''

def create_page_footer():
    return '''  <footer class="footer">
    <p>&copy; 2026 झारखंड न्यूज़ | All Rights Reserved</p>
  </footer>
</body>
</html>'''

# Generate main index.html
index_html = create_page_header("Home")
index_html += '<h2 class="section-title">ताज़ा खबर</h2><div class="news-grid">'

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
      </div>'''

index_html += '</div>' + create_page_footer()

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

# Generate category pages - ALL categories, even if empty
for cat_id, cat_name in categories.items():
    cat_news = [n for n in news_items if n['category'] == cat_id]
    
    os.makedirs(f'category/{cat_id}', exist_ok=True)
    cat_html = create_page_header(cat_name)
    cat_html += f'<a href="/" class="back-link">← Back to Home</a>'
    cat_html += f'<h2 class="section-title">{cat_name}</h2>'
    
    if cat_news:
        cat_html += '<div class="news-grid">'
        for news in cat_news:
            cat_html += f'''
        <div class="news-card">
          <img src="{news['image']}" alt="{news['title']}">
          <div class="news-card-content">
            <span class="category">{cat_name}</span>
            <h3>{news['title']}</h3>
            <p>{news['summary']}</p>
            <p class="date">📅 {news['date']}</p>
          </div>
        </div>'''
        cat_html += '</div>'
    else:
        cat_html += f'''
        <div class="no-news">
          <h3>कोई समाचार उपलब्ध नहीं</h3>
          <p>जल्द ही {cat_name} समाचार यहां आएंगे।</p>
        </div>'''
    
    cat_html += create_page_footer()
    
    with open(f'category/{cat_id}/index.html', 'w', encoding='utf-8') as f:
        f.write(cat_html)

print(f"✅ Generated index.html + {len(categories)} category pages with {len(news_items)} news articles")
