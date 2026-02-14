import requests

def get_dog_data():
    # URL відкритого API для отримання випадкового фото собаки
    url = "https://dog.ceo/api/breeds/image/random"

    try:
        # 1. Відправляємо GET-запит на сервер 
        response = requests.get(url)

        # Перевіряємо, чи успішний запит (код 200)
        response.raise_for_status()

        # 2. Парсимо отриманий JSON в об'єкт Python 
        data = response.json()

        # Отримуємо саме посилання на картинку
        image_url = data['message']

        # 3. Витягуємо породу з URL
        # Посилання виглядає так: https://images.dog.ceo/breeds/poodle-standard/n02113799_2280.jpg
        # Розбиваємо текст по символу '/' і беремо передостанній елемент
        breed = image_url.split('/')[-2]

        # 4. Виводимо результат в консоль, як просить завдання [cite: 526]
        print("-" * 30)
        print("🐶 ГЕНЕРАТОР СОБАК 🐶")
        print("-" * 30)
        print(f"Порода: {breed.upper()}") # робимо великими літерами для краси
        print(f"URL фото: {image_url}")
        print("-" * 30) 

    except requests.RequestException as e:
        print(f"Сталася помилка при підключенні до API: {e}")

if __name__ == "__main__":
    get_dog_data()
