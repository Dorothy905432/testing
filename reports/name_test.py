class Name:
    def __init__(self, name, hobby) -> None:
        if name not in ["Богдан", "Анонім", "Віталій"]:
            raise ValueError("Дозволені імена: Богдан, Анонім, Віталій")
        assert hobby.strip() != "", "Хобі не може бути порожнім!"
        self.name = name
        self.hobby = hobby

# Некоректний приклад (помилки)
# a = Name("Бодько", "малювання")  # ім’я не з дозволених
# b = Name("Богдан", "")         # порожнє хобі

# Коректний приклад
c = Name("Віталій", "малювання")
print(f"Ім'я: {c.name}, хобі: {c.hobby}")
