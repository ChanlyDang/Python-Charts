
# csv and matplotlib to read csv files and make charts easier
import csv
from matplotlib import pyplot as plt

# opening the csv file and reading contents
with open('DV_sample.csv') as data:
    reader = csv.reader(data)
    # a is the labels for the pie chart slices
    a = next(reader)
    b = next(reader)
    c = next(reader)
    d = next(reader)
    # e is the values for the pie chart
    e = next(reader)
# removing the first element that should not be a part of the data for pie chart
a.pop(0)
e.pop(0)

print(a)
print(e)
# renamed variables for easier use
x = e
y = a
# make the pie chart
plt.title('Market Share of Companies Chart')
# pie chart is small, so company name overlap
plt.pie(x, labels=y, radius=1.1)
# showing the pie chart
plt.show()
# Answer, the second largest market share looks to be Apple based on the pie chart
"""
# Prob. 2
# import pandas and matplotlib to make load data and make bar chart
import pandas as pd
from matplotlib import pyplot as plt

# opening the csv file and reading contents
data = pd.read_csv('DV_sample.csv')
# columns for Data and Huawei
x = data['Date']
y = data['Huawei']

# changing figure size for visbility
plt.figure(figsize=(15,10))
# titles and labels of axes
plt.title('Market Share of Huawei')
plt.xlabel('Date')
plt.ylabel('Market Share')
# make bar chart
plt.bar(x, y, color = 'red')
# displaying he bar chart
plt.show()


"""














