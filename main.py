import random

ideas_by_category = {
    "работа": [
        "Автоматизировать учёт расходов",
        "Создать CRM для малого бизнеса",
        "Разработать систему онбординга сотрудников",
        "Сделать дашборд для отслеживания KPI"
    ],
    "хобби": [
        "Написать книгу",
        "Изучить игру на гитаре",
        "Вести блог о путешествиях",
        "Освоить фотографию"
    ],
    "технологии": [
        "Создать мобильное приложение для заметок",
        "Открыть онлайн-курс по программированию",
        "Сделать Telegram-бота для погоды",
        "Разработать расширение для браузера"
    ]
}

def get_user_category():
    """Запрашивает категорию у пользователя"""
    print("Доступные категории:")
    for i, category in enumerate(ideas_by_category.keys(), 1):
        print(f"{i}. {category.capitalize()}")
    
    while True:
        choice = input("\nВыберите категорию (1-3): ").strip()
        if choice in ["1", "2", "3"]:
            categories = list(ideas_by_category.keys())
            return categories[int(choice) - 1]
        print("❌ Неверный выбор, попробуйте снова.")

def save_idea(idea):
    """Сохраняет идею в файл favorites.txt"""
    with open("favorites.txt", "a", encoding="utf-8") as f:
        f.write(idea + "\n")
    print("✅ Идея успешно сохранена в favorites.txt!")

def main():
    category = get_user_category()
    idea = random.choice(ideas_by_category[category])
    print(f"\n💡 Ваша идея в категории «{category}»: {idea}")
    
    save_choice = input("\nХотите сохранить эту идею? (да/нет): ").strip().lower()
    if save_choice in ["да", "д", "yes", "y"]:
        save_idea(idea)

if __name__ == "__main__":
    main()
