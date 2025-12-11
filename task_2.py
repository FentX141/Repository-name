salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
Gleb_Borisovich = months  # Новая переменная, чтобы в конце к переменной months не присваивалось значение 0
while Gleb_Borisovich > 0:
    money_capital = money_capital + (spend - salary)
    spend *= (1+ increase)
    Gleb_Borisovich -= 1
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital))
