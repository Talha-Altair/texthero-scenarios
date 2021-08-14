from faker import Faker
import pandas as pd

fake = Faker()

df = pd.DataFrame()

name_list = []

for _ in range(10000):
    name_list.append(fake.name())

df['name'] = name_list

df.to_csv('names.csv',index=False)