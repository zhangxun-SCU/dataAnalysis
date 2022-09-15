import pandas as pd
from pandas import Series, DataFrame
import numpy as np

# import pandas_datareader.data as web

if __name__ == '__main__':
    # Series
    # Series是一种类似于一维数组的对象，
    # 它由一组数据（各种NumPy数据类型）以及一组与之相关的数据标签（即索引）组成
    obj = Series([4, 7, -5, 3])
    print(obj)
    print(obj.values)
    print(obj.index)
    obj2 = pd.Series([4, 7, -5, 3], index=['a', 'b', 'c', 'd'])
    print(obj2)
    # 类似字典
    print('b' in obj2)
    print('e' in obj2)
    print(np.exp(obj2))
    # 通过字典可以直接创建Series
    sDate = {
        'Ohio': 35000,
        'Texas': 71000,
        'Oregon': 16000,
        'Utah': 5000,
    }
    obj3 = pd.Series(sDate)
    print(obj3)

    # 或NA表示缺失数据。pandas的isnull和notnull函数可用于检测缺失数据
    states = ['California', 'Ohio', 'Oregon', 'Texas']
    obj4 = pd.Series(sDate, index=states)
    print(obj4)
    print(pd.isnull(obj4))
    print(pd.notnull(obj4))
    print(obj4.isnull())

    # DataFrame
    # 由Series组成的字典
    data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
            'year': [2000, 2001, 2002, 2001, 2002, 2003],
            'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
    frame = pd.DataFrame(data)
    print(frame)
    print(frame.head())
    frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five',
                                                                                 'six'])
    print(frame2)
    print(frame2.columns)
    # 通过类似字典标记的方式或属性的方式，可以将DataFrame的列获取为一个Series
    # 即frame[columns] 是Series
    # 列可以通过赋值的方式修改
    frame2['debt'] = 16.5
    print(frame2)
    frame2['debt'] = np.arange(6.0)
    print(frame2)
    # 为不存在的列赋值会创建出一个新列。关键字del用于删除列。
    frame2['eastern'] = (frame2.state == 'Ohio')
    print(frame2)
    del frame2['eastern']
    print(frame2.columns)
    # 通过Series的copy方法即可指定复制列
    a = frame2['debt'].copy()
    print(a)

    pop = {'Nevada': {2001: 2.4, 2002: 2.9},
           'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
    frame3 = pd.DataFrame(pop)
    print(frame3)
    print(frame3.T)
    print(pd.DataFrame(pop, index=[2001, 2002, 2003]))
    # 还可以由Series组成的字典直接创建DataFrame

    print(frame3.values)

    obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
    print(obj)
    obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
    print(obj2)

    obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
    new_obj = obj.drop('c')
    print(obj)
    print(new_obj)

    data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                        index=['Ohio', 'Colorado', 'Utah', 'NewYork'],
                        columns=['one', 'two', 'three', 'four'])
    print(data)
    print(data.drop(['Colorado', 'Ohio']))
    print(data.drop('two', axis=1))
    print(data.drop(['two', 'four'], axis='columns'))

    print(obj)
    obj.drop('c', inplace=True)
    print(obj)

    print(data < 5)

    frame = pd.DataFrame(np.arange(8).reshape((2, 4)),
                         index=['three', 'one'],
                         columns=['d', 'a', 'b', 'c'])
    print(frame.sort_index())
    print(frame.sort_index(axis=1, ascending=False))
    df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5],
                       [np.nan, np.nan], [0.75, -1.3]],
                      index=['a', 'b', 'c', 'd'],
                      columns=['one', 'two'])
    print(df.idxmax())
    # print(df[df.idxmax()])
    print(df['one']['b'])

    # all_data = {ticker: web.get_data_yahoo(ticker)
    #             for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']}
    #
    # price = pd.DataFrame({ticker: data['Adj Close']
    #                      for ticker, data in all_data.items()})
    # volume = pd.DataFrame({ticker: data['Volume']
    #                       for ticker, data in all_data.items()})
    # returns = price.pct_change()
    # returns.tail()

    obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
    uniques = obj.unique()
    uniques.sort()
    print(uniques)
    print(obj.value_counts())

    data = pd.DataFrame({'Qu1': [1, 3, 4, 3, 4],
                         'Qu2': [2, 3, 1, 2, 3],
                         'Qu3': [1, 5, 2, 4, 4]})
    print(data)
    result = data.apply(pd.value_counts).fillna(0)
    print(result)
    data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
            'year': [2000, 2001, 2002, 2001, 2002, 2003],
            'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
    frame = pd.DataFrame(data)
    print(frame)
    print(frame['state'])
    print(frame.loc[[0, 1], ['state', 'year']])
