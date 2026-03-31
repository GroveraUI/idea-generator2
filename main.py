.gitignore __pycache__/.рус
import random
ideas = [
    "Написать книгу",
    "Создать мобильное приложение для заметок",
    "Открыть онлайн-курс по программированию",
    "Автоматизировать учёт расходов",
    "Сделать Telegram-бота для погоды"
]
def main():
    idea = random.choice(ideas)
    print(f"Ваша идея: {idea}")
if __name__ == "__main__":
    main()
