# population_data
import pandas as pd
data_population = {'Caralina'}
data = {
    'State': ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania', 'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan'],
    'Population': [39538223, 29145505, 21538187, 20201249, 13002700, 12812508, 11799448, 10711908, 10439388, 10077331]
}

df = pd.DataFrame(data)

def population_stats(df):
    print("Population statistics of US States:")
    print(f"Total number of states: {df.shape[0]}")
    print(f"State with the highest population: {df.loc[df['Population'].idxmax()]}")  # Находим штат с самым большим населением
    print(f"State with the lowest population: {df.loc[df['Population'].idxmin()]}")  # Находим штат с самым маленьким населением
    print(f"Average population of states: {df['Population'].mean()}")

population_stats(df)

df.to_csv('us_population_data.csv', index=False)
