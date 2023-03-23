from utils.utils import correct_input, change_calculation

denomination = {'5000', '1000', '500', '100', '50', '10', '5', '2', '1', '0.5', '0.1', '0.05', '0.01'}

sum_total = input('Введите итоговую сумму: ')
total_money = input('Введите внесенные купюры через пробел.')

all_total, all_money = correct_input(sum_total, total_money)

print('Выдать сдачу покупателю: ', change_calculation(all_total, all_money))