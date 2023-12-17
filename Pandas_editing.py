
import pandas as pd

data = pd.read_csv('Groups.csv', delimiter=';', names=['injenernaya_propedevtika', 'intellektualnaya_electromechanika', 'robototechnika','iskustvenniy_intelekt', 'propedevtika', 'Mat-Fiz', 'Matematika', 'Fizika', 'Himiya'])
print(data)

row_num = int(input("Введите номер строки: "))
col_num = int(input("Введите номер столбца: "))

new_value = input("Введите новое значение: ")
data.iloc[row_num, col_num] = new_value

data.to_csv('Groups.csv', sep=';', header=False, index=False)

print("\nОбновленные данные:")
print(data)