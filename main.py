import pandas as pd

pd.options.display.max_rows = 10

unames = ['movieId','title','genres']
movies = pd.read_table('examples/ml-latest-small/movies.csv', sep=',')
lnames = ['movieId','imdbId','tmdbId']
links = pd.read_table('examples/ml-latest-small/links.csv', sep=',')
rnames = ['userId','movieId','rating','timestamp']
ratings = pd.read_table('examples/ml-latest-small/ratings.csv', sep=',')
tnames = ['userId','movieId','tag','timestamp']
tags = pd.read_table('examples/ml-latest-small/tags.csv', sep=',')

# print(movies[:5])
# print(links[:5])
# print(ratings[:5])
# print(tags[:5])

data = pd.merge(pd.merge(ratings, links), movies)
print(data)


