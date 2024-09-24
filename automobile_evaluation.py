import numpy as np
import pandas as pd

car_dataset = pd.read_csv('/Users/olly/Downloads/car_eval_dataset.csv')
print(car_dataset.head())

manufacturer_country_freq = car_dataset.manufacturer_country.value_counts()
print("manufacturer by country frequency:", manufacturer_country_freq)

manufacturer_country_prop = car_dataset.manufacturer_country.value_counts()/len(car_dataset.manufacturer_country)
print("manufacturer by country proportion:", manufacturer_country_prop)

# print(car_dataset['buying_cost'].unique())
buying_cost_catergories = ['low', 'med', 'high', 'vhigh']
car_dataset['buying_cost'] = pd.Categorical(car_dataset['buying_cost'], buying_cost_catergories, ordered=True)
print(car_dataset['buying_cost'].unique())

median_buying_cost = np.median(car_dataset['buying_cost'].cat.codes)
print("median buying cost:", median_buying_cost)

luggage_prop = car_dataset.luggage.value_counts(dropna=False, normalize=True)
print("luggage proportion:", luggage_prop)

doors_5more = np.sum(car_dataset.doors == '5more')
print("5+ doors total:", doors_5more)
doors_5more_prop = doors_5more/len(car_dataset['doors'])
print("5+ doors proportion:", doors_5more_prop)