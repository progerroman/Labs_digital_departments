money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
months = 0  # Счетчик месяцев

# Пока есть деньги в подушке безопасности
while money_capital > 0:
    deficit = spend - salary  # Рассчитываем дефицит за месяц
    money_capital -= deficit  # Уменьшаем подушку безопасности на дефицит
    if money_capital < 0:
        break  # Выход, если деньги закончились
    spend *= (1 + increase)  # Увеличиваем расходы на 5% для следующего месяца
    months += 1  # Увеличиваем счетчик месяцев

print("Количество месяцев, которое можно протянуть без долгов:", months)

