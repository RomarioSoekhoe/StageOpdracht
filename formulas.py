import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# store the adress of the data in an var datapath
datapath = 'data\\tomslee.csv'

# store the data in a var accommodations
accommodations = pd.read_csv(datapath)

# prices from all accomodations
prices = (accommodations['price'])

# Class to calculate several statistic formula's
class Berekening:
    # method to calculate the standard deviation
    def std(x):
        return np.std(x)
    # method to calculate the T-Score
    def tscore(x, u, n):
        score = (np.mean(x) - np.mean(u)) / (Berekening.std(x) / (np.sqrt(n)))
        data = {'std': Berekening.std(x),
                'tscore': score,
                'sigmoid': Berekening.sigmoid(score)}
        return data
    # method to calculate the Sigmoïd.
    def sigmoid(t):
        return 1/(1 +np.exp(-t))

class Diagrammen:
    def staaf(self):
        # staafdiagram soorten accomodaties en hoeveelheid.
        df = pd.DataFrame()

        # check hoeveel een bepaalde type voorkomt in onze databestand.
        sharedroom = [a for a in accommodations['room_type'] if 'Shared room' in a]
        privateroom = [a for a in accommodations['room_type'] if 'Private room' in a]
        entirehome = [a for a in accommodations['room_type'] if 'Entire home/apt' in a]

        # het maken van de data voor de barplot.
        df['Room Type'] = ['Shared room', 'Private room', 'Home/Apartment']
        df['Aantal'] = [len(sharedroom), len(privateroom), len(entirehome)]

        sns.barplot(x='Room Type', y='Aantal', data=df)
        plt.show()
    def circle(self):
        # circel diagram van de hoeveelheid acomodaties per buurt
        df = pd.DataFrame(accommodations)
        arraybuurt = np.unique(df['neighborhood'], return_counts=True)


        buurtnamen = arraybuurt[0]  # buurtnamen
        sizes = arraybuurt[1]  # aantal accomodaties per buurt

        patches, texts = plt.pie(sizes, labels=buurtnamen, shadow=False, startangle=90)
        # plt.legend(patches, buurtnamen, loc='best')
        plt.axis('equal')

        plt.show()
    def correlation(selfs):
        # correlatiediagram tussen prijs en gemiddelde beoordeling
        sns.jointplot(data=accommodations, x='overall_satisfaction', y='price')
        plt.show()


