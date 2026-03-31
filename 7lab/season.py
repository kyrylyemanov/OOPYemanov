from jikanpy import Jikan

jikan = Jikan()
# Правильний метод для jikanpy v4
now = jikan.seasons(extension='now')

print("--- Аніме поточного сезону ---")
for anime in now["data"][:10]:
    title = anime.get("title", "Без назви")
    score = anime.get("score", "Немає оцінки")
    print(f"Назва: {title} | Оцінка: {score}")