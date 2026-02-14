import requests

def get_dog_data():
    # URL відкритого API для отримання випадкового фото собаки
    url = "https://dog.ceo/api/breeds/image/random"

    try:
        # 1. Відправляємо GET-запит на сервер 
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        # Отримуємо саме посилання
        image_url = data['message']

        # 3. Витягуємо породу з URL
        breed = image_url.split('/')[-2]

        # 4. Виводимо результат в консоль, як просить завдання
        print("-" * 30)
        print(" ГЕНЕРАТОР СОБАК ")
        print("-" * 30)
        print(f"Порода: {breed.upper()}") 
        print("-" * 30) 

    except requests.RequestException as e:
        print(f"Сталася помилка при підключенні до API: {e}")

if __name__ == "__main__":
    get_dog_data()
