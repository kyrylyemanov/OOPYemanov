from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def home():
    print("Завантажую аніме...")
    
    # Звертаємось безпосередньо до відкритого API (це надійно на 100%)
    url = "https://api.jikan.moe/v4/seasons/now"
    response = requests.get(url)
    now = response.json()
    
    html_content = """
    <html>
    <head>
        <title>Топ Аніме</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #f4f4f9; padding: 20px; }
            h1 { color: #333; }
            li { background: #fff; margin: 5px 0; padding: 10px; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        </style>
    </head>
    <body>
        <h1>🔥 Аніме поточного сезону</h1>
        <ul>
    """
    
    # Додаємо перші 10 аніме у список
    for anime in now.get("data", [])[:10]:
        title = anime.get("title", "Без назви")
        score = anime.get("score", "Немає оцінки")
        html_content += f"<li><strong>{title}</strong> (Оцінка: {score})</li>"
        
    html_content += """
        </ul>
    </body>
    </html>
    """
    
    return html_content

if __name__ == '__main__':
    app.run(debug=True)