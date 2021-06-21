import pandas as pd
import numpy as np
string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'])
#print(string_data.isnull())
tot = sum(string_data.isnull())
#print("tot = ", tot)
string_data = string_data.fillna(method = "bfill")
print("without NA:\n", string_data)
# passing list of dicts
dicts = [{2001: 4.2, 2002: 5.6}, {2002: 12, 2003: 3433}]
data = pd.DataFrame(dicts)
print("data from list of dictionary: \n", data)
"""
Handling missing data in DataFrame
"""
data = pd.DataFrame([[1., 6.5, 3.], [1., np.nan, np.nan], [np.nan, np.nan, np.nan], [np.nan, 6.5, 3.]])
a = 1
print(data)
filler = {0:1, 1: 3, 2: -1}
# fil na can take other methods output as input
print("multifil = \n", data.fillna(filler))
# Duplicate data
data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['one'], 'k2': [0, 1, 2, 3, 3, 4, 0]})
print("data\n",data)
print("removed k2 :\n",data.drop_duplicates())
print("removed first Duplicate: \n", data.drop_duplicates(keep = "last"))
# data transformation with funcations and mapping
data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon',
'Pastrami', 'corned beef', 'Bacon',
'pastrami', 'honey ham', 'nova lox'],
'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
print("foods\n",data)
meat_to_animal = {
'bacon': 'pig',
'pulled pork': 'pig',
'pastrami': 'cow',
'corned beef': 'cow',
'honey ham': 'pig',
'nova lox': 'salmon'
}
lowercased = data["food"].str.lower()
data['animal'] = lowercased.map(meat_to_animal)
data = pd.Series([1., -999., 2., -999., -1000., 3.])
data = data.replace(-999, np.nan)
print(data)
# reindexing with maping
data = pd.DataFrame(np.arange(12).reshape((3, 4)),
index=['Ohio', 'Colorado', 'New York'],
columns=['one', 'two', 'three', 'four'])
print(data)
reindexing = lambda x: x[:3].upper()
data.index = data.index.map(reindexing)
print("data after transformation\n", data)
# discretization and binning
print("discretization and binning")
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 40, 60, 100]
group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
data = pd.cut(ages, bins, labels = group_names, right = False)
print("age group divisions are\n", pd.value_counts(data))
# permutation and random Sampling
df = pd.DataFrame(np.arange(5 * 4).reshape((5, 4)))
sampler = np.random.permutation(5)
print("data = \n", df)
print("sampler: ", sampler)
print("permuted = \n", df.take(sampler))
print("sampled : \n", df.sample(3))
# computation indicator and dummy variables
df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
'data1': range(6)})
print("data for dummy = \n", df)
df_mod = df[["data1"]].join(pd.get_dummies(df.key, prefix = "dummy_key"))
print("==========================================")
print("modified data\n", df_mod)
mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table("movies.dat", sep='::', header = None, names = mnames, engine = "python")
generes = []
for x in movies.genres:
	generes.extend(x.split("|"))
#print(generes)
genere = pd.unique(generes)

print("generes: \n", genere)
# doing computation indicator on this complex system
# complex in the sense that single column has multiple categories
empty_matrix = np.zeros((len(movies), len(genere)))
dummies = pd.DataFrame(empty_matrix, columns=genere)
for i, gen in enumerate(movies.genres):
	indices = dummies.columns.get_indexer(gen.split("|"))
	# this will give a list of generes splitup by split for single entry
	dummies.iloc[i, indices] = 1
movies_windic = movies.join(dummies.add_prefix('Genre_'))
print(movies_windic.iloc[3])
#print(movies[:10])












