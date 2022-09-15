import pandas as pd
import numpy as np
from numpy import nan as NA

if __name__ == '__main__':
    data = pd.Series([1, NA, 3.5, NA, 7])
    print(data.dropna())
    print(data[data.notnull()])

    df = pd.DataFrame(np.random.randn(7, 3))
    df.iloc[:4, 1] = NA
    df.iloc[:2, 2] = NA
    print(df)
    print(df.dropna())
    print(df.dropna(thresh=2))

    print(df.fillna(0))
    print(df.fillna({1: 0.5, 2: 1}))

    data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'],
                         'k2': [1, 1, 2, 3, 3, 4, 4]})
    print(data.duplicated())
    print(data.drop_duplicates(keep='first'))
    print(data.drop_duplicates(keep='last'))

    data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon',
                                  'Pastrami', 'corned beef', 'Bacon',
                                  'pastrami', 'honey ham', 'nova lox'],
                         'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
    print(data)
    meat_to_animal = {
        'bacon': 'pig',
        'pulled pork': 'pig',
        'pastrami': 'cow',
        'corned beef': 'cow',
        'honey ham': 'pig',
        'nova lox': 'salmon'
    }
    lowercased = data['food'].str.lower()
    data['animal'] = lowercased.map(meat_to_animal)
    print(data)

    data = pd.Series([1., -999., 2., -999., -1000., 3.])
    print(data.replace(-999, NA))
    print(data.replace([-999, -1000], NA))
    print(data.replace([-999, -1000], [NA, 0]))
    print(data.replace({-999: NA, -1000: 0}))

    ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
    bins = [18, 25, 35, 60, 100]
    cats = pd.cut(ages, bins)
    print(cats)
    print(cats.codes)
    print(cats.categories)
    print(pd.value_counts(cats))
    group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
    print(pd.cut(ages, bins, labels=group_names))

    print(pd.cut(ages, [18, 26, 36, 61, 100], right=False))



