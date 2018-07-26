import formulas as F

# Define a array named sample
sample = []

# For loop. Create a sample of a certain roomtype.
for i, A in F.accommodations.iterrows():
    if A['room_type'] == 'Shared room':
        # add the price where the roomtype is Shared room to the sample []
        sample.append(A['price'])

# return the answers get from Berekening class
Uitkomst = F.Berekening.tscore(sample, F.prices, len(sample))

# print(Uitkomst)
# print(F.Berekening.std(prices))
print("Standaard Deviatie: ", Uitkomst['std'])
print("T-Score: ", Uitkomst['tscore'])
print("Sigmoïd: ", Uitkomst['sigmoid'])

# execute function of making a box diagram
F.Diagrammen.staaf(0)

# execute function of making a circle diagram
F.Diagrammen.circle(0)

# execute function of making a correlation diagram
F.Diagrammen.correlation(0)


