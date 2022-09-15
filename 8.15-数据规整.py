import pandas as pd
import numpy as np
from numpy import nan as NA

if __name__ == '__main__':
    data = pd.Series(np.random.randn(9),
                     index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
                            [1, 2, 3, 1, 3, 1, 2, 2, 3]])

    print(data)
    print(data['b'])
    print(data.loc[:, 2])

    print(data.unstack())
    print(data.unstack().stack())

    frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
                         index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                         columns=[['Ohio', 'Ohio', 'Colorado'],
                                  ['Green', 'Red', 'Green']])
    print(frame)
    frame.index.names = ['key1', 'key2']
    frame.columns.names = ['state', 'color']
    print(frame)

    # g根据级别汇总统计:吧key2相同的加起来
    print(frame.sum(level='key2'))

    frame = pd.DataFrame({'a': range(7), 'b': range(7, 0, -1),
                          'c': ['one', 'one', 'one', 'two', 'two',
                                'two', 'two'],
                          'd': [0, 1, 2, 0, 1, 2, 3]})
    print(frame)
    print(frame.set_index(['c', 'd']))
    print(frame.set_index(['c', 'd'], drop=False))

    s1 = pd.Series([0, 1], index=['a', 'b'])
    s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
    s3 = pd.Series([5, 6], index=['f', 'g'])
    print(pd.concat([s1, s2, s3]))
    print(pd.concat([s1, s2, s3], axis=1))
    s4 = pd.concat([s1, s3])
    print(pd.concat([s1, s4], axis=1))
    print(pd.concat([s1, s4], axis=1, join='inner'))
    result = pd.concat([s1, s1, s3], keys=['one', 'two', 'three'])
    print(result)
    # 如果沿着axis=1对Series进行合并，则keys就会成为DataFrame的列头：
    print(pd.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'three']))
