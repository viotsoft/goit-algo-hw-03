import turtle

def koch_snowflake(t, length, level):
    """
    Функція для рекурсивного малювання сніжинки Коха.

    :param t: об'єкт turtle для малювання
    :param length: довжина сторони
    :param level: рівень рекурсії
    """
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_snowflake(t, length, level-1)  # Перша частина
        t.left(60)
        koch_snowflake(t, length, level-1)  # Друга частина
        t.right(120)
        koch_snowflake(t, length, level-1)  # Третя частина
        t.left(60)
        koch_snowflake(t, length, level-1)  # Четверта частина

def main():
    """
    Головна функція для запуску програми.
    """
    print("Малювання фракталу 'Сніжинка Коха'")
    level = int(input("Введіть рівень рекурсії (рекомендується 0-5): "))

    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Сніжинка Коха")

    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість малювання
    t.penup()
    t.goto(-150, 100)  # Позиціонування для центрування сніжинки
    t.pendown()

    # Малюємо сніжинку Коха як трикутник із трьома сторонами
    for i in range(3):
        koch_snowflake(t, 300, level)
        t.right(120)

    t.hideturtle()
    window.mainloop()

if __name__ == "__main__":
    main()
