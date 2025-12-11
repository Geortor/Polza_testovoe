import requests

BOT_TOKEN = "8384102367:AAF8HfVja7P3UKb8_Xs2VShlAs7yK6hWIZ8" #вообще его лучше спрятать, но пока пускай будет так
CHAT_ID = "678636670"
FILE_PATH = "message.txt"

def send_file_content():
    try:
        # 1. Читаем файл
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            text = f.read()

        if not text.strip():
            print("Файл пуст, нечего отправлять.")
            return

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        data = {
            "chat_id": CHAT_ID,
            "text": text
        }

        response = requests.post(url, data=data)

        if response.status_code == 200:
            print("Успешно отправлено!")
        else:
            print(f"Ошибка Telegram: {response.text}")

    except FileNotFoundError:
        print(f"Файл {FILE_PATH} не найден.")
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    send_file_content()
