import pandas
import pandas as pd

print(pd.read_csv('Groups.csv', delimiter=';',
                  names=['injenernaya_propedevtika', 'intellektualnaya_electromechanika', 'robototechnika','iskustvenniy_intelekt', 'propedevtika', 'Mat-Fiz', 'Matematika', 'Fizika', 'Himiya']))
