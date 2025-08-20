from matplotlib import pyplot from pandas import read_csv
dataset =read_csv("disney_princess_popularity_dataset_300_rows.csv") dataset.hist()
pyplot.show()
from matplotlib import pyplot from pandas import read_csv
dataset = read_csv('disney_princess_popularity_dataset_300_rows.csv') d = dataset.head(15)
d.plot() pyplot.show()
from matplotlib import pyplot from pandas import read_csv
dataset = read_csv('disney_princess_popularity_dataset_300_rows.csv') d = dataset.head(10)
d.plot("InstagramFanPages") pyplot.show()
from matplotlib import pyplot from pandas import read_csv
dataset = read_csv('disney_princess_popularity_dataset_300_rows.csv') d = dataset.head(5)
d.plot(x="FirstMovieTitle",y="FirstMovieYear") pyplot.show()
import matplotlib.pyplot as plt from pandas import read_csv
dataset = read_csv('disney_princess_popularity_dataset_300_rows.csv') dataset.plot(kind='density')
plt.show()
import matplotlib.pyplot as plt from pandas import read_csv
dataset = read_csv('disney_princess_popularity_dataset_300_rows.csv') dataset.plot(kind='density',subplots=True,layout=(4,3))
plt.show()
from matplotlib import pyplot from pandas import read_csv
dataset = read_csv('disney_princess_popularity_dataset_300_rows.csv') data = dataset['MovieRuntimeMinutes'] data.head(20).plot(kind="bar",subplots=True, layout=(1,1)) pyplot.show()
from matplotlib import pyplot from pandas import read_csv
dataset = read_csv('disney_princess_popularity_dataset_300_rows.csv') data = dataset['MovieRuntimeMinutes'] data.plot(kind="box",subplots=True, layout=(1,1))
pyplot.show()