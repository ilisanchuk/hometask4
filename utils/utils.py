def correct_input(sum_total, deposited_money):

    bills_and_pennies = sum_total.split('.')
    for i in bills_and_pennies:
        if not i.isdigit():
            raise TypeError('Неверный формат данных.')
    if len(bills_and_pennies) > 2:
            raise TypeError('Неверный формат данных.')
    elif len(bills_and_pennies) > 1:
        if int(bills_and_pennies[1]) > 99:
            raise ValueError('Копеек не может быть больше 99!')
    all_total = float(sum_total)

    list_of_money = deposited_money.split(' ')
    space = list_of_money.count('')
    all_money = 0
    for _ in range(space):
        list_of_money.remove('')
    for i in list_of_money:
        if i in denomination:
            all_money += float(i)
        else:
            raise ValueError('В россии ещё не появились такие купюры или монеты!')

    if all_money < all_total:
        raise ValueError('Увы, не хватает средств.')
    else:
        return all_total, all_money

def change_calculation(all_total, all_money):
    change = all_money - all_total
    list_of_denomination = sorted(map(float, list(denomination)), reverse=True)
    list_of_change = []
    for i in list_of_denomination:
        while float(i) <= change:
            list_of_change.append(i)
            change -= float(i)

    result_change = []
    for i in list_of_change:
        if i >= 1:
            result_change.append(int(i))
        else:
            result_change.append(float(i))
    return ' '.join(map(str, result_change))
denomination ={'5000', '1000', '500', '100', '50', '10', '5', '2', '1', '0.5', '0.1', '0.05', '0.01'}

if __name__ == '__main__':
    sum_total = input('Введите итоговую сумму: ')
    total_money = input('Введите внесенные купюры через пробел.')
    denomination ={'5000', '1000', '500', '100', '50', '10', '5', '2', '1', '0.5', '0.1', '0.05', '0.01'}

    all_total, all_money = correct_input(sum_total, total_money)

    print('Выдать сдачу покупателю: ', change_calculation(all_total, all_money))