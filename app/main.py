from app.simulation import Simulation

if __name__ == "__main__":
    height, width = 0, 0
    while True:
        print("Введите высоту и ширину карты от 5 до 20 через пробел (5 5)")
        user_input = input("->")
        if len(user_input.split()) != 2:
            print(
                "Неверный формат ввода! Введите 2 целых числа от 5 до 20 через пробел (5 5)",
                end="\n\n",
            )
            continue

        height, width = user_input.split()
        if (
            height.isdigit()
            and width.isdigit()
            and 4 < int(height) < 21
            and 4 < int(width) < 21
        ):
            break

        print(
            "Неверный формат ввода! Введите 2 целых числа от 5 до 20 через пробел (5 5)",
            end="\n\n",
        )

    simulation = Simulation(int(height), int(width))
    simulation.start_simulation()
