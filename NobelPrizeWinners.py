# Loading in required libraries
import pandas as pd


nobel = pd.read_csv('data/nobel.csv')


'''
Getting the top_gender and top_country using .value_counts()
'''

top_gender = nobel['sex'].value_counts().index[0]
top_country = nobel['birth_country'].value_counts().index[0]

'''
Getting decade had the highest ration of US-born Nobel Prize winners to total winners in all categories.

1. Check if the winner nationality = winner birth country == United States of America
2. Calculate the decade using modulo
3. Grup the decade and the country based on #1 criteria
4. Get the max_decade_usa using .max on the #1 variable
'''

nobel['usa_born_winners'] = nobel['birth_country'] == 'United States of America'
nobel['decade'] = nobel['year'] - (nobel['year'] % 10)
max_decade_usa = nobel.groupby('decade')['usa_born_winners'].mean().idxmax()

'''
Create a max_female_dict with the decade is the key and the category is the value. There should only be one key:value pair.

Based on the max_female_dict, who is first_woman_name and the first_woman_category
'''

nobel['female_winner'] = nobel['sex'] == 'Female'
df_female = nobel.groupby(['decade', 'category'], as_index=False)['female_winner'].mean()
max_female_row = df_female.loc[df_female['female_winner'].idxmax()]

max_female_dict = {
    max_female_row['decade']: max_female_row['category']
}

first_woman_winner_row = nobel[nobel['female_winner']].loc[nobel[nobel['female_winner']]['year'].idxmin()]
first_woman_name = first_woman_winner_row['full_name']
first_woman_category = first_woman_winner_row['category']

'''
Getting info for the winners that won more one Nobel Prize throughout the years and store as repeat_list
'''

repeat_list = nobel['full_name'].value_counts()
repeat_list = list(repeat_list[repeat_list >= 2].index)
