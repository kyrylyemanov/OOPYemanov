import requests

def get_cat_fact():
    print("🐾 Звертаємось до сервера за фактом про котів...")
    url = "https://catfact.ninja/fact"
    
    try:
        # Робимо запит за допомогою нашої бібліотеки requests
        response = requests.get(url)
        response.raise_for_status()  # Перевіряємо, чи немає помилок
        
        # Дістаємо текст факту з JSON-відповіді
        data = response.json()
        print(f"\n💡 Цікавий факт: {data['fact']}")
        
    except Exception as e:
        print(f"❌ Сталася помилка: {e}")

if __name__ == "__main__":
    get_cat_fact()